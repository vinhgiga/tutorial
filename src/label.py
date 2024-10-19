import os
import time

import google.generativeai as genai
import pandas as pd
from dotenv import load_dotenv
from google.api_core import retry
from tqdm.auto import tqdm

load_dotenv()
tqdm.pandas()
instruction = """
Bạn là chuyên gia gán nhãn dữ liệu. Bạn phải tuân theo quy tắc gán nhãn:
* ngon: url, nhiều kiến thức, thông tin.
* haha: vui vẻ, hài hước, độc đáo, bất ngờ.
* nhạt: nội dung nhàm chán, phổ biến, câu hỏi, thắc mắc.
Ví dụ:
ngon: "Combo mới của Python ruff + uv + rye quá xịn luôn"
haha: "bảo mật vượt trội vì ít người dùng thôi nhé"
nhạt: "Cho thêm info về combo này đi man"
"""
harm_list = [
    'HARM_CATEGORY_HARASSMENT',
    'HARM_CATEGORY_HATE_SPEECH',
    'HARM_CATEGORY_SEXUALLY_EXPLICIT',
    'HARM_CATEGORY_DANGEROUS_CONTENT',
]
genai.configure(api_key=os.environ["API_KEY"])

model = genai.GenerativeModel(
    "gemini-1.5-flash",
    system_instruction=instruction,
    generation_config=genai.GenerationConfig(
        response_mime_type="text/x.enum",
        response_schema={
            "type": "STRING",
            "enum": ["ngon", "haha", "nhạt"],
        },
        temperature=0.0,
    ),
    safety_settings=[
        {
            "category": harm,
            "threshold": "BLOCK_NONE",
        }
        for harm in harm_list
    ],
)


def make_predict(model: genai.GenerativeModel):
    @retry.Retry(timeout=300.0)
    def predict(comment: str) -> str:
        max_length = 500
        response = model.generate_content(comment[:max_length])
        # 10 requests per minute
        time.sleep(10 / 60)
        return response.text

    return predict


df = pd.read_excel("data/comments.xlsx")
df["label"] = df["comment"].progress_apply(make_predict(model=model))
df.to_excel("data/comments_label.xlsx", index=False)

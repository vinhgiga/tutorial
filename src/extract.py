import json
import re

import pandas as pd
from bs4 import BeautifulSoup


def preprocess_text(text: str) -> str:
    # remmove extra whitespaces
    text = re.sub(" +", " ", text)
    # remove duplicate newlines
    text = re.sub("\n+", "\n", text).strip()
    return text


def get_text_without_quotes(html_content: str) -> str:
    soup = BeautifulSoup(html_content, "html.parser")
    for quote in soup.find_all("blockquote"):
        quote.decompose()
    text = soup.get_text()
    text = preprocess_text(text)
    return text


def is_long_text(text: str) -> bool:
    return len(text) > 9


# load the data
with open("data/data.json", encoding="utf-8") as f:
    data = json.load(f)
# sort data by page number
data["page"] = sorted(data["page"], key=lambda x: x["num"])
post_id_list = []
comment_list = []
# load page
for page in data["page"]:
    page_content = page["content"]
    soup = BeautifulSoup(page_content, "html.parser")
    for message in soup.find_all("div", class_="message-main js-quickEditTarget"):
        post_id_element = message.find("a", class_="message-attribution-gadget")["href"]
        comment_element = message.find(
            "div", class_="message-userContent lbContainer js-lbContainer"
        )
        post_id = re.search(r"post-(\d+)", post_id_element).group(1)
        comment_text = get_text_without_quotes(str(comment_element))
        if is_long_text(comment_text):
            post_id_list.append(post_id)
            comment_list.append(comment_text)

# save the messages to excel file
df = pd.DataFrame({"id": post_id_list, "comment": comment_list})
df.to_excel("data/comments.xlsx", index=False)

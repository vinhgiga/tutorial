<div align="center">
<a href="https://youtu.be/XlX2NaVCiNw">
  <img src="https://github.com/user-attachments/assets/860eae8a-d710-4b0a-a957-dd2eeea21e6a">
  </a>
  <p>Nhấp vào hình thu nhỏ để xem video 23 phút hướng dẫn sử dụng Gemini API để phân loại bình luận.</p>
</div>


[English]("README_EN.md") | Tiếng Việt

## Nội dung trong video

- Giới thiệu quy trình xây dựng mô hình phân loại bình luận.
- Thiết lập dự án python với UV.
- Cấu hình Ruff và tích hợp vào VSCode.
- Trích xuất bình luận từ một [chủ đề VOZ](https://voz.vn/t/tat-tan-tat-ve-dich-vu-nextdns.522718/).
- Tạo và sử dụng Gemini API để phân loại bình luận theo nhãn ["ngon", "haha", "nhạt"].

## Yêu cầu tiên quyết

- Tài khoản Google.
- Windows 10 trở lên, kiến trúc 64bit.
- Cài đặt python 3.10 hoặc cao hơn trong máy.
- Giao diện dòng lệnh Git (Git CLI).
- Visual Studio Code.

## Cài đặt

1. Cài đặt uv và ruff:

   ```powershell
   $ pip install uv ruff
   ```

2. Nhân bản dự án trên máy của bạn:

   ```powershell
   $ git clone 'https://github.com/vinhgiga/tutorial.git'
   $ cd tutorial
   ```

3. Tạo môi trường ảo với python 3.10:

   ```powershell
   $ uv venv --python 3.10
   ```

4. Cài đặt các thư viện cần thiết:

   ```powershell
   $ uv pip install -r pyproject.toml
   ```

5. Lấy khóa API tại [Google AI Studio](https://aistudio.google.com/apikey).

   Tạo file `.env` bên trong thư mục gốc của dự án và thêm biến môi trường `API_KEY` bằng khóa của bạn. HOẶC bạn có thể chạy lệnh dưới đây. Nhớ thay thế `your_api_key` bằng khóa của bạn:

   ```powershell
   $ echo 'API_KEY=your_api_key' > .env
   ```

6. Chạy code python theo nhu cầu của bạn:

- Code `extract.py`: Đọc tệp JSON được xuất ra từ tiện ích mở rộng Chrome [SavePostForVoz](https://chromewebstore.google.com/detail/savepostforvoz/oknmbclpnggfejjadadcgdbhndgjcjgg), bóc tách bình luận và ghi vào tệp `comments.xlsx`
- Code `label.py`: Sử dụng Gemini API để gán nhãn bình luận từ tệp `comments.xlsx` và xuất vào tệp `comments_label.xlsx`

  ```powershell
  $ uv run extract.py
  $ uv run label.py
  ```

## Đọc thêm

- [Tài liệu Gemini API](https://ai.google.dev/gemini-api/docs).
- [Tài liệu thư viện Langchain](https://python.langchain.com/docs/tutorials/).
- [Dự án ruff](https://github.com/astral-sh/ruff).
- [Dự án uv](https://github.com/astral-sh/uv).
- [Python template cookiecutter](https://github.com/cookiecutter/cookiecutter).

## Giấy phép

Dự án này được cấp theo giấy phép Apache License 2.0 - xem tệp [LICENSE](/LICENSE) để biết chi tiết.

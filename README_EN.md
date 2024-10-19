<div align="center">
<a href="https://youtu.be/XlX2NaVCiNw">
  <img src="https://github.com/user-attachments/assets/860eae8a-d710-4b0a-a957-dd2eeea21e6a">
  </a>
  <p>Click on the thumbnail to watch a 23-minute video tutorial on using the Gemini API to classify comments.</p>
</div>

<p style="font-size: 2rem;">
    <a href="README.md">Tiếng Việt</a>
</p>

## Video Contents

- Introduction to the process of building a comment classification model.
- Setting up a Python project with UV.
- Configuring Ruff and integrating it into VSCode.
- Extracting comments from a [VOZ thread](https://voz.vn/t/tat-tan-tat-ve-dich-vu-nextdns.522718/).
- Creating and using the Gemini API to classify comments with labels ["good", "funny", "bad"].

## Prerequisites

- A Google account.
- Windows 10 or later, 64-bit architecture.
- Python 3.10 or higher installed on your machine.
- Git command-line interface (Git CLI).
- Visual Studio Code.

## Installation

1. Install UV and Ruff:

   ```powershell
   $ pip install uv ruff
   ```

2. Clone the project to your machine:

   ```powershell
   $ git clone 'https://github.com/vinhgiga/tutorial.git'
   $ cd tutorial
   ```

3. Create a virtual environment with Python 3.10:

   ```powershell
   $ uv venv --python 3.10
   ```

4. Install the required libraries:

   ```powershell
   $ uv pip install -r pyproject.toml
   ```

5. Get an API key from [Google AI Studio](https://aistudio.google.com/apikey).

   Create a `.env` file inside the root directory of the project and add the `API_KEY` environment variable with your key. OR you can run the command below. Remember to replace `your_api_key` with your actual key:

   ```powershell
   $ echo 'API_KEY=your_api_key' > .env
   ```

6. Run the Python code as needed:

   - `extract.py` code: Reads a JSON file exported from the Chrome extension [SavePostForVoz](https://chromewebstore.google.com/detail/savepostforvoz/oknmbclpnggfejjadadcgdbhndgjcjgg), extracts comments, and writes them to the `comments.xlsx` file.
   - `label.py` code: Uses the Gemini API to label comments from the `comments.xlsx` file and exports them to the `comments_label.xlsx` file.

   ```powershell
   $ uv run extract.py
   $ uv run label.py
   ```

## Learn more

- [Gemini API Documentation](https://ai.google.dev/gemini-api/docs).
- [Langchain Framework Documentation](https://python.langchain.com/docs/tutorials/).
- [Ruff Project](https://github.com/astral-sh/ruff).
- [UV Project](https://github.com/astral-sh/uv).
- [Python Template Cookiecutter](https://github.com/cookiecutter/cookiecutter).

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](/LICENSE) file for details.

import textwrap
from typing import List
from typing import cast

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()
client = OpenAI()


def write_response_content_to_txt(content, file_path):
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Response successfully written to {file_path}")
    except Exception as e:
        raise RuntimeError(f"Error writing response to file: {e}")


def read_data_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")


def wrap_text_preserving_paragraphs(content, max_line_length=100):
    wrapped_lines: List[str] = []

    for para in content.splitlines():
        if not para.strip():
            wrapped_lines.append("")
            continue

        wrapped = textwrap.wrap(
            para,
            width=max_line_length,
            break_long_words=False,
            break_on_hyphens=False,
            replace_whitespace=False
        )

        wrapped_lines.extend(wrapped if wrapped else [para])

    return "\n".join(wrapped_lines)


def generate_paragraph(system_prompt, prompt, max_line_length=100):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt}
    ]

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=cast(list, messages),
    )

    content = completion.choices[0].message.content.strip()
    return wrap_text_preserving_paragraphs(content, max_line_length)

from utils import generate_paragraph, write_response_content_to_txt, read_data_from_file


SYSTEM_PROMPT = """
You are an AI language model tasked with converting plain text into Markdown format following a predefined structure. 
The Markdown output must:
- Include a title as an H1 heading (# Title).
- Use H2 headings (##) for main sections.
- Apply bullet points (-) for lists.
- Preserve any code snippets inside triple backticks (```).
- Ensure proper spacing and readability.
- Do not add extra content beyond the original text; only reformat according to Markdown rules.
"""


PROMT = f"""
Convert the following text into Markdown format using the predefined structure with headings, bullet points, 
and code blocks where appropriate:
'{read_data_from_file("../file_output/task_2.txt")}'
"""


if __name__ == "__main__":
    result = generate_paragraph(system_prompt=SYSTEM_PROMPT, prompt=PROMT)
    write_response_content_to_txt(result, "../file_output/task_3.md")

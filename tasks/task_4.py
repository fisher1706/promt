from utils import generate_paragraph, write_response_content_to_txt, read_data_from_file


SYSTEM_PROMPT = """
You are an AI language model tasked with writing a letter that provides constructive negative feedback regarding a 
software developer's performance. The letter must:
- Be highly polite and professional in tone.
- Clearly outline specific areas where the developer made mistakes.
- Explain the impact of these issues on the project and the reasons for concern.
- Maintain a constructive approach, suggesting improvement rather than blame.
- If the initial draft lacks sufficient politeness or clarity, 
  iterate and refine until the tone and structure are appropriate.
"""


PROMT = f"""
Write a polite and professional letter that gives constructive negative feedback about a software developer's 
performance. The letter should include:
- Specific mistakes made by the developer.
- The impact of these mistakes on the project.
- Reasons for concern.
Ensure the tone is respectful and focused on improvement.
"""


if __name__ == "__main__":
    result = generate_paragraph(system_prompt=SYSTEM_PROMPT, prompt=PROMT)
    write_response_content_to_txt(result, "../file_output/task_4.txt")

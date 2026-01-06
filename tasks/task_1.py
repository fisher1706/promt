from utils import generate_paragraph, write_response_content_to_txt


SYSTEM_PROMPT = """
You are an AI language model tasked with generating clear, factual, and well-structured English text. 
Your goal is to create a concise paragraph that explains Linus Torvalds’ contributions to software development 
and technology innovation. The paragraph should:
- Highlight key achievements such as the creation of Linux and Git.
- Explain their impact on open-source software and modern development practices.
- Maintain a neutral, professional tone.
- Avoid unnecessary jargon or overly technical details.
"""


PROMT = """
Generate a paragraph in English about Linus Torvalds’ contributions to software development and technology innovation.
"""



if __name__ == "__main__":
    result = generate_paragraph(system_prompt=SYSTEM_PROMPT, prompt=PROMT)
    write_response_content_to_txt(result, "../file_output/task_1.txt")

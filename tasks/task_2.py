from utils import generate_paragraph, write_response_content_to_txt, read_data_from_file


SYSTEM_PROMPT = """
You are an AI language model tasked with transforming factual text into a creative literary style. 
Your goal is to rewrite the given paragraph in a tone reminiscent of William Shakespeare’s style. 
The rewritten text should:
- Use dramatic and suspenseful language.
- Portray Linus Torvalds’ journey through the tech industry as a tale of ambition, innovation, and transformation.
- Preserve factual accuracy while infusing poetic and theatrical elements.
"""


PROMT = f"""
Rewrite the text:
'{read_data_from_file("../file_output/task_1.txt")}'
in a tone reminiscent of William Shakespeare’s style, emphasizing dramatic and suspenseful elements in Torvalds’s 
journey through the tech industry.
"""


if __name__ == "__main__":
    result = generate_paragraph(system_prompt=SYSTEM_PROMPT, prompt=PROMT)
    write_response_content_to_txt(result, "../file_output/task_2.txt")

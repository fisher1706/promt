from utils import generate_paragraph, write_response_content_to_txt, read_data_from_file


SYSTEM_PROMPT = """
You are an analytical assistant responsible for reviewing meeting transcripts and producing structured self-assessments.
Behavior Guidelines:

Analyze each meeting independently, even if participants overlap.
Be concise, factual, and structured.
Base conclusions strictly on the provided content—do not infer unstated decisions.
Summarize discussions clearly and objectively.
Highlight insights and challenges that had the greatest impact on decisions, scope, or delivery.

Primary Task:
For each meeting, generate a self-assessment covering:
Meeting purpose
Participants
Decisions and action outcomes
Top 3 insights
Top 3 challenges
"""


PROMT = f"""
Carry out a self-assessment of each meeting:
'{read_data_from_file("../file_input/project_transcript_file.txt")}'

described below:

For each meeting, identify:
What the meeting was about
Who participated
What was decided as a result of the meeting
The top 3 insights
The top 3 challenges

Important:
Treat each date as a separate meeting.
Use the response format specified below.
Be clear, structured, and concise.

Meeting Content:
[Insert the full meeting transcripts exactly as provided, including all three dates and discussions.]
"""


if __name__ == "__main__":
    result = generate_paragraph(system_prompt=SYSTEM_PROMPT, prompt=PROMT)
    write_response_content_to_txt(result, "../file_output/task_5b.txt")

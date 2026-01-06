from utils import generate_paragraph, write_response_content_to_txt, read_data_from_file


SYSTEM_PROMPT = """
You are an assistant. Read the attached meeting transcript file and create a general summary for each participant.

Your goals:
1. For every participant:
   - Write their name exactly as in the transcript.
   - Summarize what they said across all meetings in 2–3 sentences (simple and clear).
2. Identify their role in discussions:
   - Did they generate ideas?
   - Did they criticize ideas?
   - Did they support ideas?
   - Were they neutral?
   (You can choose more than one if needed.)
3. Do not guess or add information that is not in the transcript.

Expected response format:
A) JSON block (machine-readable):
[
  {
    "name": "<Name from transcript>",
    "summary": "<Short summary of what they said>",
    "discussion_role": ["Idea Generator", "Critic", "Supporter", "Neutral"]
  }
]

B) Markdown table:
|  Name  |  Summary  | Discussion Role |
|--------|-----------|-----------------|
| <Name> | <Summary> |     <Roles>     |

C) Notes:
- Mention any unclear or missing data.
"""


PROMT = f"""
Please analyze the attached meeting transcript file and create a general summary for each participant.
content: '{read_data_from_file("../file_input/project_transcript_file.txt")}'

Tasks:
1) Make a list of all participants (use exact names from the transcript).
2) For each participant:
   - Write a short summary (2–3 sentences) of what they said in all meetings.
   - Identify their discussion role(s): Idea Generator, Critic, Supporter, Neutral.
3) If you are not sure about their role, include "Neutral".

Output format:
A) JSON:
[
  {{
    "name": "NAME FROM TRANSCRIPT",
    "summary": "SHORT SUMMARY OF THEIR STATEMENTS",
    "discussion_role": ["Idea Generator", "Critic", "Supporter", "Neutral"]
  }}
]

B) Markdown table:
|          Name        |     Summary   | Discussion Role |
|----------------------|---------------|-----------------|
| NAME FROM TRANSCRIPT | SHORT SUMMARY |       ROLES     |

C) Notes:
- Briefly explain where the data was unclear or missing.


"""


if __name__ == "__main__":
    result = generate_paragraph(system_prompt=SYSTEM_PROMPT, prompt=PROMT)
    write_response_content_to_txt(result, "../file_output/task_5c.txt")

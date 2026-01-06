from utils import generate_paragraph, write_response_content_to_txt, read_data_from_file


SYSTEM_PROMPT = """
You are an assistant. Read the attached meeting transcript file and write a professional email to all participants.

Tone:
- Optimistic and businesslike.
- Clear, concise, and positive.

What to include in the email:
1) A short summary of the three meetings (1–2 sentences per meeting).
2) The next steps (a simple bullet list with owners, if available).
3) A thank‑you mention for every participant by name (use names exactly as in the transcript).
4) A proposed date for the next meeting. If the transcript suggests a revisit window, choose a date inside that window; 
otherwise, pick a reasonable date soon after the last meeting.

Important rules:
- Use only information from the transcript (do not guess).
- Keep technology names and decisions exactly as written in the transcript.
- Keep the letter length ~250–400 words.
- Write in English.

Expected response format (follow exactly):
A) Subject line (one sentence).
B) Email body in Markdown:
   - Greeting
   - Meeting summaries (three short bullets, one per meeting)
   - Next steps (bulleted list)
   - Appreciation (thank each participant by name)
   - Next meeting date (YYYY‑MM‑DD)
   - Closing and signature

C) JSON metadata (machine‑readable), in a single code block:
{
  "participants_thanked": ["<Name1>", "<Name2>", "..."],
  "meetings_summary": [
    { "date": "<YYYY‑MM‑DD>", "summary": "<1–2 sentences>" },
    { "date": "<YYYY‑MM‑DD>", "summary": "<1–2 sentences>" },
    { "date": "<YYYY‑MM‑DD>", "summary": "<1–2 sentences>" }
  ],
  "next_steps": ["<Step 1>", "<Step 2>", "..."],
  "next_meeting_date": "<YYYY‑MM‑DD>"
}
"""


PROMT = f"""
Please read the attached meeting transcript file and write an optimistic, businesslike email to all participants.

Include:
1) A brief summary of each of the three meetings (one bullet per meeting).
2) A clear list of next steps (bulleted; include owners if mentioned).
3) A thank‑you to each participant by name (use names exactly as in the transcript).
4) A proposed date for the next meeting (YYYY‑MM‑DD). If the transcript mentions a revisit window, 
pick a date inside it; otherwise choose a sensible date after the last meeting.

Output format (please follow exactly):
A) Subject line.
B) Email body (Markdown sections: Greeting, Meeting summaries, Next steps, Appreciation, Next meeting date, Closing).
C) JSON metadata code block:
{{
  "participants_thanked": ["NAME1", "NAME2", "..."],
  "meetings_summary": [
    {{ "date": "YYYY‑MM‑DD", "summary": "TEXT" }},
    {{ "date": "YYYY‑MM‑DD", "summary": "TEXT" }},
    {{ "date": "YYYY‑MM‑DD", "summary": "TEXT" }}
  ],
  "next_steps": ["TEXT", "TEXT"],
  "next_meeting_date": "YYYY‑MM‑DD"
}}
Please analyze the attached meeting transcript file and create a general description of the project.

Use only information from:
'{read_data_from_file("../file_input/project_transcript_file.txt")}'
"""


if __name__ == "__main__":
    result = generate_paragraph(system_prompt=SYSTEM_PROMPT, prompt=PROMT)
    write_response_content_to_txt(result, "../file_output/task_5e.txt")

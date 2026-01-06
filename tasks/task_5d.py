from utils import generate_paragraph, write_response_content_to_txt, read_data_from_file


SYSTEM_PROMPT = """
You are an assistant. Read the attached meeting transcript file and create a simple, clear project description.

Goals (use only information from the transcript; do not guess):
1) Explain what the project is about (1–2 short sentences).
2) List the technologies used:
   - Frontend (frameworks, libraries, UI considerations),
   - Backend (frameworks, services),
   - Data storage (databases, caches),
   - Any other relevant layers (UX/UI, QA/testing, performance, infrastructure).
3) Describe current problems or challenges mentioned in the meetings.
4) Describe what is planned to be implemented in the near future.

Rules:
- Keep technology names and terms exactly as they appear in the transcript.
- If something is unclear or not mentioned, write "Unknown".
- Use short, simple language.

Expected response format:
A) JSON block (machine-readable) — first:
[
  {
    "project_overview": "<1–2 sentences>",
    "technologies": {
      "frontend": ["<tech or 'Unknown'>"],
      "backend": ["<tech or 'Unknown'>"],
      "data_storage": ["<tech or 'Unknown'>"],
      "other": ["<items like 'UX/UI', 'QA/testing', 'performance', or 'Unknown'>"]
    },
    "problems": [
      "<short description of each issue in the transcript>"
    ],
    "near_future_plans": [
      "<short description of planned work mentioned in the transcript>"
    ]
  }
]

B) Markdown summary (human-readable):
### Project Overview
- <short text>

### Technologies
- Frontend: <items>
- Backend: <items>
- Data storage: <items>
- Other: <items>

### Problems
- <bullet points>

### Near-Future Plans
- <bullet points>

C) Notes
- Briefly list any missing or unclear information.
"""


PROMT = f"""
Please analyze the attached meeting transcript file and create a general description of the project.
'{read_data_from_file("../file_input/project_transcript_file.txt")}'

Tasks:
1) What the project is about (in 1–2 sentences).
2) What technologies are used in the project for the frontend, backend, data storage, etc.
3) What problems the project has and what is planned to be implemented in the near future.

Output format (please follow exactly):

A) JSON:
[
  {{
    "project_overview": "TEXT",
    "technologies": {{
      "frontend": ["ITEMS OR 'Unknown'"],
      "backend": ["ITEMS OR 'Unknown'"],
      "data_storage": ["ITEMS OR 'Unknown'"],
      "other": ["ITEMS OR 'Unknown'"]
    }},
    "problems": [
      "ITEM 1",
      "ITEM 2"
    ],
    "near_future_plans": [
      "ITEM 1",
      "ITEM 2"
    ]
  }}
]

B) Markdown:
### Project Overview
- TEXT

### Technologies
- Frontend: ITEMS
- Backend: ITEMS
- Data storage: ITEMS
- Other: ITEMS

### Problems
- ITEM 1
- ITEM 2

### Near-Future Plans
- ITEM 1
- ITEM 2

C) Notes
- Briefly mention anything unclear or missing (write "Unknown" when needed).
"""


if __name__ == "__main__":
    result = generate_paragraph(system_prompt=SYSTEM_PROMPT, prompt=PROMT)
    write_response_content_to_txt(result, "../file_output/task_5d.txt")

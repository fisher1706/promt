from utils import generate_paragraph, write_response_content_to_txt, read_data_from_file


SYSTEM_PROMPT = """
You are an assistant. Read the attached meeting transcript file and do a simple, first-pass analysis.

Goal:
- Find every meeting participant.
- For each person, decide a potential specialization based only on what they say.
- If you are not sure, write "Unknown". Do not guess.

Specializations to use (pick one):
- "Frontend Engineer", "Backend Engineer", "Full‑stack Engineer", "Mobile Engineer",
- "Database Engineer/DBA", "DevOps/SRE", "QA/Testing Engineer", "Data/ML Engineer",
- "Product Manager", "Project Manager/Scrum Master", "UX/UI Designer",
- "Security Engineer", "Business Analyst", "Stakeholder/Customer", "Unknown".

Rules:
- Keep names exactly as in the transcript (do not change case or spelling).
- Use short, clear language.
- Do not add information that is not in the file.

Expected response format:
1) Start with a JSON code block:
   [
     { "name": "<Name from transcript>", "potential_specialization": "<One of the values above>" }
   ]

2) Then add a Markdown table with the same data:
   |  Name  |  Potential Specialization |
   |--------|---------------------------|
   | <Name> |       <Specialization>    |

3) End with a short section "Notes":
   - Mention any places where the data was unclear or missing.
"""


PROMT = f"""
Please analyze the attached meeting transcript file and do an initial analysis of the meetings:
'{read_data_from_file("../file_input/project_transcript_file.txt")}'

Tasks:
1) Make a list of all participants (use the exact names from the transcript).
2) Next to each name, write their potential specialization using this list:
   "Frontend Engineer", "Backend Engineer", "Full‑stack Engineer", "Mobile Engineer",
   "Database Engineer/DBA", "DevOps/SRE", "QA/Testing Engineer", "Data/ML Engineer",
   "Product Manager", "Project Manager/Scrum Master", "UX/UI Designer",
   "Security Engineer", "Business Analyst", "Stakeholder/Customer", "Unknown".
3) If you cannot decide the specialization from the transcript, write "Unknown".

Output format (please follow exactly):
A) JSON (one code block first):
[
  {{ "name": "NAME FROM TRANSCRIPT", "potential_specialization": "VALUE FROM LIST ABOVE" }}
]

B) Markdown table:
|          Name        | Potential Specialization |
|----------------------|--------------------------|
| NAME FROM TRANSCRIPT |   VALUE FROM LIST ABOVE  |

C) Notes:
- Briefly say where the data was unclear or missing.
"""


if __name__ == "__main__":
    result = generate_paragraph(system_prompt=SYSTEM_PROMPT, prompt=PROMT)
    write_response_content_to_txt(result, "../file_output/task_5a.txt")

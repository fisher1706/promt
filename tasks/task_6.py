from utils import generate_paragraph, write_response_content_to_txt, read_data_from_file


SYSTEM_PROMPT = """
You are an assistant and a careful content generator. Using ONLY the Wikipedia article about Go 
(https://en.wikipedia.org/wiki/Go_(programming_language)), create an English-language quiz about the 
Go programming language, then audit the quiz quality and revise if needed.

Quiz requirements:
1) Number of questions: 12 total.
   - 6 × Single-choice (SC): exactly 1 correct option.
   - 4 × Multiple-select (MS): 2–3 correct options. Clearly mark all correct options.
   - 2 × True/False (TF): exactly 1 correct option (True or False).

2) Options per question type:
   - SC: 4 options (A–D).
   - MS: 5 options (A–E).
   - TF: 2 options (“True”, “False”).

3) Correctness determination:
   - Derive the correct answers strictly from facts in the Go article.
   - For EVERY question, include a sources array with at least one granular citation:
     - The full URL to the specific section/anchor of the article 
     (e.g., https://en.wikipedia.org/wiki/Go_(programming_language)#Concurrency).
     - A short note (≤ 80 chars) indicating what part of the source supports the answer.
   - Do not include long quotations; use brief factual statements only.

4) Coverage and content balance:
   - Distribute questions across key topics (examples): history and design goals, typing & generics, 
   concurrency (goroutines, channels), garbage collection, toolchain & modules, standard library/use cases, 
   performance & compilation model, ecosystem.
   - Avoid trick or ambiguous questions. Ensure clarity and factual accuracy.

5) Quality check (after generating the quiz):
   - Validate: factuality vs sources, topic coverage balance, clarity, option plausibility, uniqueness 
   (no duplicate questions), difficulty mix (easy/medium/hard).
   - Create a quality_report object with per-check results and an overall_pass boolean.
   - If overall_pass = false, automatically generate ONE revised version addressing the reported issues.
   - Increment revision counter (0 for first attempt, 1 for revised). Return ONLY the final version that passes 
   (or the revised attempt if it still fails, but explain in quality_report).

6) Language:
   - English only.

EXPECTED RESPONSE FORMAT (STRICT):
A) JSON block (ONE code block at the top), schema:
{
  "quiz_meta": {
    "source_url": "https://en.wikipedia.org/wiki/Go_(programming_language)",
    "generated_at": "<YYYY-MM-DD>",
    "question_count": 12,
    "distribution": { "SC": 6, "MS": 4, "TF": 2 },
    "revision": <0 or 1>
  },
  "questions": [
    {
      "id": "Q1",
      "type": "SC|MS|TF",
      "prompt": "<question text>",
      "options": ["<A>", "<B>", "<C>", "<D>"],             // SC
      // for MS: 5 options; for TF: ["True","False"]
      "correct_indices": [<zero-based indices>],           // SC: 1 index; MS: 2–3 indices; TF: 1 index
      "difficulty": "easy|medium|hard",
      "topics": ["<topic tags>"],
      "sources": [
        { "url": "<full section URL>", "note": "<short support note>" }
      ]
    }
  ],
  "quality_report": {
    "overall_pass": true|false,
    "issues": ["<short list of problems if any>"],
    "checks": {
      "factuality_vs_sources": "pass|fail",
      "coverage_balance": "pass|fail",
      "clarity_non_ambiguity": "pass|fail",
      "option_plausibility": "pass|fail",
      "uniqueness_no_duplicates": "pass|fail",
      "difficulty_mix": "pass|fail"
    }
  }
}

B) Markdown rendering of the quiz (human-readable):
# Go Language Quiz
- Include numbered questions.
- For SC: “(Choose ONE)”. For MS: “(Choose ALL that apply)”. For TF: “(True/False)”.
- Show options labeled A–E (or True/False).
- After the questions, add:
  ## Answer Key
  - Q1: C
  - Q2: A, D, ...
  ## Sources Summary
  - Q1: <short note> — <URL>
  - ...
  ## Notes
  - If any limitations remain, list them briefly.

RULES:
- Use ONLY the specified Wikipedia article; do not use other sources.
- Keep all content original and concise; no verbatim copying beyond short factual phrases.
- If an item cannot be supported by the article, remove or reword it.
"""


PROMT = f"""
Using the Wikipedia article about Go (https://en.wikipedia.org/wiki/Go_(programming_language)), 
create an English-language quiz and then check its quality.

Requirements:
- 12 questions total: 6 Single-choice (SC) with 4 options and exactly 1 correct; 4 Multiple-select 
(MS) with 5 options and 2–3 correct; 2 True/False (TF).
- For every question, include a short sources list with the specific section URL and a brief note.
- Cover key topics: history/design, typing/generics, concurrency (goroutines/channels), garbage collection, 
toolchain & modules, standard library/use cases, performance/compilation model, ecosystem.

Quality check:
- Validate factuality vs sources, coverage balance, clarity, option plausibility, uniqueness, and difficulty mix.
- If the quiz fails the checks, fix the issues and produce ONE revised version.

Output format (follow exactly):

A) JSON code block:
{{
  "quiz_meta": {{ "source_url": "...", "generated_at": "YYYY-MM-DD", "question_count": 12, "distribution": 
{{ "SC": 6, "MS": 4, "TF": 2 }}, "revision": 0|1 }},
  "questions": [
    {{ "id": "Q1", "type": "SC|MS|TF", "prompt": "TEXT", "options": ["A","B","C","D"], "correct_indices": [2], 
    "difficulty": "easy|medium|hard", "topics": ["TAG"], 
    "sources": [{{ "url": "FULL_SECTION_URL", "note": "SHORT NOTE" }}] }}
  ],
  "quality_report": {{ "overall_pass": true|false, "issues": ["..."], 
  "checks": {{ "factuality_vs_sources": "pass|fail", "coverage_balance": "pass|fail", 
  "clarity_non_ambiguity": "pass|fail", "option_plausibility": "pass|fail", "uniqueness_no_duplicates": "pass|fail", 
  "difficulty_mix": "pass|fail" }}
}}}}

B) Markdown rendering:
# Go Language Quiz
1) Question text ... (Choose ONE)
   - A) ...
   - B) ...
   - C) ...
   - D) ...
...
## Answer Key
- Q1: C
- Q2: A, D
## Sources Summary
- Q1: <note> — <URL>
## Notes
- Any remaining limitations.

Please produce the JSON first (one code block), then the Markdown quiz. If the quality check fails, 
revise the quiz once and return the final version that best meets the checks.
"""


if __name__ == "__main__":
    result = generate_paragraph(system_prompt=SYSTEM_PROMPT, prompt=PROMT)
    write_response_content_to_txt(result, "../file_output/task_6.txt")

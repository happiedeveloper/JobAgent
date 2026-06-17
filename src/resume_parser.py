
from pypdf import PdfReader
from pathlib import Path
import json
import re

SKILLS = [
    "python",
    "fastapi",
    "docker",
    "kubernetes",
    "postgresql",
    "sql",
    "spark",
    "pyspark",
    "kafka",
    "hadoop",
    "nifi",
    "neo4j",
    "git",
    "terraform",
    "aws",
    "gcp",
    "airflow",
    "docker compose",
    "rest api",
    "langchain",
    "llama",
]

def extract_text(pdf_path):
    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text.lower() + "\n"

    return text


def extract_skills(text):

    found_skills = []

    for skill in SKILLS:

        pattern = rf"\b{re.escape(skill)}\b"

        if re.search(pattern, text):
            found_skills.append(skill)

    return sorted(list(set(found_skills)))


def save_skills(skills):

    Path("output").mkdir(exist_ok=True)

    output = {
        "skills": skills,
        "total_skills": len(skills)
    }

    with open("output/skills.json", "w") as f:
        json.dump(output, f, indent=4)

    return output


def main():

    resume_path = "resumes/master_resume.pdf"

    if not Path(resume_path).exists():
        print(f"Resume not found: {resume_path}")
        return

    text = extract_text(resume_path)

    skills = extract_skills(text)

    result = save_skills(skills)

    print("\nDetected Skills:\n")

    for skill in skills:
        print(f"✓ {skill}")

    print(f"\nTotal Skills Found: {result['total_skills']}")

    print("\nSaved:")
    print("output/skills.json")


if __name__ == "__main__":
    main()


from pathlib import Path
from pypdf import PdfReader
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
    "langchain",
    "llama",
    "ollama",
    "rest api",
    "microservices"
]


class ResumeParser:

    def __init__(self, resume_path="resumes/master_resume.pdf"):
        self.resume_path = Path(resume_path)

        Path("output").mkdir(
            parents=True,
            exist_ok=True
        )

    def extract_text(self):

        if not self.resume_path.exists():
            raise FileNotFoundError(
                f"Resume not found: {self.resume_path}"
            )

        reader = PdfReader(str(self.resume_path))

        text_parts = []

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text_parts.append(page_text)

        return "\n".join(text_parts).lower()

    def save_resume_text(self, text):

        with open(
            "output/resume_text.txt",
            "w",
            encoding="utf-8"
        ) as f:

            f.write(text)

    def extract_skills(self, text):

        found_skills = set()

        for skill in SKILLS:

            pattern = rf"\b{re.escape(skill)}\b"

            if re.search(pattern, text):
                found_skills.add(skill)

        return sorted(list(found_skills))

    def save_skills(self, skills):

        data = {
            "skills": skills,
            "total_skills": len(skills)
        }

        with open(
            "output/skills.json",
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                indent=4
            )

    def run(self):

        print("Reading resume...")

        text = self.extract_text()

        self.save_resume_text(text)

        skills = self.extract_skills(text)

        self.save_skills(skills)

        print("\nResume parsed successfully.\n")

        print("Detected Skills:\n")

        for skill in skills:
            print(f"✓ {skill}")

        print(
            f"\nTotal Skills Found: {len(skills)}"
        )

        print("\nGenerated Files:")

        print(
            "output/resume_text.txt"
        )

        print(
            "output/skills.json"
        )


if __name__ == "__main__":

    parser = ResumeParser()

    parser.run()

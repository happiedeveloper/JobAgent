
import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

model = SentenceTransformer(MODEL_NAME)

def load_skills():
    with open("output/skills.json") as f:
        data = json.load(f)

    return " ".join(data["skills"])

def score_job(job_description, skills_text):

    resume_embedding = model.encode([skills_text])

    job_embedding = model.encode([job_description])

    score = cosine_similarity(
        resume_embedding,
        job_embedding
    )[0][0]

    return round(score * 100, 2)

if __name__ == "__main__":

    skills = load_skills()

    sample_job = """
    Looking for a Python Backend Engineer with
    FastAPI, Docker, Kubernetes, PostgreSQL and Kafka.
    """

    score = score_job(sample_job, skills)

    print(f"Match Score: {score}%")

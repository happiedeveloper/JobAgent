
import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

print("Loading model...")

model = SentenceTransformer(MODEL_NAME)

def load_resume_text():

    with open(
        "output/resume_text.txt",
        "r",
        encoding="utf-8"
    ) as f:

        return f.read()

def calculate_match_score(
    resume_text,
    job_description
):

    resume_embedding = model.encode(
        [resume_text]
    )

    job_embedding = model.encode(
        [job_description]
    )

    similarity = cosine_similarity(
        resume_embedding,
        job_embedding
    )[0][0]

    return round(
        similarity * 100,
        2
    )

if __name__ == "__main__":

    resume_text = load_resume_text()

    sample_job = """
    Looking for a Backend Engineer with
    Python,
    FastAPI,
    Docker,
    Kubernetes,
    PostgreSQL,
    Kafka
    experience.

    Experience with cloud and
    distributed systems preferred.
    """

    score = calculate_match_score(
        resume_text,
        sample_job
    )

    print(
        f"\nMatch Score: {score}%"
    )

import os
from flask import Flask, render_template, request
from google.cloud import run_v2

app = Flask(__name__)

PROJECT_ID = os.environ.get("PROJECT_ID", "your-project-id")
REGION = os.environ.get("REGION", "us-central1")
JOB_NAME = os.environ.get("JOB_NAME", "prime-job")


def trigger_prime_job(number):
    client = run_v2.JobsClient()
    job_path = f"projects/{PROJECT_ID}/locations/{REGION}/jobs/{JOB_NAME}"

    request_obj = run_v2.RunJobRequest(
        name=job_path,
        overrides=run_v2.RunJobRequest.Overrides(
            container_overrides=[
                run_v2.RunJobRequest.Overrides.ContainerOverride(
                    env=[run_v2.EnvVar(name="NUMBER", value=str(number))]
                )
            ]
        ),
    )

    operation = client.run_job(request=request_obj)
    execution_name = operation.metadata.name.split("/")[-1]
    return execution_name


@app.route("/", methods=["GET", "POST"])
def home():
    execution_id = None
    error = None

    if request.method == "POST":
        number = int(request.form["number"])
        try:
            execution_id = trigger_prime_job(number)
        except Exception as e:
            error = str(e)

    return render_template("index.html", execution_id=execution_id, error=error)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

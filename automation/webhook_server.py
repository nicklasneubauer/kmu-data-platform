from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/webhook/import-sales")
def run_import_script():
    try:
        result = subprocess.run(["python", "db/import_data.py"], capture_output=True, text=True, check=True)
        return {"status": "success", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "error": e.stderr}

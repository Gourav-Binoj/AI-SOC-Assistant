from fastapi import FastAPI

app = FastAPI(
    title="AI SOC Assistant",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "AI SOC Assistant Backend is Running!"
    }
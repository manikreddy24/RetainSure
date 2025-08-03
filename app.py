from fastapi import FastAPI

app = FastAPI(
    title="User Management API",
    openapi_tags=[
        {"name": "users", "description": "User operations"},
        {"name": "auth", "description": "Authentication"}
    ]
)

@app.get("/")
def home():
    return {"message": "Hello World"}

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/save/")
async def save_code(data: dict):
    code_content = data.get("code")
    with open("saved_code.py", "w") as file:
        file.write(code_content)
    return {"message": "Code saved successfully"}


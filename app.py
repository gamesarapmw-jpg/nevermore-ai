from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {
        "status": "online",
        "name": "NeverMore AI"
    }

@app.post("/chat")
def chat(req: ChatRequest):
    msg = req.message.lower()

    if "سلام" in msg:
        answer = "سلام! حالت چطوره؟"
    elif "اسم" in msg:
        answer = "من NeverMore AI هستم."
    elif "ماینکرفت" in msg:
        answer = "ماینکرفت یکی از بازی‌های مورد علاقه منه!"
    else:
        answer = f"پیام شما دریافت شد: {req.message}"

    return {
        "response": answer
    }

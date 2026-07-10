from fastapi import FastAPI, HTTPException
from app.schemas import RequestData
from services.gpt_service import analyze_request

app = FastAPI()

@app.post("/webhook")
async def webhook(data: RequestData):
    try:
        result = analyze_request(data.text)
    except Exception as e:
        print (f"Ошибка при обращении к GPT: {e}")
        raise HTTPException(status_code=502, detail="Не удалось проанализировать заявку")
    
    return {
        "user_id": data.user_id,
        "text": data.text,
        "category": result.get("category", "прочее"),
    }



import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

def analyze_request(text: str) -> dict:
    response = client.chat.completions.create(
        model = "gpt-5.4-nano",
        messages = [
            {"role": "system", "content": "Ты классификатор заявок поддержки. Твоя задача определять категорию задачи из списка: покупка, поддержка, жалоба. Верни ответ в json с полями category (одна из категорий)."},
            {"role": "user", "content": text},
        ],
        response_format = {"type": "json_object"},
    )
    answer = response.choices[0].message.content
    return json.loads(answer)

if __name__ == "__main__":
    print(analyze_request("Здравсвуйте, провел оплату но со мной не связались"))

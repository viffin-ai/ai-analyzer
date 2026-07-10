# ai-analyzer

A small FastAPI service that receives customer requests via a webhook, classifies them with the OpenAI API (categories: purchase / support / complaint), and returns a structured result. Includes automated tests with pytest.

## Features

- **Webhook endpoint** (`POST /webhook`) for incoming requests
- **Input validation** via Pydantic schemas (invalid payloads are rejected automatically with a 422 response)
- **LLM classification** through the OpenAI API with structured JSON output
- **Error handling** with a clear response on upstream failures
- **Automated tests** (pytest), including a mocked OpenAI call so tests run fast and without spending tokens

## Tech stack

Python · FastAPI · Pydantic · OpenAI API · pytest

## Project structure

```
ai-analyzer/
├── app/
│   ├── main.py        # FastAPI app and the /webhook endpoint
│   └── schemas.py     # Pydantic request schema (validation)
├── services/
│   └── gpt_service.py # OpenAI call and request classification
├── tests/
│   └── test_webhook.py # automated tests (pytest)
├── .gitignore
└── requirements.txt
```

## Getting started

1. Clone the repository:
   ```
   git clone https://github.com/viffin-ai/ai-analyzer.git
   cd ai-analyzer
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # macOS / Linux
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your OpenAI key:
   ```
   OPENAI_API_KEY=your_key_here
   ```

5. Run the service:
   ```
   uvicorn app.main:app --reload
   ```

The API will be available at `http://127.0.0.1:8000`, with interactive docs at `http://127.0.0.1:8000/docs`.

## Example request

```
POST /webhook
Content-Type: application/json

{
  "text": "I paid for the order but no one contacted me",
  "user_id": 7
}
```

Example response:

```
{
  "user_id": 7,
  "text": "I paid for the order but no one contacted me",
  "category": "complaint"
}
```

## Running tests

```
pytest
```
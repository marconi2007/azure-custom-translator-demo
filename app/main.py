from fastapi import FastAPI
from app.translator import translate_text

app = FastAPI(
    title="Azure Custom Translator - Demo",
    description="Simulação de integração com Azure Custom Translator",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message": "API de Tradução Personalizada - Demo"}

@app.post("/translate")
def translate(text: str, to_language: str = "pt"):
    return translate_text(text, to_language)

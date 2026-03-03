def translate_text(text: str, to_language="pt"):
    return {
        "provider": "Azure Custom Translator (Simulado)",
        "category_id": "demo-category-id-123",
        "original_text": text,
        "translated_text": f"[{to_language}] {text} (tradução personalizada simulada)"
    }

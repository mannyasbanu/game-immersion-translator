from deep_translator import GoogleTranslator

def translate_text(text):
  try:
    # Translate Japanese to English
    english = GoogleTranslator(source='ja', target='en').translate(text)
    print(f"Translation: {english}")
    return english
  except Exception as e:
    print(f"Translation failed: {e}")
    return ""

from googletrans import Translator

def translate_text(text, src_language, dest_language):
    translator = Translator()
    translated = translator.translate(text, src=src_language, dest=dest_language)
    return translated.text

if __name__ == "__main__":
    # Example usage
    text_to_translate = "Hello, how are you?"
    source_language = "en"  # English
    destination_language = "hi"  # Spanish

    translated_text = translate_text(text_to_translate, source_language, destination_language)
    print(f"Original text: {text_to_translate}")
    print(f"Translated text: {translated_text}")

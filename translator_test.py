from deep_translator import GoogleTranslator
translated = GoogleTranslator(source='auto',target='ja').translate("Hello")

print(translated)
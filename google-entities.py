from google.cloud import language
from BasicSettings import *


def analyze_text_entities(text):
    client = language.LanguageServiceClient()
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT, language=lang)

    response = client.analyze_entities(document=document)

    for entity in response.entities:
        print("=" * 80)
        results = dict(
            name=entity.name,
            type=entity.type_.name,
            salience=f"{entity.salience:.1%}",
            wikipedia_url=entity.metadata.get("wikipedia_url", "-"),
            mid=entity.metadata.get("mid", "-"),
        )
        for k, v in results.items():
            print(f"{k:15}: {v}")

text = content
analyze_text_entities(text)
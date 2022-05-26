from google.cloud import language
from BasicSettings import *

def analyze_text_syntax(text):
    client = language.LanguageServiceClient()
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT, language=lang)

    response = client.analyze_syntax(document=document)

    fmts = "{:10}: {}"
    print(fmts.format("sentences", len(response.sentences)))
    print(fmts.format("tokens", len(response.tokens)))
    for token in response.tokens:
        print(fmts.format(token.part_of_speech.tag.name, token.text.content))

text = content
analyze_text_syntax(text)
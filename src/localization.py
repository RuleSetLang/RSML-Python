

translations = {}

def load_lang(lang: str):
    with open("localization/" + lang + ".txt", "r") as f:
        for entry in f.read().split("\n\n"):
            entry = entry.split("\n")
            key = entry[0]
            val = entry[1]
            translations[key] = val


def tr(key: str) -> str:
    return translations[key] if key in translations.keys() else key

load_lang("en")

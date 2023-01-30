from json import load, dump
from lang_consts import LANGUAGES, LANG_CONTENT

with open("./src/utils/lang/lang.json", 'r') as f:
    LANG: dict[str, str] = load(f)

def _editLang(new_lang: str) -> None:
    """Permet de modifier la langue du jeu

    Args:
        new_lang (str): La langue souhaitée
    """
    assert new_lang.upper() in LANGUAGES, f"{new_lang} n'est pas une langue valide"

    LANG["lang"] = new_lang

    with open("./src/utils/lang/lang.json", 'w') as d:
        dump(LANG, d)

def _getLang() -> str:
    """Permet d'obtenir la langue actuel du jeu

    Returns:
        str: La langue du jeu
    """
    return LANG["lang"]


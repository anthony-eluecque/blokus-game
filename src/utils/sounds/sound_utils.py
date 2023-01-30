from json import load, dump

with open("./src/utils/sounds/soundVolume.json", 'r') as f:
    SOUND_VOLUME: dict[str, float | int] = load(f)

# print(SOUND_VOLUME)
# print(list(SOUND_VOLUME.keys()))
# print(SOUND_VOLUME["music"])

def _editValue(sound: str, volume: int|float) -> None:
    """Permet de modifier le volume d'un son de manière à récupérer cette valeur modifiée dans tout le programme (passée dans un json)

    Args:
        sound (str): Le son dont il faut modifier le volume
        volume (int | float): Le volume qu'il faut attribuer au son
    """
    assert sound in list(SOUND_VOLUME.keys()), f"'{sound}' n'est pas une valeur dont le son peut être modifié"

    SOUND_VOLUME[sound] = volume

    with open("./src/utils/sounds/soundVolume.json", 'w') as d:
        dump(SOUND_VOLUME, d)

def _getValues() -> dict[str, float|int]:
    """Permet d'obtenir les sons et leur volume attribué 

    Returns:
        dict[str, float|int]: Dictionnaire des sons et leur volume 
                              ex: {"son" : volume}
    """ 
    return SOUND_VOLUME
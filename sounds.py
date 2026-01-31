from pygame import mixer

def load_sounds(keys):
    sounds = {}
    for k, filename in keys:
        sounds[k] = mixer.Sound(f"assets/sounds/{filename}")
    return sounds

import subprocess
from syslibrary import execute

class SoundLevel:

    def __init__(self, app: str) -> None:
        self._app: str = app

    def __repr__(self) -> str:
        return f"SoundLevel({self._app})"


if __name__ == "__main__":
    sound_level = SoundLevel("firefox")

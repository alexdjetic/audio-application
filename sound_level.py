import subprocess
from syslibrary import execute

class SoundLevel:
    def __init__(self, sink_input: int) -> None:
        self._sink_input: int = sink_input

    def __repr__(self) -> str:
        return f"SoundLevel({self._sink_input})"

    def set_volume(self, volume: int) -> None:
        command = f"pactl set-sink-input-volume {self._sink_input} {volume}%"
        stdout, stderr, returnee = execute(command)

        if returnee == 0:
            print(stdout)
        else:
            print(f"Error: {stderr}")


if __name__ == "__main__":
    sound_level = SoundLevel(1797)
    sound_level.set_volume(100)

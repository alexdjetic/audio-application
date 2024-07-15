import subprocess
import re
from typing import Optional


def execute(cmd: str) -> tuple:
    """
    Execute a shell command and capture its output and return code.

    Args:
        cmd (str): The shell command to execute.

    Returns:
        tuple: A tuple containing the stripped stdout, stderr, and return code.
               If an error occurs, returns empty strings for stdout and stderr
               and a return code of 1.

    Raises:
        FileNotFoundError: If the command executable is not found.
        subprocess.CalledProcessError: If the command returns a non-zero exit status.
        OSError: If an OS-level error occurs during command execution.
        Exception: For any other unexpected errors.
    """
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip(), result.stderr.strip(), result.returncode
    except FileNotFoundError as e:
        return '', f"Command not found: {str(e)}", 1
    except subprocess.CalledProcessError as e:
        return '', f"Command '{cmd}' failed with error: {str(e)}", e.returncode
    except OSError as e:
        return '', f"OS error occurred: {str(e)}", 1
    except Exception as e:
        return '', f"An unexpected error occurred: {str(e)}", 1


def check_filter_data(data: Optional[str]) -> str:
    """
    Check and filter data found in a regex match.

    Args:
        data (Optional[str]): Data to check and filter.

    Returns:
        str: The matched data if found, otherwise "NA".
    """
    if data is None:
        return "NA"

    return data.group(1) if data else "NA"


def get_app_info_linux(app_info: str) -> dict:
    """
    Extract sink input, application name, media name, and volume percent from `pactl list sink-inputs` output.

    Args:
        app_info (str): Information about an application from `pactl list sink-inputs`.

    Returns:
        dict: A dictionary containing sink input, application name, media name, and volume percent.
    """
    sink_input_pattern = re.compile(r'^Sink Input #(\d+)', re.MULTILINE)
    application_name_pattern = re.compile(r'^\s*application\.name = "(.*?)"', re.MULTILINE)
    media_name_pattern = re.compile(r'^\s*media\.name = "(.*?)"', re.MULTILINE)
    volume_pattern = re.compile(r'Volume:.*?(\d+)%')

    return {
        "sink_input": check_filter_data(sink_input_pattern.search(app_info)),
        "application_name": check_filter_data(application_name_pattern.search(app_info)),
        "media_name": check_filter_data(media_name_pattern.search(app_info)),
        "volume": check_filter_data(volume_pattern.search(app_info))
    }


def get_all_sound_app() -> dict:
    """
    Retrieve information about all sound applications from `pactl list sink-inputs`.

    Returns:
        dict: A dictionary where keys are sink input numbers and values are tuples
              containing application name, media name, and volume percent.
    """
    command: str = "pactl list sink-inputs"
    stdout, stderr, returnee = execute(command)
    data: dict = {}

    if returnee == 0 and stdout:
        apps: list = stdout.split("\n\n")

        for app in apps:
            tmp: dict = get_app_info_linux(app)
            data.setdefault(
                tmp.get("sink_input", "NA"),
                (
                    tmp.get("application_name", "NA"),
                    tmp.get("media_name", "NA"),
                    tmp.get("volume", "NA")
                )
            )

    return data


if __name__ == "__main__":
    print("###################################")
    print("##    test fonction execute:     ##")
    print("###################################\n")
    stdout, stderr, return_code = execute("ls")
    print(f"STDOUT: {stdout}")
    print(f"STDERR: {stderr}")
    print(f"Return Code: {return_code}")

    print("###################################")
    print("## test des application avec son ##")
    print("###################################\n")
    print(get_all_sound_app())

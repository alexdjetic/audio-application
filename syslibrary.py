import subprocess


def execute(cmd: str) -> tuple:
    try:
        process = subprocess.Popen(cmd.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return stdout.decode('utf-8'), stderr.decode('utf-8'), process.returncode
    except FileNotFoundError as e:
        return '', f"Command not found: {str(e)}", 1
    except subprocess.CalledProcessError as e:
        return '', f"Command '{cmd}' failed with error: {str(e)}", e.returncode
    except OSError as e:
        return '', f"OS error occurred: {str(e)}", 1
    except Exception as e:
        return '', f"An unexpected error occurred: {str(e)}", 1


if __name__ == "__main__":
    cmd = "ls -l"
    stdout, stderr, return_code = execute(cmd)
    print(f"STDOUT: {stdout}")
    print(f"STDERR: {stderr}")
    print(f"Return Code: {return_code}")

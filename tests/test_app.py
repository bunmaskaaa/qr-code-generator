import os, subprocess, sys, shutil, pathlib

def test_cli_generates_file():
    # clean old runs
    if os.path.exists("qr_codes"):
        shutil.rmtree("qr_codes")
    if os.path.exists("logs"):
        shutil.rmtree("logs")

    result = subprocess.run(
        [sys.executable, "main.py", "--url", "https://www.njit.edu"],
        capture_output=True, text=True, check=True
    )
    saved_line = [line for line in result.stdout.splitlines() if line.startswith("Saved:")][0]
    path = saved_line.split("Saved:",1)[1].strip()
    assert os.path.exists(path)
    assert pathlib.Path(path).suffix.lower() == ".png"

import os
import shutil
import subprocess
import sys

PATH_VS = r"C:\Users\tothr\AppData\Local\Programs\Microsoft VS Code\bin\code.cmd"
WORK_ROOT = os.environ['USERPROFILE']


def start_exam() -> None:
    exam_id = sys.argv[1]
    path_exam = os.path.join(WORK_ROOT, exam_id)
    shutil.rmtree(path_exam, ignore_errors=True)
    os.mkdir(path_exam)
    with open(os.path.join(path_exam, "solution.c"), "w"):
        pass

    with open(os.path.join(path_exam, "input.csv"), "w") as file:
        file.writelines("TODO")

    command = f"{PATH_VS} {os.path.join(path_exam)}"
    subprocess.run(command.split(" "), timeout=2)

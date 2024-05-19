import os
import shutil
import subprocess
import sys

PATH_VS = r"C:\Users\tothr\AppData\Local\Programs\Microsoft VS Code\bin\code.cmd"
WORK_ROOT = os.environ['USERPROFILE']
EXTENSIONS = [
    name
    for name in """
    ms-vscode.cmake-tools
    ms-vscode.cpptools
    ms-vscode.cpptools-extension-pack
    ms-vscode.cpptools-themes
    """.splitlines()
    if name
]


def finish_exam() -> None:
    exam_id = sys.argv[2]
    path_exam = os.path.join(WORK_ROOT, exam_id)
    shutil.rmtree(path_exam)


def start_exam() -> None:
    exam_id = sys.argv[2]
    path_exam = os.path.join(WORK_ROOT, exam_id)
    shutil.rmtree(path_exam, ignore_errors=True)
    os.mkdir(path_exam)
    with open(os.path.join(path_exam, "solution.c"), "w"):
        pass

    with open(os.path.join(path_exam, "input.csv"), "w") as file:
        file.writelines("TODO")

    command = f"{PATH_VS} --disable-extensions --reuse-window {os.path.join(path_exam)}"
    subprocess.run(command.split(" "), timeout=2)


def run() -> None:
    print(sys.argv[1])
    if sys.argv[1] == "start":
        start_exam()
    else:
        finish_exam()


if __name__ == '__main__':
    start_exam()

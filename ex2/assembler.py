import os
import re

def greater_than(x, y):
    x_n, x_i = re.findall(r"([a-zA-Z]+)(\d*)\.py", x)[0]
    y_n, y_i = re.findall(r"([a-zA-Z]+)(\d*)\.py", y)[0]
    if x_i != y_i:
        return x_i > y_i
    if x_n == "reducer" and y_n != "reducer":
        return True
    if x_n == "combiner" and y_n == "mapper":
        return True
    return False

def compare(x, y):
    if greater_than(x, y):
        return 1
    elif greater_than(y, x):
        return -1
    else:
        return 0

def get_content(full_name):
    with open(full_name) as fr:
        return fr.read()

first = True
with open("exc-mr.txt", 'w') as fw:
    for path, dirs, files in sorted(os.walk(".")):
        if first:
            first = False
            continue

        if '.git' in path or '.idea' in path:
            continue

        dir_name = os.path.basename(os.path.normpath(path))
        task_num = dir_name.split('Task')[1]

        fw.write("Task {0} code begin\n\n".format(task_num))
        python_files = filter(lambda x: ".py" in x, files)
        python_files = sorted(python_files, cmp=compare)
        for python_file in python_files:
            fw.write(python_file + " begin\n\n")
            fw.write(get_content(os.path.join(path, python_file)))
            fw.write("\n" + python_file + " end\n\n\n\n\n\n\n")

        fw.write("Command.sh begin\n\n")
        fw.write(get_content(os.path.join(path, "command.sh")))
        fw.write("\nCommand.sh end\n\n\n\n\n")

        fw.write("\nTask {0} code end\n\n\n\n\n\n".format(task_num))

        fw.write("Task {0} results begin\n\n".format(task_num))
        fw.write(get_content(os.path.join(path, "result.txt")))
        fw.write("\nTask {0} results end\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n".format(task_num))





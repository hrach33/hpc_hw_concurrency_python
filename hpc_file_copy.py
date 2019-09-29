
# coding: utf-8




import os
import shutil




from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import sys


def execTask(source, destination):
    if not os.path.exists(destination):
        os.makedirs(destination)

    files = os.listdir(source)
    [shutil.copy(os.path.join(source, f), os.path.join(destination, f)) for f in files]




def execTaskWithThreads(source, destination):
    if not os.path.exists(destination):
        os.makedirs(destination)
    with ThreadPoolExecutor(max_workers=10) as e:
        files = os.listdir(source)
        [e.submit(shutil.copy, os.path.join(source, f), os.path.join(destination, f)) for f in files]




def execTaskWithProcesses(source, destination):
    if not os.path.exists(destination):
        os.makedirs(destination)
    with ProcessPoolExecutor(max_workers=10) as e:
        files = os.listdir(source)
        [e.submit(shutil.copy, os.path.join(source, f), os.path.join(destination, f)) for f in files]


def generateFiles():
    for i in range(10):
        command = "dd if=/dev/zero of=dir1/filename" + str(i) + ".txt count=1024000 bs=1024"
        os.system(command)


def main():
    arguments = sys.argv[1:]
    execTask(arguments[0], arguments[1])
    # execTaskWithThreads(arguments[0], arguments[1])
    # execTaskWithProcesses(arguments[0], arguments[1])




if __name__ == '__main__':
    main()


import os


def createDirIfNotExist(file_path):
    file_dir = os.path.split(file_path)[0]
    if not os.path.isdir(file_dir):
        os.makedirs(file_dir)


def fileExist(file_path):
    if os.path.isfile(file_path):
        return True
    return False

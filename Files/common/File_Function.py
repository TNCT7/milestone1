from .Utils.Find import find_in

def file_read (file_name):
    with open(file_name, "r") as file_Questions:
        return file_Questions.read()

def file_write(file_name,content):
    with open(file_name, "w") as File_Write:
        File_Write.write(content)

print(__name__)

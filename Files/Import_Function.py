"""
import File_Function

File_Function.file_write("Readable.txt","Amruta")

print(File_Function.file_read("Readable.txt"))
"""

from common.File_Function import file_write,file_read
from common.Utils.Find import find_in

list_data = ['Tejas','Amruta','Rudransh']

file_write("Readable.txt","Amruta Ankola")
print(file_read("Readable.txt"))
print(find_in(list_data,"Amruta"))

print(__name__)
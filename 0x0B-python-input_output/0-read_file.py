#!/usr/bin/python3
def read_file(filename=""):
    with open(filename , "r" , encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")

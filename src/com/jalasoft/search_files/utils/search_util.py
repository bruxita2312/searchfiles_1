from datetime import date

from os import path


def size_converter_to_bytes(size, type):
    """Function receives a file size with its measure type and converts it to bytes"""
    if type=="tb":
        return int(size*1024*1024*1024*1024)
    elif type=="gb":
        return int(size * 1024 * 1024 * 1024)
    elif type=="mb":
        return int(size * 1024 * 1024)
    elif type=="kb":
        return int(size * 1024)
    else:
        return int(size)

def size_converter(size, type):
    """Function receives a file size with its measure type and converts it to bytes"""
    if type=="tb":
        return int((((size/1024)/1024)/1024)/1024)
    elif type=="gb":
        return int(((size/1024)/1024)/1024)
    elif type=="mb":
        return int((size/1024)/1024)
    elif type=="kb":
        return int(size/1024)
    else:
        return int(size)

def timestamp_to_date(ctime):
    """Function receives a timestamp and returns a formated date"""
    return date.fromtimestamp(ctime).strftime('%Y-%m-%d %H:%M:%S')

def get_extension(apath):
    if path.isfile(apath):
        extension = path.splitext(apath)[1]
    return extension

def get_name(apath):
    if path.isfile(apath):
        archivo = path.splitext(apath)[0]
    return archivo


converted = size_converter(15,"mb")
#print (converted)
converted = size_converter_to_bytes(15728640,"mb")
#3print (converted)
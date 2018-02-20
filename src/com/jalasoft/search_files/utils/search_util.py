from datetime import date, datetime, time
from src.com.jalasoft.search_files.utils.search_logging import logger

from os import path


def size_converter_to_bytes(size, type):
    """Function receives a file size with its measure type and converts it to bytes"""
    if type == "tb":
        return int(size * 1024 * 1024 * 1024 * 1024)
    elif type == "gb":
        return int(size * 1024 * 1024 * 1024)
    elif type == "mb":
        return int(size * 1024 * 1024)
    elif type == "kb":
        return int(size * 1024)
    else:
        return int(size)


def size_converter(size, type):
    """Function receives a file size with its measure type and converts it to bytes"""
    if type == "tb":
        return int((((size / 1024) / 1024) / 1024) / 1024)
    elif type == "gb":
        return int(((size / 1024) / 1024) / 1024)
    elif type == "mb":
        return int((size / 1024) / 1024)
    elif type == "kb":
        return int(size / 1024)
    else:
        return int(size)


def timestamp_to_date(ctime):
    """Function receives a timestamp and returns a formated date"""
    logger.info("SEARCH UTILS ::: TIMESTAMP ::: %d " % ctime)
    return date.fromtimestamp(ctime).strftime('%Y-%m-%d')


def date_to_timestamp(cdate):
    """Function receives a format date and returns a timestamp"""
    return time.time.mktime(datetime.datetime.strptime(cdate, "%Y-%m-%d").timetuple())


def get_datetime(cdate):
    logger.info("SEARCH UTILS ::: DATETIME ::: %s " % cdate)
    formato_fecha = "%Y-%m-%d"
    return datetime.strptime(cdate, formato_fecha)


def get_extension(apath):
    """Function that returns only the extension of a file"""
    extension = ""
    if path.isfile(apath):
        extension = path.splitext(apath)[1]
    return extension


def get_filename(file, type):
    """Function that returns only the name without the extension of a file"""
    new_name = ""
    new_name = file.replace(type, "")
    return new_name

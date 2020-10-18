class MyException(Exception):
    status_code = 500


class ConfigException(MyException):
    """
    Raise when there ies configuration exception
    """


class InvalidFilePath(MyException):
    """
    Raise when there file path is invalid
    """
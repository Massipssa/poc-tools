class MyException(Exception):
    status_code = 500


class ConfigException(MyException):
    """
    Raise when there ies configuration exception
    """
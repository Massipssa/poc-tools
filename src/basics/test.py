from datetime import datetime

if __name__ == '__main__':
    print(bool(0))
    print(sum(bool(x) for x in [0, 0]))

    test = "2023-08-05T14:25:00.627547Z"
    print(datetime.strptime(test[:-8], "%Y-%m-%dT%H:%M:%S").timestamp())

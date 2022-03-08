class Malware_down:

    def __init__(self):
        self.ii = 100000

    def spam(self):
        spam = []

        for i in range(0, self.ii):
            spam.append(i)

        return print(spam)


if __name__ == '__main__':
    s = Malware_down()
    Malware_down.spam(s)
class Malware_down:

    def __init__(self):
        self.ii = 40

    def spam(self):
        spam = []
        for i in range(0, self.ii):
            spam.append(i)
        return spam


def main():
    s = Malware_down()
    x = Malware_down.spam(s)
    return x


if __name__ == '__main__':
    main()

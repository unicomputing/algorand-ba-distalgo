from termcolor import colored


def printable_votes(votes_dict: dict):
    if not len(votes_dict):
        return ''

    printable = list()
    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    n_c = len(colors)
    i = 0
    for hval, count in votes_dict.items():
        printable += [colored('{}'.format(hval[:10]), color=colors[i], attrs=['bold']) +
                      colored(' : {}'.format(count), color='white', attrs=['bold'])]
        i = (i + 1) % n_c
    string = '\n'.join(printable)
    return string


def WarningColor(string):
    if not len(string):
        return string

    return colored(string, color='red', attrs=['bold'])


def InfoColor(string):
    if not len(string):
        return string

    return colored(string, color='green', attrs=['bold'])


if __name__ == '__main__':

    A = {'ABCDEFGH': 1, 'IJKLMNOP': 2, 'QRSTUVWX': 3, 'YZABCDEF': 4}
    print(printable_votes(A))

    print(printable_votes({}))

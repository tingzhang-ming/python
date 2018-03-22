from observed import HanFeiZi
from observer import Lisi, Wangsi


def main():
    lisi = Lisi()
    ws = Wangsi()

    hanfeizi = HanFeiZi()
    hanfeizi.add_observer(lisi)
    hanfeizi.add_observer(ws)

    hanfeizi.have_breakfast()
    hanfeizi.have_fun()


if __name__ == '__main__':
    main()

# i have_breakfast
# li si observe han fei zi
# bao gao:  han fei zi have_breakfast
# Wang si observe han fei zi
# Wo kan jian:  han fei zi have_breakfast
# i have fun
# li si observe han fei zi
# bao gao:  han fei zi have fun
# Wang si observe han fei zi
# Wo kan jian:  han fei zi have fun
from proxy import PlayerProxy


def main():
    p = PlayerProxy("mhc")
    p.login("mhcuser", "mhc.123")
    p.kill_boss()
    p.upgrade()


if __name__ == '__main__':
    main()

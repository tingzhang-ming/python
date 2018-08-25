from gamePlayer.player import Player


def main():
    p = Player("mhc")
    p.login("mhcuser", "mhc.123")
    p.kill_boss()
    p.upgrade()
    p.get_proxy()
    p.login("mhcuser", "mhc.123")
    p.kill_boss()
    p.upgrade()

# Please set proxy
# Please set proxy
# Please set proxy
# login user: mhcuser, password: mhc.123
# mhc kill boss
# mhc upgrade


if __name__ == '__main__':
    main()

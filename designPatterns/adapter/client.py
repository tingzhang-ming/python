from userInfo import UserInfo
from outerUserInfo import OuterUserInfo


def main():
    ui = UserInfo()
    ui.get_name()
    ui.get_number()

    ui = OuterUserInfo()
    ui.get_name()
    ui.get_number()


if __name__ == '__main__':
    main()

# name is
# number is
# outer get name
# outer get number

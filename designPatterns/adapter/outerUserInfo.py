from outerUser import OuterUser
from userInfo import AbstractUserInfo


class OuterUserInfo(OuterUser, AbstractUserInfo):

    def __init__(self):
        super(OuterUserInfo, self).__init__()
        self._base_info = super(OuterUserInfo, self).get_user_base_info()
        self._home_info = super(OuterUserInfo, self).get_user_home_info()

    def get_name(self):
        print "outer get name"
        return self._base_info["name"]

    def get_number(self):
        print "outer get number"
        return self._home_info["number"]


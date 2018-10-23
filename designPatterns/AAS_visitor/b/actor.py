# encoding: utf-8


class AbsActor(object):

    def act(self, role):
        print "演员可以扮演任何角色"


class YoungActor(AbsActor):

    def act(self, role):
        print "最喜欢功夫角色"


class OldActor(AbsActor):
    def act(self, role):
        print "不喜欢功夫角色"
# encoding: utf-8


class AdvTemplate(object):

    def __init__(self):
        self._adv_subject = "抽奖活动"
        self._adv_context = "抽奖活动详情"

    def get_adv_subject(self):
        return self._adv_subject

    def get_adv_context(self):
        return self._adv_context

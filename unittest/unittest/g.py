import unittest


def gen_drds_area_ids(inst_ids, area_ids):
    return [area_ids[index % 2] for index in xrange(len(inst_ids))]


def gen_split_inst_ids(inst_ids, area_ids):
    drds_area_ids = gen_drds_area_ids(inst_ids, area_ids)
    length = len(inst_ids)
    index = length / 2 if length > 1 else 1
    return inst_ids[:index], inst_ids[index:], drds_area_ids[:index], drds_area_ids[index:]


class Test(unittest.TestCase):

    def test_gen_split_inst_ids(self):
        area_ids = ["a1", "a2"]
        inst_ids = ["i1"]
        self.assertEqual((["i1"], [], ["a1"], []), gen_split_inst_ids(inst_ids, area_ids))
        inst_ids = ["i1", "i2"]
        self.assertEqual((["i1"], ["i2"], ["a1"], ["a2"]), gen_split_inst_ids(inst_ids, area_ids))
        inst_ids = ["i1", "i2", "i3"]
        self.assertEqual((["i1"], ["i2", "i3"], ["a1"], ["a2", "a1"]), gen_split_inst_ids(inst_ids, area_ids))
        inst_ids = ["i1", "i2", "i3", "i4"]
        self.assertEqual((["i1", "i2"], ["i3", "i4"], ["a1", "a2"], ["a1", "a2"]), gen_split_inst_ids(inst_ids, area_ids))
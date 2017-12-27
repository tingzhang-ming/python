

def get_cmd(target_module, target_cmd):
    try:
        res = vars(target_module)[target_cmd]
    except KeyError:
        return None
    return res
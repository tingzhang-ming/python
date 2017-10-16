from ansible.plugins import cache_loader, action_loader
from ansible import constants as C

def t1():
    print cache_loader.find_plugin("pickle")

    pickle_cache = cache_loader.get("pickle")

    # pickle_cache.set("mhc", "value")
    print pickle_cache.get("mhc")

def t2():
    print action_loader._get_paths()

if __name__ == '__main__':
    t2()
from glom import glom, T


def t1():
    target = {'galaxy': {'system': {'planet': 'jupiter'}}}
    spec = 'galaxy.system.planet'
    print(glom(target, spec))
    try:
        spec = 'galaxy.system.planet2'
        print(glom(target, spec))
    except KeyError as e:
        print(e)
    spec = 'galaxy.system.planet2'
    print(glom(target, spec, default=None))

    """
    jupiter
could not access 'planet2', index 2 in path Path('galaxy', 'system', 'planet2'), got error: KeyError('planet2',)
None
    """


def t2():
    target = {'system': {'planets': [{'name': 'earth'}, {'name': 'jupiter'}]}}
    print(glom(target, ('system.planets', ['name'])))
    # ['earth', 'jupiter']


def t3():
    target = {'system': {'planets': [{'name': 'earth', 'moons': 1},
                                     {'name': 'jupiter', 'moons': 69}]}}

    spec = {'names': ('system.planets', ['name']),
            'moons': ('system.planets', ['moons'])}

    print(glom(target, spec))


def t4():
    target = {'system': {'planets': [{'name': 'earth', 'moons': 1},
                                     {'name': 'jupiter', 'moons': 69}]}}

    print(glom(target, {'moon_count': ('system.planets', ['moons'], sum)}))
    spec = T['system']['planets'][-1].values()
    print(glom(target, spec))
# {'moon_count': 70}
# dict_values(['jupiter', 69])


if __name__ == '__main__':
    t4()

"""
$ pip install glom
$ curl -s https://api.github.com/repos/mahmoud/glom/events \
  | glom '[{"type": "type", "date": "created_at", "user": "actor.login"}]'
Which gets us:

[
  {
    "date": "2018-05-09T03:39:44Z",
    "type": "WatchEvent",
    "user": "asapzacy"
  },
  {
    "date": "2018-05-08T22:51:46Z",
    "type": "WatchEvent",
    "user": "CameronCairns"
  },
  {
    "date": "2018-05-08T03:27:27Z",
    "type": "PushEvent",
    "user": "mahmoud"
  },
  {
    "date": "2018-05-08T03:27:27Z",
    "type": "PullRequestEvent",
    "user": "mahmoud"
  }
...
]
"""

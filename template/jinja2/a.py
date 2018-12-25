import jinja2


def build_jinja_environment():
    env = jinja2.Environment(
        autoescape=True,
        loader=jinja2.ChoiceLoader([
            jinja2.FileSystemLoader("D:\github\python\\template\jinja2\\templates")
            # jinja2.PackageLoader("trove", "templates")
        ]))
    # Add some basic operation not built-in.
    env.globals['max'] = max
    env.globals['min'] = min
    return env


env = build_jinja_environment()


def t1():
    template = env.get_template("a.template")
    print template.render(filenames=["name1", "name2"])
# file name is name1
# file name is name2


def t2():
    template = env.get_template("a.template")
    path = "/etc/a/a.txt"
    with open(path, 'w') as f:
        template.stream(filenames=["name1", "name2"]).dump(f)


if __name__ == '__main__':
    t2()

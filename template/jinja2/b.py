# encoding: utf-8
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


class Myobject(object):

    def something(self):
        return "something"


def t1():
    env.filters["max2"] = max
    template = env.get_template("b.template")

    mydict = {"key": "value"}
    mylist = ["111", "222", "333", "4444"]
    myobject = Myobject()

    print template.render(mydict=mydict, mylist=mylist, myobject=myobject, a=1, b=2)
# <p>this is a dicectory:value </p>
# <p>this is a list:4444 </p>
# <p>this is a object:something </p>
# 2
# 2
# 1
# 2

# max2 用with 不行


if __name__ == '__main__':
    t1()

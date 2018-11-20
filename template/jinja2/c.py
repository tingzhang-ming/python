import jinja2
from collections import namedtuple


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
    template = env.get_template("c.template")
    print template.render()


class People(object):

    def __init__(self):
        self.safe = False
        self.dead = False


def t2():
    template = env.get_template("d.template")
    daxin = People()
    daxin.safe = True
    print template.render(daxin=daxin)
    daxin.safe = False
    daxin.dead = True
    print template.render(daxin=daxin)
#
# daxin is safe.
# daxin is dead


def t3():
    User = namedtuple('User', ['username'])
    users = []
    for i in range(3):
        users.append(User(username="user-{}".format(str(i))))
    my_dict = dict(
        aa="11",
        bb="22"
    )
    template = env.get_template("e.template")
    print template.render(users=users, my_dict=my_dict)
# <ul>
#
# <li>User-0</li>
#
# <li>User-1</li>
#
# <li>User-2</li>
#
# </ul>
#
# <dl>
#
# <dt>aa</dt>
# <dd>11</dd>
#
# <dt>bb</dt>
# <dd>22</dd>
#
# </dl>


def t4():
    template = env.get_template("f.template")
    print template.render()
# <p>
#
#  <input type='text' name="daxin" value="18" >
#
#  </p>
# <p>
#
#  <input type='text' name="daxin" value="20" >
#
#  </p>


def t5():
    template = env.get_template("g.template")
    print template.render()


def t6():
    template = env.get_template("h.template")
    print template.render()

# < !DOCTYPE
# html >
# < html
# lang = "en" >
# < head >
#
# < link
# rel = "stylesheet"
# href = "style.css" / >
# < title > Dachenzi - My
# Webpage < / title >
#
# < style
# type = 'text/css' >
# .important
# {color:  # FFFFFF }
# < / style >
#
#     < / head >
#         < body >
#         < div
# id = "content" > < / div >
#                      < div
# id = "footer" >
#
#      < script > This is javascript
# code < / script >
#
#          < / div >
#              < / body >
#                  < / html >


if __name__ == '__main__':
    t6()


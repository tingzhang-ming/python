from invoker import Invoker
from command.commands import Command1, Command2


def main():
    xiao3 = Invoker()
    xiao3.set_command(Command1())
    xiao3.action()
    xiao3.set_command(Command2())
    xiao3.action()

# start action--------------
# find requirement group
# find code group
# add an requirement
# add an function
# change requirement plan
# change code plan
# start action--------------
# find requirement group
# find code group
# delete an requirement
# delete an function
# change requirement plan
# change code plan

if __name__ == '__main__':
    main()



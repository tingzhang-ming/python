from office import ModenPostOffice


def main():
    o = ModenPostOffice()
    o.send_letter("hello jack", "beijing")


if __name__ == '__main__':
    main()
# write: hello jack
# fill address: beijing
# send letter

from director import Director


def main():
    d = Director()

    a = d.get_a_benz_model()
    a.run()

    b = d.get_b_benz_model()
    b.run()

    c = d.get_a_bmw_model()
    c.run()


if __name__ == '__main__':
    main()

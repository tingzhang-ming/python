import clame

INBUFSIZE = 4096

if __name__ == '__main__':
    encoder = clame.Encoder('test.mp3')
    input = file('test.raw', 'rb')
    data = input.read(INBUFSIZE)

    while data != '':
        encoder.encode(data)
        data = input.read(INBUFSIZE)
    input.close()
    encoder.close()

import pylame

if __name__ == '__main__':
    inPath = './test.raw'
    outPath = './test.mp3'
    pylame.encode(inPath, outPath)



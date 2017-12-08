#!/usr/bin/python
import sys
import json


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print sys.argv[1]
        with open(sys.argv[1], 'rb') as f:
            try:
                data_parse = json.load(f)
            except:
                print("This is not json file.")
                sys.exit(1)
        with open(sys.argv[1], 'w') as f:
            json.dump(data_parse, f, indent=2)
            print "success"

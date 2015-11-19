import json
import sys

if len(sys.argv) > 2:
    d = json.loads(open(sys.argv[2]).read())
    f = open(sys.argv[1]).read()
    for l in f.strip().split("\n"):
        if len(l) == 0 or l[0] == "#":
            continue
        s, t = tuple(l.split())
        print "{} {}".format(d[s], d[t]) 
else:
    print "Need to specify the source and the mapping file"

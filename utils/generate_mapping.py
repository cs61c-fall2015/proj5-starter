import json
import sys

if len(sys.argv) > 1:
    f = open(sys.argv[1]).read()
    d = {}
    i = 0
    for l in f.strip().split("\n"):
        if len(l) == 0 or l[0] == "#":
            continue
        s, t = tuple(l.split())
        if s not in d:
            d[s] = i
            i += 1
        if t not in d:
            d[t] = i
            i += 1
    print json.dumps(d)
else:
    print "Need to specify input file"

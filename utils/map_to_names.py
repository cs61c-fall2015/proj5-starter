import json
import sys

if len(sys.argv) > 2:
    inv_d = json.loads(open(sys.argv[2]).read())
    d = {}
    for (k, v) in inv_d.iteritems():
        d[v] = k 
    f = open(sys.argv[1]).read()
    for l in f.strip().split("\n"):
        s, t = tuple(l.split())
        print "{} {}".format(d[int(s)], t) 
else:
    print "Need to specify the source and the mapping file"


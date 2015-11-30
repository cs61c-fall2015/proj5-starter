import sys
import traceback

from pyspark import SparkContext
from pagerank.simple_page_rank import SimplePageRank
from pagerank.backedges_page_rank import BackedgesPageRank
from time import time

if __name__ == "__main__":
    if len(sys.argv) > 2:
        if sys.argv[1] == "b":
            method = BackedgesPageRank
        elif sys.argv[1] == "s":
            method = SimplePageRank
        else:
            print >> sys.stderr, "Invalid method specified. Must be either 'b' or 's'"
            sys.exit(0)
        num_iters = 1
        if len(sys.argv) > 3:
            try:
                num_iters = int(sys.argv[3])
            except:
                pass
        sc = SparkContext()
        try:
            input_rdd = sc.textFile(sys.argv[2])
            input_rdd = input_rdd.repartition(int(sys.argv[4]))
        except:
            print >> sys.stderr, "Unable to load file"
            sys.exit(0)
        try:
            s = time()
            output = method(input_rdd).compute_pagerank(num_iters)
        except:
            print >> sys.stderr, "Something went wrong"
            traceback.print_exc()
            sys.exit(0)
        print "Weight of five nodes:"
        for (node, weight) in output.top(5):
            print "{0} {1}".format(node, weight)
        e = time()
        print 'Time elapsed: %.2f min' % ((e - s) / 60.0)
        print ''
    else:
        print >> sys.stderr, "Not enough arguments specified. Must specify the method and input file."
        sys.exit(0)

import sys
import traceback

from utils.test_utils import FakeRDD
from pagerank.simple_page_rank import SimplePageRank
from pagerank.backedges_page_rank import BackedgesPageRank

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
        try:
            input_rdd = FakeRDD(open(sys.argv[2]).read().strip().split("\n"))
        except:
            print >> sys.stderr, "Unable to load file"
            sys.exit(0)
        try:
            output = method(input_rdd).compute_pagerank(num_iters)
        except:
            print >> sys.stderr, "Something went wrong"
            traceback.print_exc()
            sys.exit(0)
        for (node, weight) in output.take(100):
            print "{} {}".format(node, weight)
    else:
        print >> sys.stderr, "Not enough arguments specified. Must specify the method and input file."
        sys.exit(0)


import subprocess

def check(test_input, method, num_iters):
    with open("test/{}_{}_{}".format(test_input, method, num_iters), "r") as ref:
        cmd = ["python", "run_mock_pagerank.py", method, "data/" + test_input, str(num_iters)]
        output = subprocess.check_output(cmd)
        d = {}
        passed = True
        m = "SimplePageRank" if method == "s" else "BackedgesPageRank"
        for l in output.strip().split("\n"):
            try:
                n, w = tuple(l.split())
                d[n] = float(w)
            except:
                print "Error parsing output on {} on input {} for {} iterations.".format(m, test_input, num_iters)
                return
        for l in ref.read().strip().split("\n"):
            n, w = tuple(l.split())
            if n not in d:
                print "Missing entry for node {} on {} on input {} for {} iterations.".format(n, m, test_input, num_iters)
                return
            if abs(d[n] - float(w)) > 0.01:
                print "Wrong weight for node {} {} on input {} for {} iterations failed.".format(n, m, test_input, num_iters)
                return
        print "{} on input {} for {} iterations passed.".format(m, test_input, num_iters)
                         
for method in ["s", "b"]:
    for test_input in ["simple1", "simple2", "simple3"]:
        for num_iters in [1, 20]:
            check(test_input, method, num_iters)

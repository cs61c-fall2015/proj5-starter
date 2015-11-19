class FakeRDD(object):

    def __init__(self, collection):
        self.collection = list(collection)

    def filter(self, f):
        return FakeRDD(filter(f, self.collection))

    def count(self):
        return len(self.collection)

    def map(self, f):
        return FakeRDD(map(f, self.collection))

    def flatMap(self, f):
        return FakeRDD(sum(map(f, self.collection), []))

    def groupByKey(self):
        d = {}
        for (k, v) in self.collection:
            if k not in d:
                d[k] = [v]
            else:
                d[k].append(v)
        return FakeRDD(d.items())

    def sortByKey(self, ascending = True):
        return FakeRDD(sorted(self.collection, key = lambda (k, v): k, reverse = not ascending))

    def collect(self):
        return self.collection

    def take(self, n):
        return self.collection[:n]

    def reduceByKey(self, f):
        return FakeRDD([(k, reduce(f, v)) for (k, v) in self.groupByKey().collect()])

repartition_count=500

mkdir results
touch results/output_5
echo "Simple PageRank, Facebook Dataset" >> results/output_5
~/spark/bin/spark-submit run_pagerank.py s /user/root/facebook 20 $repartition_count >> results/output_5
echo "Backedges PageRank, Facebook Dataset" >> results/output_5
~/spark/bin/spark-submit run_pagerank.py b /user/root/facebook 20 $repartition_count >> results/output_5
echo "Simple PageRank, Enron Dataset" >> results/output_5
~/spark/bin/spark-submit run_pagerank.py s /user/root/enron 20 $repartition_count >> results/output_5
echo "Backedges PageRank, Enron Dataset" >> results/output_5
~/spark/bin/spark-submit run_pagerank.py b /user/root/enron 20 $repartition_count >> results/output_5

cd ~

echo "Downloading Datasets"
curl -O https://snap.stanford.edu/data/facebook_combined.txt.gz
curl -O https://snap.stanford.edu/data/email-Enron.txt.gz

echo "Unzipping datasets"
gzip -d facebook_combined.txt.gz
gzip -d email-Enron.txt.gz

echo "Cleaning up Enron dataset"
echo "$(tail -n +5 email-Enron.txt )" > email-Enron.txt

echo "Puting datasets into HDFS"
~/ephemeral-hdfs/bin/hadoop fs -put facebook_combined.txt facebook
rm -rf facebook_combined.txt
~/ephemeral-hdfs/bin/hadoop fs -put email-Enron.txt enron
rm -rf email-Enron.txt
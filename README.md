# ClusterCount
# Language: Python
# Input: TXT
# Output: none (screen, number of clusters)
# Tested with: PluMA 1.0, Python 3.6

PluMA plugin that takes a CSV file of clusters as input
and outputs the number of clusters that are at least a certain
number of nodes (the 'threshold').

Each of these are specified in an input TXT file of tab-delimited
keyword, value pairs - with keywords "inputfile" and "threshold".

Clusters are assumed to be delineated by "","x".

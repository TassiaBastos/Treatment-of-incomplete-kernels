import sys
from typing import List
from math import sqrt

# input
F1_score = sys.argv[1]
# RMSE = sys.argv[1]
# Pearson_correlation = sys.argv[1]
# output
analysis_F1_score_deleted_files = sys.argv[2]
# analysis_RMSE_deleted_files = sys.argv[2]
# analysis_Pearson_correlation_deleted_files = sys.argv[2]

with open(F1_score) as f:
    lines = f.readlines()
    f.close()
    mean = 0
    for line in lines:
        number = float(line)
        mean = mean + number

    mean = mean / len(lines)

with open(F1_score) as f:
    lines = f.readlines()
    f.close()
    sum = 0
    for line in lines:
        x = float(line)
        sum = sum + (x-mean)
    power = (sum) ** 2
    variance = power / len(lines)
    stddev = variance ** 0.5

my_list = [mean, stddev]

with open(analysis_F1_score_deleted_files, 'w') as output:
    for item in my_list:
        output.write("%s\n" % item)

# Por o seguinte código na linha de comando:
        # python analysis.py F1_score.txt analysis_F1_score_deleted_files.txt
# Por o seguinte código na linha de comando:
        # python analysis.py RMSE.txt analysis_RMSE_deleted_files.txt
# Por o seguinte código na linha de comando:
        # python analysis.py Pearson_correlation.txt analysis_Pearson_correlation_deleted_files.txt
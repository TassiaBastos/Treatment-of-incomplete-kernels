import sys
from typing import List
from math import sqrt

# input
F1_score_final_STANDARD_DEVIATION = sys.argv[1]
# RMSE_final_STANDARD_DEVIATION = sys.argv[1]
# Pearson_correlation_final_STANDARD_DEVIATION = sys.argv[1]
# output
analysis_F1_score_Desvio = sys.argv[2]
# analysis_RMSE_Desvio = sys.argv[2]
# analysis_Pearson_correlation_Desvio = sys.argv[2]

with open(F1_score_final_STANDARD_DEVIATION) as f:
# with open(RMSE_final_STANDARD_DEVIATION) as f:
# with open(Pearson_correlation_final_STANDARD_DEVIATION) as f:
    lines = f.readlines()
    f.close()
    mean = 0
    for line in lines:
        number = float(line)
        mean = mean + number

    mean = mean / len(lines)

my_list = [mean]

with open(analysis_F1_score_Desvio, 'w') as output:
# with open(analysis_RMSE_Desvio, 'w') as output:
# with open(analysis_Pearson_correlation_Desvio, 'w') as output:
    for item in my_list:
        output.write("%s\n" % item)

# Por o seguinte código na linha de comando:
        # python analysis.py F1_score_final_STANDARD_DEVIATION.txt analysis_F1_score_Desvio.txt
# Por o seguinte código na linha de comando:
        # python analysis.py RMSE_final_STANDARD_DEVIATION.txt analysis_RMSE_Desvio.txt
# Por o seguinte código na linha de comando:
        # python analysis.py Pearson_correlation_final_STANDARD_DEVIATION.txt analysis_Pearson_correlation_Desvio.txt
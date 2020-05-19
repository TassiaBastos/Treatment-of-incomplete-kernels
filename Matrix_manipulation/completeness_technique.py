
import numpy as np


class Techniques:
    @staticmethod
    def technique_1(cells, data, tech):
        tech_complete = 0
        if (tech == "average"):
            average = data.mean()
            for i in range(0, len(cells)):
                data[cells[i][0]][cells[i][1]] = average

        elif (tech == "median"):
            median = data.median()
            for i in range(0, len(cells)):
                data[cells[i][0]][cells[i][1]] = median
        else:
            for i in range(0, len(cells)):
                data[cells[i][0]][cells[i][1]] = 0
                print()
        return data






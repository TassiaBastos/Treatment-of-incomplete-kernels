import numpy as np
import random

from completeness_technique import Techniques


class MatrixCleaner:
    @staticmethod
    def load(filename):
        dimension = MatrixCleaner.get_dimension(filename)
        matrix = np.loadtxt(filename, skiprows=0, usecols=range(0, dimension))
        return matrix

    @staticmethod
    def get_dimension(filename):
        try:
            f = open(filename, "r")
            dimension = len(f.readlines())
            f.close()
            return dimension
        except UnicodeDecodeError:
            raise Exception("Unsupported encoding on file: " + filename)

    @staticmethod
    def get_random_cells(dimension, percentage):
        cells = []
        size = dimension ** 2
        from math import ceil
        desired_cell_count = ceil((size / 2) * (percentage / 100))
        print("Total of positions selected: ", desired_cell_count)
        while len(cells) < desired_cell_count * 2:
            cell = MatrixCleaner.get_random_cell(dimension)
            if MatrixCleaner.should_append(cell, cells):
                cells.append(cell)
                cells.append(tuple(reversed(cell)))
        return cells

    @staticmethod
    def should_append(cell, cells):
        condition_1 = cell not in cells
        condition_2 = cell[0] != cell[1]
        return condition_1 and condition_2

    @staticmethod
    def get_random_cell(dimension):
        random_row = random.randrange(dimension)
        random_column = random.randrange(dimension)
        position = random_row, random_column
        return position


if __name__ == '__main__':
    # fileName = "Kc_cn_146.txt"
    # fileName = "Kc_cn_270.txt"
    # fileName = "Kc_cn_417.txt"
    # fileName = "Kc_expression_147.txt"
    # fileName = "Kc_expression_163.txt"
    # fileName = "Kc_expression_177.txt"
    # fileName = "Kc_methylation_176.txt"
    # fileName = "Kc_methylation_210.txt"
    # fileName = "Kc_methylation_252.txt"
    # fileName = "Kc_mutation_57.txt"
    # fileName = "Kc_mutation_71.txt"
    # fileName = "Kc_mutation_132.txt"
    # fileName = "Kd_circular.txt"
    # fileName = "Kd_estate.txt"
    # fileName = "Kd_ext.txt"
    # fileName = "Kd_graph.txt"
    # fileName = "Kd_hybr.txt"
    # fileName = "Kd_kr.txt"
    # fileName = "Kd_maccs.txt"
    # fileName = "Kd_PubChem.txt"
    # fileName = "Kd_sp.txt"
    fileName = "Kd_std.txt"

    # percent = [10, 30, 50, 70]
    percent = [10]
    # percent = [30]
    # percent = [50]
    # percent = [70]

    # techniques = ['zero', 'average', 'median']
    # techniques = ['average']
    # techniques = ['median']
    # techniques = ['zero']
    techniques = ['na']


    data = MatrixCleaner.load(filename=fileName)

    for perc in percent:
        cells = MatrixCleaner.get_random_cells(len(data), perc)
        data_modified = data.copy()

        for tech in techniques:
            Techniques.technique_1(cells, data_modified, tech)

            # só falta rodar!!
            np.savetxt("Modified" + "_" + tech + "_" + str(perc) + "_" + fileName, data_modified, delimiter='\t')

            # np.savetxt('/home/tassia/Scenario 3 - all change/data_base/Scenario-03/Scenario-03_zero_70/Iteration-03/'
            #            + "Modified" + "_" + tech + "_" + str(perc) + "_" + fileName, data_modified, delimiter='\t')

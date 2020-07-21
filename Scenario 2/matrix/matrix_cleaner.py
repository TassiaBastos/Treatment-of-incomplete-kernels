import numpy as np
import random

from completeness_technique import Techniques


class MatrixCleaner:
    @staticmethod
    def load(filename):
        dimension = MatrixCleaner.get_dimension(filename)
        matrix = np.loadtxt(filename, skiprows=1, usecols=range(1, dimension))
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
    fileName = "Kc_expression_163.txt"
    # fileName = "Kc_methylation_176.txt"
    # fileName = "Kd_PubChem.txt"
    percent = [10, 30, 50, 70]
    techniques = ['zero', 'average', 'median']
    techniques = ['zero']
    data = MatrixCleaner.load(filename=fileName)

    for perc in percent:
        cells = MatrixCleaner.get_random_cells(len(data), perc)
        data_modified = data.copy()

        for tech in techniques:
            Techniques.technique_1(cells, data_modified, tech)

            for cell in cells:
                with open('vectorPosition_nr_simmat_drugs_lambda.txt', 'a') as vectorPosition_01_data1:
                    vectorPosition_01_data1.write('\n'.join(str(cells) for item in cell))
                    vectorPosition_01_data1.write('\n')

            # print("Set of selected cells in the matrix: ", cells)
            # print()
            # print("Matrix original:")
            # print(data)
            # print("________________________________________________")
            # print("Matrix modified:")
            # print(data_modified)

            # só falta rodar!!
            np.savetxt('path_modified/' + "Average" + "_" + tech + "_" +
                    str(perc) + "_" + fileName, data_modified, delimiter='\t')

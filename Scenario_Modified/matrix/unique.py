import sys

# inputfile
# vectorPositions = sys.argv[1]
vectorPosition_01_Cell01_01 = sys.argv[1]
# outputfile
# vectorPositionsCleaned = sys.argv[2]
vectorPositionCleaned_01_Cell01_01 = sys.argv[2]

with open(vectorPosition_01_Cell01_01) as f:
    content = f.readlines()

content = [x.strip() for x in content]

my_list = list(set(content))

with open(vectorPositionCleaned_01_Cell01_01, 'w') as output:
    for item in my_list:
        output.write("%s\n" % item)

# Abrir um terminal na pasta que contém o 'inputfile'
# Por o seguinte código na linha de comando: python unique.py inputfile.txt outputfile.txt

# (Nota: lembrar de ajustar os nomes dos arquivos)
# python unique.py vectorPositions.txt vectorPositionsCleaned.txt

# python unique.py vectorPosition_01_Cell01_01.txt vectorPositionCleaned_01_Cell01_01.txt

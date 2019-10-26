from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from ortools.sat.python import cp_model

def kakuro(sums,output):
    CpModel = cp_model.CpModel()
    CpSolver = cp_model.CpSolver()

    x1 = CpModel.NewIntVar(1, 9, 'x1')
    x2 = CpModel.NewIntVar(1, 9, 'x2')
    x3 = CpModel.NewIntVar(1, 9, 'x3')
    
    y1 = CpModel.NewIntVar(1, 9, 'y1')
    y2 = CpModel.NewIntVar(1, 9, 'y2')
    y3 = CpModel.NewIntVar(1, 9, 'y3')
    
    z1 = CpModel.NewIntVar(1, 9, 'z1')
    z2 = CpModel.NewIntVar(1, 9, 'z2')
    z3 = CpModel.NewIntVar(1, 9, 'z3')
    
    CpModel.Add(x1 + x2 + x3 == int(sums[3]))
    CpModel.Add(y1 + y2 + y3 == int(sums[4]))
    CpModel.Add(z1 + z2 + z3 == int(sums[5]))
    CpModel.Add(x1 + y1 + z1 == int(sums[0]))
    CpModel.Add(x2 + y2 + z2 == int(sums[1]))
    CpModel.Add(x3 + y3 + z3 == int(sums[2]))
    
    
    firstRow     = [x1,x2,x3]
    secondRow    = [y1,y2,y3]
    thirdRow     = [z1,z2,z3]
    firstColumn  = [x1,y1,z1]
    secondColumn = [x2,y2,z2]
    thirdColumn  = [x3,y3,z3]
    
    
    CpModel.AddAllDifferent(firstRow)
    CpModel.AddAllDifferent(secondRow)
    CpModel.AddAllDifferent(thirdRow)
    CpModel.AddAllDifferent(firstColumn)
    CpModel.AddAllDifferent(secondColumn)
    CpModel.AddAllDifferent(thirdColumn)
    
    status = CpSolver.Solve(CpModel)
    if status == cp_model.FEASIBLE:
        kakurosOutputFile.writelines(str(sum[3]) + "," + str(CpSolver.Value(x1)) + "," + str(CpSolver.Value(x2)) + "," + str(CpSolver.Value(x3)) + "\n")
        kakurosOutputFile.writelines(str(sum[4].strip()) + "," + str(CpSolver.Value(y1)) + "," + str(CpSolver.Value(y2)) + "," + str(CpSolver.Value(y3)) + "\n")
        kakurosOutputFile.writelines(str(sum[5].strip()) + "," + str(CpSolver.Value(z1)) + "," + str(CpSolver.Value(z2)) + "," + str(CpSolver.Value(z3)) + "\n")



kakurosInputFile = open("kakuro_input.txt",'r')
lines = kakurosInputFile.readlines()
sum = []
for i in lines :
    linesplit = i.strip().split(",")
    for x in linesplit :
        sum.append(x)
kakurosInputFile.close()
        

kakurosOutputFile = open("kakuro_output.txt",'w')
line = lines[0].strip().replace(" ","")
kakurosOutputFile.writelines("x" + "," + str(line) + "\n")



kakuro(sum,kakurosOutputFile)

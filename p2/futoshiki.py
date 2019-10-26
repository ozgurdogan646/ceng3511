from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from ortools.sat.python import cp_model

def Futoshiki(input,output):
    Cpmodel = cp_model.CpModel()
    CpSolver = cp_model.CpSolver()
    
    A1 = Cpmodel.NewIntVar(1, 4, 'A1')
    A2 = Cpmodel.NewIntVar(1, 4, 'A2')
    A3 = Cpmodel.NewIntVar(1, 4, 'A3')
    A4 = Cpmodel.NewIntVar(1, 4, 'A4')
    
    B1 = Cpmodel.NewIntVar(1, 4, 'B1')
    B2 = Cpmodel.NewIntVar(1, 4, 'B2')
    B3 = Cpmodel.NewIntVar(1, 4, 'B3')
    B4 = Cpmodel.NewIntVar(1, 4, 'B4')
    
    C1 = Cpmodel.NewIntVar(1, 4, 'C1')
    C2 = Cpmodel.NewIntVar(1, 4, 'C2')
    C3 = Cpmodel.NewIntVar(1, 4, 'C3')
    C4 = Cpmodel.NewIntVar(1, 4, 'C4')
    
    D1 = Cpmodel.NewIntVar(1, 4, 'D1')
    D2 = Cpmodel.NewIntVar(1, 4, 'D2')
    D3 = Cpmodel.NewIntVar(1, 4, 'D3')
    D4 = Cpmodel.NewIntVar(1, 4, 'D4')
    
    firstRow     = [A1, A2, A3, A4]
    secondRow    = [B1, B2, B3, B4]
    thirdRow     = [C1, C2, C3, C4]
    fourthRow    = [D1, D2, D3, D4]
    
    firstColumn  = [A1, B1, C1, D1]
    secondColumn = [A2, B2, C2, D2]
    thirdColumn  = [A3, B3, C3, D3]
    fourthColumn = [A4, B4, C4, D4]
    
    Cpmodel.AddAllDifferent(firstRow)
    Cpmodel.AddAllDifferent(secondRow)
    Cpmodel.AddAllDifferent(thirdRow)
    Cpmodel.AddAllDifferent(fourthRow)
    
    Cpmodel.AddAllDifferent(firstColumn)
    Cpmodel.AddAllDifferent(secondColumn)
    Cpmodel.AddAllDifferent(thirdColumn)
    Cpmodel.AddAllDifferent(fourthColumn)
    
    inputFile = open(input, 'r')
    lines = inputFile.readlines()
    
    linesplit = []
    for i in lines:
        
        linesplit.append(i.strip().split(","))
        
    for x in linesplit:
            try:
                if (int(x[1]) > 0):
                    
                    Cpmodel.Add(eval(x[0])==eval(x[1]))
            except:
                
                Cpmodel.Add(eval(x[0])>eval(x[1]))
    
    inputFile.close()
    
    
    outputFile = open(output,'w')
    
    
    status = CpSolver.Solve(Cpmodel)

    if status == cp_model.FEASIBLE:
        
        outputFile.writelines(str(CpSolver.Value(A1))+","+str(CpSolver.Value(A2))+","+str(CpSolver.Value(A3))+","+str(CpSolver.Value(A4))+"\n")
        outputFile.writelines(str(CpSolver.Value(B1))+","+str(CpSolver.Value(B2))+","+str(CpSolver.Value(B3))+","+str(CpSolver.Value(B4))+"\n")
        outputFile.writelines(str(CpSolver.Value(C1))+","+str(CpSolver.Value(C2))+","+str(CpSolver.Value(C3))+","+str(CpSolver.Value(C4))+"\n")
        outputFile.writelines(str(CpSolver.Value(D1))+","+str(CpSolver.Value(D2))+","+str(CpSolver.Value(D3))+","+str(CpSolver.Value(D4))+"\n")

Futoshiki("futoshiki_input.txt","futoshiki_output.txt")
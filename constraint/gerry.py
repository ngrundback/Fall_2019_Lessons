import constraint
# 0 connected to 1, 1 connected to 2, etc
problem = constraint.Problem()
# problem.addVariable('x1', [1,1,1,1,0,0])
# problem.addVariable('x2', [1,1,1,0,0])
# problem.addVariable('x3', [0,0,0,0,0,1])
# problem.addVariable('x4', [0,0,0,0,0,1])
# problem.addVariable('x5', [1,1,1,0,0])

# range 0-5
# adding variables 0-5 with range 0-1
for i in range(0,5):
    problem.addVariables(range(i*10, i*10+10), range(0,1))

# add constraint all

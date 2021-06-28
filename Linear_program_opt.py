from scipy.optimize import minimize

def objective(x):
    return -x[0] - x[1] + 50.0

def ineq_constraint(x):
    return -50.0 * x[0] - 24.0 * x[1] + 2400

def ineq_constraint2(x):
    return -30.0 * x[0] - 33.0 * x[1] + 2100

def ineq_constraint3(x):
    return x[0]-45

def ineq_constraint4(x):
    return x[1]-5



con1 = {'type': 'ineq', 'fun': ineq_constraint}
con2 = {'type': 'ineq', 'fun': ineq_constraint2}
con3 = {'type': 'ineq', 'fun': ineq_constraint3}
con4 = {'type': 'ineq', 'fun': ineq_constraint4}

cons = ([con1, con2, con3, con4])

x0 = (0,0)

sol = minimize(objective,x0, method='SLSQP', constraints=cons)

print(sol.x)








import pandas as pd
M = {"Student": ["Ice Bear", "Panda", "Grizzly"], "Math": [80,95,79]}
E = {"Student": ["Ice Bear", "Panda", "Grizzly"], "Electronics": [85,81,83]}
G = {"Student": ["Ice Bear", "Panda", "Grizzly"], "GEAS": [90,79,93]}
ES = {"Student": ["Ice Bear", "Panda", "Grizzly"], "ESAT": [93,89,88]}
 
math = pd.DataFrame(M, columns = ["Student", "Math"])
electronics= pd.DataFrame(E, columns = ["Student", "Electronics"]) 
geas= pd.DataFrame(G, columns = ["Student", "GEAS"])  
esat = pd.DataFrame(ES, columns = ["Student", "ESAT"]) 
score = pd.merge(pd.merge(math,electronics, on = "Student"),
                pd.merge(geas, esat, on = "Student") , on = "Student")
score2 = pd.melt(score, id_vars = ["Student"], var_name = "Subject", value_name = "Grades")

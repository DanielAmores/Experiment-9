import pandas as pd
x = {"Box": ["Box 1", "Box 1","Box 1","Box 2","Box 2","Box 2"], "Dimension":["Length","Width","Height","Length","Width","Height"],"Value": [6,4,2,5,3,4]}
box = pd.DataFrame(x, columns = ["Box", "Dimension", "Value"])
boxtidy = box.pivot_table(index = "Box", columns = "Dimension", values = "Value")
boxtidy['Volume'] = boxtidy.Length * boxtidy.Width * boxtidy.Height
mag= "Hallo world"
print ("mag")
info_table = [
    {"color": "green", "number": 7},
    {"color": "red", "number": 2},
    {"color": "orange", "number": 1}
]

import pandas as pd
df = pd.DataFrame(info_table)
type(df) 
print(df["color"]) 
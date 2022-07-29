import pandas as pd
import numpy as np


# Reading the csv file
df_new = pd.read_csv('output_91.csv')

# saving xlsx file
GFG = pd.ExcelWriter('output_91.xlsx')
df_new.to_excel(GFG, index = False)

GFG.save()
# GFG.close()

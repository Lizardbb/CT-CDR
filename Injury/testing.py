import pandas as pd
import plotly.express as px
workzone_df = pd.read_csv("WorkzoneInjuries.csv") 
#print(workzone_df)

test_df = px.data.tips()
print(test_df)
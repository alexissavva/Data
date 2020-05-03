import pandas as pd
df = pd.read_csv('2013-10-01_capture-win8.weblogng.csv', sep='\t')
df.to_excel('output.xlsx', 'Sheet1',index=False)



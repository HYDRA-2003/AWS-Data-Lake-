# import os
# import pandas as pd
# import glob
# from datetime import datetime
# data = []
# globbed_files = glob.glob("Historic Data/*.csv")
# print(globbed_files)
# from datetime import datetime
# current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S-%f")
# str_current_datetime = str(current_datetime)
# file_name = str_current_datetime+".csv"
# for fp in globbed_files:
#     df=pd.read_csv(fp).assign(New=os.path.basename(fp).split('.')[0])
#     df.to_csv(r'F:\Software\danish\Alapex\Historic Data Changed Names\\'+file_name)
# print(df)
import pandas as pd 
import os
from datetime import datetime
path = r'F:\Software\danish\Alapex\Historic Data\\' 
files = os.listdir(path)
df_total = pd.DataFrame()
for file in files:

    df_temp = pd.read_csv( path + "\\" + file) 
    current_datetime = datetime.now().strftime("%H-%M-%S-%f")
    str_current_datetime = str(current_datetime)
    file_name = str_current_datetime+".csv"
    df_temp['Sector Name'] = file.replace(".csv","")
    df_temp.to_csv(r'F:\Software\danish\Alapex\Historic Data Changed Names\\'+file_name)

    # df_total = df_total.append(df_temp)

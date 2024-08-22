import pandas as pd
df=pd.read_csv("C:\\Users\\kvsan\\Desktop\\Ml projects\\Shark Tank india\\Season1\\Shark_Tank_India_S1.csv")
def shark_wise(df,shark):
    number=df[df[shark+"_"+"invested"]==1].shape[0]
    total=round(((df[df[shark+"_"+"invested"]==1]["amount_per_shark"].sum())*0.01),2)
    max=round(((df[df[shark+"_"+"invested"]==1]["amount_per_shark"].max())*0.01),2)
    max_val=round(((df[df[shark+"_"+"invested"]==1]["deal_valuation"].max())*0.01),2)
    return number,total,max,max_val
def plot_statistics(select):
    sharks ={"aman":[29,8.95,1],"anupam":[24,5.34,0.5],"ashneer":[21,4.94,0.7],"ghazal":[7,1.3,0.33],"namita":[24,7.05,0.75],"peyush":[28,7.7,1.0],"vineeta":[16,3.35,0.4]}
    sharks=pd.DataFrame(sharks)
    rotated_df = sharks.transpose()[::-1]
    rotated_df.rename(columns={0:"Number of Deals",1:"Total_investments",2:"Max_investments"},inplace=True)
    sorted_df=rotated_df.sort_values(by=select)
    return sorted_df
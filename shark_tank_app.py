import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import helper
import seaborn as sns
df=pd.read_csv("C:\\Users\\kvsan\\Desktop\\Ml projects\\Shark Tank india\\Season1\\Shark_Tank_India_S1.csv")
st.sidebar.title("Shark Tank India")
st.sidebar.image("https://im.rediff.com/movies/2021/dec/28shark-tank-india-3.jpg?w=670&h=900")
user=st.sidebar.radio("Season",("Season 1","Season 2"))
if user == "Season 1":
    st.title("High Level Statistics")
    col1,col2,col3=st.columns(3)
    with col1:
        st.header("Deals/Total")
        st.title("68/121")
    with col2:
        st.header("Total Invested")
        st.title("38.63 cr")
    with col3:
        st.header("Equity/Debt")
        st.title("35.12/3.15cr")

    col4,col5,col6=st.columns(3)
    with col4:
        st.header("Max offered")
        st.title("1.5 cr")
    with col5:
        st.header("Max Valuation")
        st.title("66.6 cr")
    with col6:
        st.header("All Shark deals")
        st.title("4")
    shark=st.selectbox("Select a shark",("aman","anupam","ashneer","ghazal","namita","peyush","vineeta"))
    st.title(shark)
    col1,col2=st.columns(2)
    number,total,max,max_val=helper.shark_wise(df,shark)
    with col1:
        st.header("No. of Deals")
        st.title(number)
    with col2:
        st.header("Total Invested in cr")
        st.title(total)
    col3,col4=st.columns(2)
    with col3:
        st.header("Max Invested in cr")
        st.title(max)
    with col4:
        st.header("Max Valuation in cr")
        st.title(max_val)
    st.header("Sharks investments")
    select=st.selectbox("select",["Number of Deals","Total_investments","Max_investments"])
    sorted_df=helper.plot_statistics(select)
    fig,ax=plt.subplots()
    sns.barplot(x=np.array(sorted_df.index),y=sorted_df[select].values)
    st.header(select)
    st.pyplot(fig)
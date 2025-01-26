import streamlit as st
import numpy as np
import pandas as pd
import datetime
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("supermarket_sales.csv")
st.title("** SuperMarket Sales Analysis **")
st.sidebar.title("Set the Parameter")
catego = ['Invoice ID','Branch']
categorical_cols =['City','Customer type','Gender','Product line','Payment']
Time_date_cols =['Time','Date']
numerical_cols= ['Unit price','Quantity','Tax 5%','Total']
numerical_cols2 =['cogs','gross margin percentage','gross income','Rating']

select = st.sidebar.selectbox("Choose Invoice Id or Branch:",catego)
select_1 = st.sidebar.selectbox("Select the Apporitate Parameter:",categorical_cols)
select_2 = st.sidebar.selectbox("Choose Time or Date:",Time_date_cols)
select_3 = st.sidebar.selectbox("Select Column for Comparison:",numerical_cols)
select_4 = st.sidebar.selectbox("Select Parameter for Comparison",numerical_cols2)

st.header("Total Sales Vs Different Parameter Across Branch")
st.markdown("--------------------------------------------------------------------------------------------------------------------------------------")
select1 = df.groupby(['Invoice ID','Branch'])['Total'].sum().nlargest(20).reset_index()
if catego:
    if select in catego:
        if select == "Invoice ID":
            fig = px.bar(select1,x=select,y='Total',color='Branch',title='Total vs. Invoice Id Across Branch')
        else:
            fig = px.bar(select1,x=select,y='Total',color='Branch',title='Total vs. Branch Across Branch')
    st.plotly_chart(fig)

st.header("Product line with repect to different Unit price Vs Total")
st.markdown("--------------------------------------------------------------------------------------------------------------------------------------")
if categorical_cols:
    if select_1 in categorical_cols:
        fig= px.scatter(df,x='Unit price',y='Total',color='Product line',title="Product line wrt Unit Price vs total")
    st.plotly_chart(fig)

st.header("Amount spent in total by different Parameter wrt Product line")
st.markdown("------------------------------------------------------------------------------------------------------------------------")
if categorical_cols:
    if select_1 in categorical_cols:
        fig = px.bar(df,x=select_1,y='Total',color='Product line',title=f'Amount Spent in total by {select_1} wrt Product')
    st.plotly_chart(fig)

st.header("Ratings of product by both genders") 
st.markdown("------------------------------------------------------------------------------------------------------------------")      
fig = px.bar(df,x='Product line',y='Rating',color='Gender',title='Ratings of product by both genders')
st.plotly_chart(fig)
st.header("Daily Gross Income Across Cities")
st.markdown("-----------------------------------------------------------------------------------------------------------------------------")
if Time_date_cols:
    if select_2 in Time_date_cols:
        fig = px.scatter(df,x=select_2,y='gross income',color='City',title=f'Daily Gross Income Across Cities by {select_2.capitalize()}')
    st.plotly_chart(fig)

st.header("Distribution of Total Sales by Categories")
st.markdown("---------------------------------------------------------------------------------------------------------------------------")
if categorical_cols:
    if select_1 in categorical_cols:
        if select_1 =="City":
            fig=px.box(df,x=select_1,y='Total')
        elif select_1 =="Customer type":
            fig = px.box(df,x=select_1,y='Total',points ="all")
        elif select_1 == "Gender":
            fig=px.box(df,x=select_1,y='Total')
        elif select_1 =="Product line":
            fig = px.box(df,x=select_1,y='Total',points ="all")
        else:
            fig=px.box(df,x=select_1,y='Total')
    st.plotly_chart(fig)

st.header(f"Pie Chart of {select_4} with Respect to City")
st.markdown("---------------------------------------------------------------------------------------------------------------------")
if numerical_cols2:
    if select_4 in numerical_cols2:
        fig = px.pie(df,values=select_4,names='City',title=f'{select_4} wrt city')
    st.plotly_chart(fig)

Total_Amount_branch= df.groupby(['Branch','Customer type','Gender'])['Total'].sum().reset_index()
st.header("Total Amount by Branch, Customer Type, and Gender (Stacked)")
st.markdown("---------------------------------------------------------------------------------------------------------------------")
fig = px.bar(Total_Amount_branch,x='Branch',y= 'Total',color='Gender',barmode='stack',facet_col='Customer type',title='Total Amount by Branch, Customer Type, and Gender (Stacked)')
st.plotly_chart(fig)

st.header(f'Relationship Between {select_3}, Total Sales, and Gross Income Across Cities Over Time')
st.markdown("-------------------------------------------------------------------------------------------------------------------")
if numerical_cols:
    if select_3 in numerical_cols:
        fig = px.scatter(df,x=select_3,y='Total',color='City',size='gross income',hover_name='Product line',animation_frame='Date',range_x=[30,90],title=f'Relationship Between {select_3}, Total Sales, and Gross Income Across Cities Over Time')
    st.plotly_chart(fig)
    
st.header("Tax Distribution by Payment Method and Customer Type with Total Sales Insight")
st.markdown("-------------------------------------------------------------------------------------------------------------------")
fig = px.bar(df,x='Payment',y='Tax 5%',color='Total',barmode='group',facet_col='Customer type',title='Tax Distribution by Payment Method and Customer Type with Total Sales Insight')
st.plotly_chart(fig)

st.header("Total Sales vs. Unit Price Across Cities")
st.markdown("-------------------------------------------------------------------------------------------------------------------")
per_price = df.groupby(['Unit price','City'])['Total'].sum().reset_index()
fig = px.line(per_price,x='Unit price',y='Total',color='City',title='Total Sales vs. Unit Price Across Cities')
st.plotly_chart(fig)



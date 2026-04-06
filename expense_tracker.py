import streamlit as st
st.set_page_config(
 page_title="Expense Buddy",
 page_icon="icon.png",
 layout="wide"
)
import pandas as pd
import os
import matplotlib.pyplot as plt

FILE = "expenses.csv"

# Create CSV if not exists
if not os.path.exists(FILE):
 df = pd.DataFrame( columns=["Date", "Category", "Amount", "Description"] )
 df.to_csv(FILE, index=False)

st.title("💼 Expense Buddy")

menu = st.sidebar.selectbox ( "Menu",["Add Expense", "View Expenses", "Summary"])

# Add Expense
if menu == "Add Expense":
 st.subheader("Add New Expense")
 date = st.date_input("Date")
 category = st.selectbox("Category",["Food", "Travel", "Shopping", "Bills", "Others"] )
 amount = st.number_input( "Amount", min_value=0.0 )
 description = st.text_input("Description")
 if st.button("Add Expense"):
   new_data = pd.DataFrame({ "Date": [date], "Category": [category], "Amount": [amount], "Description": [description] })
   new_data.to_csv(FILE, mode='a', header=False, index=False )
   st.success("Expense Added!")

# View Expenses
elif menu == "View Expenses":
  st.subheader("All Expenses")
  df = pd.read_csv(FILE)
  st.dataframe(df)

# Summary
elif menu == "Summary":
  st.subheader("Expense Summary")
  df = pd.read_csv(FILE)
  if not df.empty:
      category_sum = df.groupby("Category")[ "Amount" ].sum()
      fig, ax = plt.subplots()
      category_sum.plot( kind="bar", ax=ax )
      st.pyplot(fig)
  else:
      st.warning("No Data Available")

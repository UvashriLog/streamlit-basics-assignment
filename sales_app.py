import streamlit as st
import pandas as pd

#  Title and description
st.title("Sales Summary Dashboard")
st.subheader("Interactive view of product sales by category")

#  Create hardcoded dataset
data = {
    "Product": ["Laptop", "Shirt", "Phone", "Shoes", "Tablet"],
    "Category": ["Electronics", "Clothing", "Electronics", "Clothing", "Electronics"],
    "Sales": [50000, 2000, 30000, 4000, 15000]
}

df = pd.DataFrame(data)

#  Sidebar filter
st.sidebar.header("Filter Options")
selected_category = st.sidebar.selectbox(
    "Select Category",
    df["Category"].unique()
)

#  Filter data
filtered_df = df[df["Category"] == selected_category]

#  Show filtered data
st.write(f"Showing results for: {selected_category}")
st.dataframe(filtered_df)

# Line chart
st.line_chart(filtered_df["Sales"])
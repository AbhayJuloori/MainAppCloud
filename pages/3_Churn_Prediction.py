import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from cleaning_data import correlation_matrix, customer_engagement

# Assuming customer_engagement and correlation_matrix are pre-defined DataFrames

# Correlation Heatmap
st.write("### Correlation Analysis Between Disengagement and Demographics")
# Displaying heatmap using st.pyplot, as Streamlit doesn't have a native heatmap function
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", ax=ax)
plt.title("Correlation Analysis Between Disengagement and Demographics")
st.pyplot(fig)

# Total Spend Trends by Disengagement Status
st.write("### Total Spend Trends by Disengagement Status")
# Group by year and disengagement status, and plot using st.line_chart
total_spend_trends = customer_engagement.groupby(['year', 'disengaged'])['total_spend'].sum().unstack()
st.line_chart(total_spend_trends)

# Purchase Frequency Trends by Disengagement Status
st.write("### Purchase Frequency Trends by Disengagement Status")
# Group by year and disengagement status, and plot using st.line_chart
purchase_frequency_trends = customer_engagement.groupby(['year', 'disengaged'])['frequency_of_purchase'].sum().unstack()
st.line_chart(purchase_frequency_trends)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_data():
    df = pd.read_csv('metadata.csv', low_memory=False)
    df = df.dropna(subset=['title', 'publish_time'])
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    return df

df = load_data()

st.title("CORD-19 Research Papers Explorer")

# Sidebar filter for year range
year_min = int(df['year'].min())
year_max = int(df['year'].max())
year_filter = st.sidebar.slider('Select year range', year_min, year_max, (2019, 2021))

filtered_df = df[(df['year'] >= year_filter[0]) & (df['year'] <= year_filter[1])]

st.write(f"Number of papers from {year_filter[0]} to {year_filter[1]}: {len(filtered_df)}")

# Plot papers per year in filtered range
papers_per_year = filtered_df.groupby('year').size()

fig, ax = plt.subplots()
sns.lineplot(x=papers_per_year.index, y=papers_per_year.values, ax=ax)
ax.set_title('Number of Papers Published per Year')
ax.set_xlabel('Year')
ax.set_ylabel('Number of Papers')
st.pyplot(fig)

# Show sample papers table
st.subheader('Sample Papers')
st.write(filtered_df[['publish_time', 'title']].head(10))

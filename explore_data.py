import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Load dataset
    df = pd.read_csv('metadata.csv', low_memory=False)
    print("Initial data:")
    print(df.head())

    print("\nInfo:")
    print(df.info())

    print("\nMissing values:")
    print(df.isnull().sum())

    # Clean data
    df = df.dropna(subset=['title', 'publish_time'])
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year

    # Papers per year
    papers_per_year = df.groupby('year').size()
    print("\nPapers per year:")
    print(papers_per_year)

    # Top 10 journals
    top_journals = df['journal'].value_counts().head(10)
    print("\nTop 10 journals by paper count:")
    print(top_journals)

    # Plot papers per year
    plt.figure(figsize=(10,6))
    sns.lineplot(x=papers_per_year.index, y=papers_per_year.values)
    plt.title('Number of Papers Published per Year')
    plt.xlabel('Year')
    plt.ylabel('Number of Papers')
    plt.show()

    # Plot top journals
    plt.figure(figsize=(10,6))
    sns.barplot(x=top_journals.values, y=top_journals.index)
    plt.title('Top 10 Journals by Paper Count')
    plt.xlabel('Number of Papers')
    plt.ylabel('Journal')
    plt.show()

if __name__ == '__main__':
    main()

# Frameworks_Assignment

## Overview

This project analyzes the CORD-19 research dataset and presents an interactive web application using Streamlit. The app allows users to explore COVID-19 research papers by filtering publication years and viewing trends.

---

## Dataset

- The dataset used is the `metadata.csv` file from the CORD-19 dataset.
- Contains paper titles, abstracts, publication dates, authors, journals, and source information.
- The dataset should be placed in the root project directory.

---

## Features

- Load and clean the dataset by handling missing values.
- Analyze the number of papers published per year.
- Interactive year range slider to filter papers.
- Line chart visualizing publication trends over years.
- Display of sample paper titles with publication dates.

---

## Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd Frameworks_Assignment
````

2. Install required packages:

```bash
pip install pandas matplotlib seaborn streamlit
```

---

## Usage

To run the Streamlit app, execute:

```bash
streamlit run app.py
```

Open the provided localhost URL in your browser to access the app.

---

## Optional

Run the data exploration script for additional analysis:

```bash
python explore_data.py
```

---

## Project Structure

```
Frameworks_Assignment/
├── app.py                # Streamlit app
├── explore_data.py       # Data exploration and visualization
├── metadata.csv          # Dataset file
└── README.md             # Project documentation
```

---

## Notes

* Ensure `metadata.csv` is in the project directory.
* The app caches data loading for faster performance.
* Modify filters in the sidebar to explore different publication year ranges.

---

## Author

Your Name Here

---

## References

* [CORD-19 Dataset on Kaggle](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)
* [Streamlit Documentation](https://docs.streamlit.io/)
* [Pandas Documentation](https://pandas.pydata.org/)
* [Seaborn Documentation](https://seaborn.pydata.org/)


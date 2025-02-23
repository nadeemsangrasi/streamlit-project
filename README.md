# Data Sweeper App with Streamlit

A simple web application built with [Streamlit](https://streamlit.io/) that allows you to upload a CSV file, preview its contents, perform basic data cleaning (removing duplicates and filling missing values), and download the cleaned data. The app also includes a fixed footer that displays "Created by Nadeem Khan".

## Features

- **File Upload:** Easily upload CSV files for processing.
- **Data Preview:** View a preview of your original data.
- **Data Cleaning:**
  - Remove duplicate rows.
  - Fill missing values:
    - Numeric columns are filled with the mean value.
    - Non-numeric columns are filled with the mode (or a default value).
- **Progress Bar:** Visual feedback during the cleaning process.
- **Download Option:** Download the cleaned data as a CSV file.
- **Footer:** A fixed footer that reads "Created by Nadeem Khan".

## Getting Started

### Prerequisites

- Python 3.12 or higher
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your_username/your_repo.git
   cd your_repo
   ```

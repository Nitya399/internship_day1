# Netflix Titles Dataset - Data Cleaning Project

---

## Task Date
**7th April 2025**

## Performed By
**Nitya Patel**

---

## Objective
To clean and preprocess the Netflix Titles dataset to make it analysis-ready by handling missing values, fixing inconsistencies, and standardizing data formats.

---

## Tasks Performed

### 1. **Handled Missing Values** (without dropping rows)
- `director`: Filled with `'Unknown Director'`
- `cast`: Filled with `'Not Specified'`
- `country`: Filled with `'Unknown Country'`
- `date_added`: Filled with `'2000-01-01'`
- `rating`: Filled with `'Unrated'`
- `duration`: Filled with `'0 Unknown'`
- `duration_int`: Filled with `0`
- `duration_type`: Filled with `'Unknown'`

### 2. **Converted `date_added` to datetime format**
- Original format: `"September 25, 2021"`
- Converted to Python datetime: `2021-09-25`

### 3. **Standardized the `duration` column**
- Split into:
  - `duration_int`: Numeric part (e.g., `90`)
  - `duration_type`: Unit (e.g., `"min"`, `"Season(s)"`)

### 4. **Removed Extra Spaces in Categorical Columns**
- Trimmed and standardized values in:
  - `country`
  - `rating`

### 5. **Checked & Fixed Data Types**
- Ensured `date_added` is in `datetime` format
- `duration_int` is of type `int`
- `duration_type` is a clean string column

---

## Final Output
- Cleaned Excel file: `netflix_titles_cleaned.xlsx`
- Cleaned and analysis-ready dataset with no null values and consistent formatting

---

##  Ready For
- Exploratory Data Analysis (EDA)
- Dashboarding (Power BI, Tableau)
- Machine Learning / Recommendations
- Time Series Trends & Insights

---

##  Files Included
- `netflix_titles.csv` – Original Dataset
- `netflix_titles_cleaned.xlsx` – Cleaned Dataset
- `main.py` – Python code used for cleaning
- `netflix_data_cleaning_report.pdf` – Project summary/report
- `README.md` – Project documentation

---

##  Notes
- All missing values were handled with domain-relevant default values.
- No rows were dropped; focus was on retention and repair.

---

##  Contact
For queries or collaboration:  
**Nitya Patel** – [LinkedIn](https://www.linkedin.com/)


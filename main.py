import pandas as pd

# Load the dataset (use raw string to avoid unicode error on Windows)
df = pd.read_csv(r"C:\Users\DELL\Downloads\internshi_day1\netflix_titles.csv")

# 1. Convert 'date_added' to datetime format
df['date_added'] = pd.to_datetime(df['date_added'], format='%B %d, %Y', errors='coerce')

# 2. Standardize 'duration' column
df[['duration_int', 'duration_type']] = df['duration'].str.extract(r'(\d+)\s*(\w+)', expand=True)
df['duration_int'] = df['duration_int'].astype(float)  # float allows NaNs

# 3. Strip whitespaces from 'country' and 'rating'
df['country'] = df['country'].str.strip()
df['rating'] = df['rating'].str.strip()

# 4. Handle missing values
df['director'] = df['director'].fillna('Unknown Director')
df['cast'] = df['cast'].fillna('Not Specified')
df['country'] = df['country'].fillna('Unknown Country')
df['date_added'] = df['date_added'].fillna(pd.Timestamp('2000-01-01'))
df['rating'] = df['rating'].fillna('Unrated')
df['duration'] = df['duration'].fillna('0 Unknown')
df['duration_int'] = df['duration_int'].fillna(0)
df['duration_type'] = df['duration_type'].fillna('Unknown')

# 5. Save the cleaned data to a new Excel file
output_path = r"C:\Users\DELL\Downloads\internshi_day1\netflix_titles_cleaned.xlsx"
df.to_excel(output_path, index=False)

print(f"✅ Cleaned data saved to: {output_path}")


import sys
import pandas as pd
from pathlib import Path

# Get all files in a folder. Hopefully they will all be CSV files.
def get_files(folder: Path) -> list[Path]:
    return [p for p in folder.iterdir() if p.is_file()]

if len(sys.argv) < 4:
    print("Usage: python combine-traps.py <folder with individual CSV lists> <course_id> <assignment_id>")
    sys.exit(1)

data_folder = Path(sys.argv[1])
COURSE_ID = sys.argv[2]
ASSIGNMENT_ID = sys.argv[3]
fold_name = data_folder.name
files = get_files(data_folder)

# Load all CSV files
files = [ pd.read_csv(f) for f in files ]

# Combine all rows
combined = pd.concat(files, ignore_index=True)

# Keep only the required columns
combined = combined[['submission_id', 'uin', 'name', 'email']]

# Drop duplicate UINs, keeping the first occurrence
combined = combined.drop_duplicates(subset='uin', keep='first')

# Prepend the Gradescope URL to each submission_id
url_prefix = f"https://www.gradescope.com/courses/{COURSE_ID}/assignments/{ASSIGNMENT_ID}/submissions/"
combined['submission_id'] = url_prefix + combined['submission_id'].astype(str)
combined = combined.rename(columns={'submission_id': 'submission_link'})    # Rename for clarity

# Save result
combined.to_csv(f'./{fold_name}_trapped.csv', index=False)
print(f"Done! {len(combined)} unique UIN rows written.")

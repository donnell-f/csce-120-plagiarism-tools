# Combine Table of Trapped Students

This tool combines tables of students that fell for a single AI trap into a table of all the students that fell for any AI trap.

## Motivation

In Gradescope Sleuth, you can use the Regex List Submissions feature to list metadata about all submissions with a matching keyword (or regex expression) in them. See `./README_fig1.png` for more info. The metadata contains the submission ID that the keyword appears in, the UIN of the student who submitted it, and the contact info for that student. This feature makes finding students that fell for the traps very easy. Better yet: the Streamlit UI makes it easy to download this list as a CSV file.

One problem remains, however: not all AI plagiarists fall for the same traps. Even if someone is using AI to plagiarize their entire assignment, their LLM fight not even fall for every single trap. So, it would be even more helpful to get a list of all students that fell for **any trap** in a given assignment. That is where this script comes in.

## How it Works

Here is how to run this script to get a list of all students that fell for any trap on an assignment

- Find the Gradescope **course ID** and **assignment ID** for the assignment.
    - This can be done by going to the assignment home page (aka. the Review Grades page) and examining the url, which should look like `https://www.gradescope.com/courses/XXXXXXX/assignments/YYYYYYY/review_grades`. The course ID will be the XXXXXXX, and the assignment ID will be the YYYYYYY.
- Throw all the individual CSV lists into a folder in this directory (e.g. `./sorting_algorithm_hw`).
    - The `example_assignment` folder is given as an example.
- Run the following command `python ./combine-traps.py <your folder name> <course ID> <assignment ID>`.
    - This will generate a list of all students that fell for any trap named `<your folder name>_trapped.csv`.
    - It will contain links to the Gradescope submissions with the traps for your convenience.


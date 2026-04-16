# Plagiarism Report Generator

Automatically generate a report by filling in a JSON config file and pasting code into a Markdown file.

## How it Works

How to use this script:

- Copy and paste the Markdown and JSON file for a template from the `templates` folder into this folder.
- Rename the JSON config file to whatever you want your output DOCX file to be named.
- Edit the JSON file so that it has all correct student / professor / homework information in it.
- Edit the Markdown file so that it includes all necessary evidence in it.
    - For the `ai_template.md` specifically, you only need to edit the "List of AI Traps" and "Evidence of AI Traps" sections.
- Run the script using this command: `python ./generate_report.py <report_template>.md <report_json_config>.json`

After that, you should see the DOCX file appear in this folder.

## TODO

Here are some ideas I have for improving this script (ranked by **easiness**):

1. Allow images to be added to the reports.
    - In many cases (but especially when comparing code side-by-side), it may be useful for people to add images to the reports. Better yet: this feature could probably be added to the script in 20 lines of code or less.
    - Markdown already supports image inclusion with the `![Alt text](image-url-or-path)` syntax.
2. Make a database that can use the Gradescope submission ID to get student
name, homework name, student's professor name, section number, etc.
    - This would be moderately easy to do. One would simply need to scrape the Canvas roster and save it to a database (easy) and then link that database with the databases that Gradescope Sleuth saves for each assignment (not so easy).
    - Although this would be slightly challenging, it would be massively helpful for the plagiarism team.
3. Integrate this script into Gradescope Sleuth
    - If this script were integrated into Gradescope Sleuth it would massively increase the throughput of the plagiarism team. Gradescopoe Sleuth could act as our dashboard for all AI plagiarism.
    - Although this task would certainly be non-trivial, Streamlit makes it very easy to create simple data entry UIs, and all you need to create a plagiarism report is a JSON file and a Markdown file.
    - If you, the future maintainer, decide to do this, please just integrate all of the tools in this repo into Gradescope Sleuth. You'll thank me later.

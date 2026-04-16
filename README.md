# CSCE 120 Plagiarism Tools

This repo contains several tried-and-true tools that the CSCE 120 plagiarism team uses to catch plagiarists (mostly AI plagiarists). There is room to improve on all of these tools, so I invite any interested plagiarism team member to make a PR.

Note that these tools have been designed to work for any CSCE course where code is submitted to Gradescope. They are not exclusive to CSCE 120.

All of the tools have their own README.md files with more detailed information, but a brief descriptions of each tool will be given here in order of the tool's importance.

## 🛠️ Gradescope Sleuth

Gradescope Sleuth allows you to download all previous submissions for an assignment and search through all of them for AI traps. It comes with a beautiful (yet simple) graphical interface provided by Streamlit.

## 🛠️ Plagiarism Report Generator

Generates a plagiarism report using a .MD report template and a .JSON config file. Comes pre-loaded with report templates. See its specific README.md for more information; this tool is probably most in need of contribution.

## 🛠️ CSV Trap List Combiner

Gradescope Sleuth gives TAs the ability to download a CSV list (or, perhaps, a table) of all students that fell for a given AI trap in a given assignment. This script will take those specific trap CSV lists as input and give you a CSV list of all students that fell for any of the traps in that assignment.

## 🛠️ Trap Enumeration Script

Given the HTML file for the instructions webpage, this script will tell you exactly which traps the instructions contain.


# 🫆 Gradescope Sleuth 2

Gradescope Sleuth 2 is a tool that allows you to easily sleuth through all submissions for a Gradescope programming assignment. It is equipped with a powerful regex engine that can catch plagiarists at mach speed.

## Starting Gradescope Sleuth 2

You will need to have Anaconda installed in order to run Gradescope Sleuth.

- Consider Miniconda if you are low on disk space...
- If you can't be bothered to set up a `conda` environment, just look at `environment.yml` and install the dependencies manually. There aren't a lot of them.

First, create and activate the conda environment.

- `conda create -f environment.yml`
- `conda activate grade_sleuth`

Then, run Gradescope Sleuth using Streamlit

- `streamlit run app.py`

Then, configure Gradescope Sleuth by giving it the absolute path to a folder of downloaded submissions.

## Configuration

How to configure Gradescope Sleuth:

- Go to the home page (aka. Review Grades page) for your Gradescope assignment and click on the "Export Submissions" folder. Once it is download it, unzip it and remember the path to the unzipped folder.
- Enter a short name (no spaces) for the assignment you want to load into Gradescope Sleuth.
- Enter the path to the unzipped submissions folder.
- Enter the due date for the assignment
- (Optional) Enter the late due date for the assignment (NOTE: doesn't do anything, for now...).
- Network settings (**required for downloading**):
    - Enter the course ID and and assignment ID for the assignment.
        - This can be done by going to the assignment home page (aka. the Review Grades page) and examining the url, which should look like `https://www.gradescope.com/courses/XXXXXXX/assignments/YYYYYYY/review_grades`. The course ID will be the XXXXXXX, and the assignment ID will be the YYYYYYY.
    - Enter your current **remember_me** and **signed_token** cookies for Gradescope.
        - See `./README_fig1.png` to see where to find the cookies.
        - NOTE: these cookies **will change** over time! You can correct them by editing the `<name>.config.json` file for the assignment in the `configs` folder.

Notes on configuration:

- The configuration name will be used to save a new configuration folder to the `configs` folder.
- All the past submissions will be saved to an extremely simple database: `<name>.db`.
- If you need to edit the metadata of a configuration, edit the `<name>.config.json` file.
- Creating a new configuration will probably take a **long time**, but it depends on your hardware. Set a timer for 20 minutes, and if it's not done by then, open up the debugger.

## Features

- Download **all historical submissions** for an assignment
- Regex search all submissions
    - Print list of submissions matching pattern
    - Print the matches themselves (and two lines of surrounding context)
- Print student's entire submission history at once
    - Surprisingly hard to do on Gradescope itself
- Store and reload configurations for past assignments
- [COMING SOON] Print list of students whose first submission was right before the deadline

**NOTE**: Gradescope Sleuth supports **case sensitive regex only**. If you aren't seeing any occurances of an AI trap, make sure you are getting the case right.

## Support / Compatibility

Supports any Gradescope programming assignment (namely Go and C++). Completely cross platform.

## Common Problems

- **Problem**: traps not showing up in Regex List Submissions even though surely some students have fallen for it.
    - **Solution**: probably a case sensitive regex issue. Make sure you are matching the case of your trap well.
- **Problem**: I keep getting an error when I try to download past submissions
    - **Solution**: This is probably because Gradescope is **rate limiting** you. Go to Gradescope.com and see if you have been signed out. If you have, this means that your cookies have expired / been revoked.
    - Try logging in again, updating the `.config.json` file for your assignment with the new `remember_me` and `signed_token` cookies, and attempt to resume downloading the historical submissions.
    - If you get logged out **again** shortly after this, try taking a break for **2 days** so that Gradescope's servers have time to chill out.

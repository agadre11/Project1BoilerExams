# Project1BoilerExams

Project Author: Aryan Gadre

For this project, I decided to do the first option and create a question UI that I would use.

## Features

- Ability to enter question ID to retrieve questions from boiler exams api
- Support for both Free Response and Multiple Choice questions
- Brief statistics for questions solved, accuracy, and answer streak
- Ability to strikethrough/eliminate answer choices in Multiple Choice questions
- Switch between dark theme and light theme
- Sample Questions for each question type implemented


## How to Run

On VSCode:
- Download github repository and then run pip install -r requirements.txt
- Run app.py in the root directory and navigate to the localhost link in the terminal

## Vercel Deployment Link
project1-boiler-exams-a0qpeat5n-agadre11s-projects.vercel.app

## Notes

Although in the resources section of the assessment it says that BoilerExams has Fill in the blank questions available on your website I wasn't able to find any, so I did not implement functionality for those.
I am not sure if BoilerExams has True/False Questions as their own separate so they will just be treated as multiple choice questions with two options.

## AI Use

In this project, I used Gemini to help me figure out how to handle LaTex in my website and what libraries to use (I ended up using the MathJax Library)
I also used AI as a research tool to examine how different fonts and colors would look instead of manually searching for them

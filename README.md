# Career Guide Streamlit

A Streamlit-based career recommendation system designed for Computer Engineering students.

This project aims to help students discover the most suitable specialization areas by combining their course performance, interest areas, and Big Five personality traits. Based on the given inputs, the system generates the top 3 recommended fields such as Artificial Intelligence, Cybersecurity, Backend Development, Frontend Development, Game Development, and Systems.

## Project Purpose

Choosing a career path can be confusing for many students, especially in a broad field like Computer Engineering. This project was developed to provide a simple decision-support tool that offers more personalized guidance based on academic and personal factors.

## Features

- Collects student information through an interactive Streamlit form
- Uses course grades, interest preferences, and personality traits as input
- Applies rule-based preprocessing and scoring logic
- Generates top 3 recommended specialization areas
- Displays recommendation scores in a simple and understandable way
- Provides a practical prototype for education and career guidance

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy

## How It Works

1. The user enters course grades, interest areas, and personality traits through the form.
2. The system preprocesses the input data and converts it into numerical features.
3. A scoring logic evaluates how strongly the student matches different specialization areas.
4. The application returns the top 3 most suitable fields with their scores.

## Project Structure

- `app.py` → main Streamlit application
- `form_schema.py` → form fields and input structure
- `preprocess.py` → input preprocessing and feature generation
- `predict.py` → recommendation logic and scoring
- `requirements.txt` → project dependencies

## Installation


1. Clone the repository:
```bash
git clone https://github.com/enesd3d3/career-guide-streamlit.git
```

2. Go to the project folder:
```bash
cd career-guide-streamlit
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
streamlit run app.py
```

## Future Improvements

- Improve the recommendation logic with a data-driven or machine learning-based approach
- Add a more detailed explanation for each recommended field
- Expand the system for students from different departments
- Improve the user interface and visual design
- Deploy the project online for easier access

- ## Live Demo
> Note: If the app is asleep due to inactivity, the first load may take a few seconds.
[Open the app](https://career-app-luxttrdm99wzcfubkh9pgj.streamlit.app/)

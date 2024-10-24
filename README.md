# Supplement Recommendation System

This is a Flask-based web application that recommends supplements based on nutrient deficiencies. The system calculates deficiencies based on user input and suggests the best supplements to fulfill the deficiencies. Nutrient values are entered in grams, and the recommendations are based on daily recommended intakes.

## Features

- **User Input**: The user can input their age, and the amount of Iron, Vitamin D, and Calcium they have consumed (in grams).
- **Deficiency Calculation**: The application calculates how much of each nutrient is still needed to meet the recommended daily intake.
- **Supplement Recommendation**: Based on the deficiencies, the system recommends the most suitable supplement to meet the user's needs.

## Requirements

- Python 3.12+
- Flask
- Pandas
## Project Structure

```bash
supplement-recommendation-system/
│
├── templates/
│   └── index.html          # Main user input form
│
├── static/
│   └── style.css           # Basic styling for the web page (optional)
│
├── app.py                  # Flask application logic
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
└── .gitignore              # Git ignore file
```
## Output:



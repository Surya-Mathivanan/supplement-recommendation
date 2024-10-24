from flask import Flask, render_template, request
import pandas as pd
app = Flask(__name__)
recommended_daily = {'Iron': 18, 'Vitamin D': 20, 'Calcium': 1000}
recommended_df = pd.DataFrame(recommended_daily, index=[0])
supplement_data = {
    'Supplement': ['Iron Supplement', 'Vitamin D Supplement', 'Calcium Supplement'],
    'Iron (mg/g)': [50, 0, 0],  # Iron content per gram of supplement
    'Vitamin D (mcg/g)': [0, 100, 0],  # Vitamin D content per gram of supplement
    'Calcium (mg/g)': [0, 0, 1200]  # Calcium content per gram of supplement
}
supplement_df = pd.DataFrame(supplement_data)

# Function to calculate deficiencies
def calculate_deficiencies(user):
    deficiencies = recommended_df.values - user[['Iron', 'Vitamin D', 'Calcium']].values
    return pd.DataFrame(deficiencies, columns=['Iron', 'Vitamin D', 'Calcium'])

# Function to recommend supplements
def recommend_supplements(deficiency):
    supplement_scores = []
    for _, row in supplement_df.iterrows():
        total_iron = row['Iron (mg/g)']
        total_vitamin_d = row['Vitamin D (mcg/g)']
        total_calcium = row['Calcium (mg/g)']
        score = sum(min(deficiency.iloc[0, i], total_nutrient)
                    for i, total_nutrient in enumerate([total_iron, total_vitamin_d, total_calcium])
                    if total_nutrient > 0)
        supplement_scores.append(score)

    supplement_df['Deficiency Score'] = supplement_scores
    return supplement_df.sort_values(by='Deficiency Score', ascending=False)

@app.route("/", methods=["GET", "POST"])
def index():
    recommendation = None
    if request.method == "POST":
        age = int(request.form["age"])
        iron = float(request.form["iron"])
        vitamin_d = float(request.form["vitamin_d"])
        calcium = float(request.form["calcium"])
        user_data = {
            'Age': [age],
            'Iron': [iron],
            'Vitamin D': [vitamin_d],
            'Calcium': [calcium]
        }
        user_df = pd.DataFrame(user_data)
        user_deficiency = calculate_deficiencies(user_df)
        recommendations = recommend_supplements(user_deficiency)
        recommendation = recommendations.iloc[0]['Supplement']
    return render_template("index.html", recommendation=recommendation)

if __name__ == "__main__":
    app.run(debug=True)

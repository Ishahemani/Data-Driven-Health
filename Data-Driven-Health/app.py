from flask import Flask, request, render_template
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
import random 

app = Flask(__name__, template_folder='templates')

df = pd.read_csv('content/cancer1.csv')
df.drop(['Patient Id'], axis=1, inplace=True)

imputer = SimpleImputer(strategy='most_frequent')
df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

X = df_imputed.drop('Level', axis=1)
Y = df_imputed['Level']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.35, random_state=2)

model = RandomForestClassifier()
model.fit(X_train, Y_train)

@app.route('/')
def home():
    return render_template('index2.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict() 
    if data.get('healthIssue') == 'check':
        alcoholvalues = [
            int(data.get('drinkFrequency', 0)),
            int(data.get('drinkquestions',0))
        ]
        Alcoholuse = int(sum(alcoholvalues))

        question_values = [
            int(data.get('location', 0)),
            int(data.get('pollution', 0)),
            int(data.get('timeIndoors', 0)),
            int(data.get('modeTransportation', 0)),
            int(data.get('occupation', 0)),
            int(data.get('weather', 0)),
            int(data.get('activities', 0)),
        ]
        AirPollution = int(sum(question_values) / 3)

        geneticvalues = [
            int(data.get('familyCancer', 0)),
            int(data.get('ageonset', 0)),
            int(data.get('familyCancerType', 0)),
            int(data.get('multiplemember', 0)),
            int(data.get('familyCancerRelation', 0)),
            int(data.get('heriditycancer', 0)),
        ]
        GeneticRisk = int(sum(geneticvalues))

        asthamavalues = int(data.get('otherMedicalCondition', 0))
        random_number = random.randint(4,7)
        random_number1 = random.randint(1,3)
        if asthamavalues == 6 :
            chronicLungDisease = random_number
        else:
            chronicLungDisease = random_number1

        smokingvalues = [
            int(data.get('smoking', 0)),
            int(data.get('smokingDuration', 0)),
            int(data.get('smokingpack', 0))
        ]
        Smoking = int(sum(smokingvalues))

        passivesmoke = int(data.get('passivsmoker', 0))
        random_number2 = random.randint(5,8)
        random_number3 = random.randint(1,4)
        if passivesmoke == 6 :
            PassiveSmoker = random_number2
        else:
            PassiveSmoker = random_number3

        balancedvalues = [
            int(data.get('fruitVegetables', 0)),
            int(data.get('leanProtein', 0)),
            int(data.get('wholeGrains', 0)),
            int(data.get('dairyConsumption', 0)),
            int(data.get('sugarFats', 0)),
            int(data.get('waterConsumption', 0)),
            int(data.get('nutritionalDeficiencies', 0)),
            int(data.get('mealTime', 0))
        ]
        BalancedDiet = int(sum(balancedvalues))

        symptomvalues = [
            int(data.get('symptomschestpain', 0)),
            int(data.get('symptomscoughblood', 0)),
            int(data.get('symptomsfatigue', 0)),
            int(data.get('symptomsswallow', 0)),
            int(data.get('symptomsbreath', 0)),
            int(data.get('symptomswheezing', 0)),
            int(data.get('symptomscold', 0)),
            int(data.get('symptomscough', 0)),
            int(data.get('symptomsnone', 0))
        ]
        Symptoms = int(sum(symptomvalues))
        if Symptoms == 1:
            Symptoms = Symptoms + 1
        
        weight = int(data.get('weightLoss', 0))
        random_number4 = random.randint(5,8)
        random_number5 = random.randint(1,4)
        if weight == 6 :
            WeightLoss = random_number4
        else:
            WeightLoss = random_number5

        obesityvalues = [
            int(data.get('obesityHistory', 0)),
            int(data.get('obesityquestions', 0))
        ]
        Obesity = int(sum(obesityvalues))

        data['Age'] = int(data['age'])
        data['Gender'] = int(data['gender'])
        data['AirPollution'] = AirPollution
        data['Alcoholuse'] = Alcoholuse
        data['GeneticRisk'] = GeneticRisk
        data['chronicLungDisease'] = chronicLungDisease
        data['Smoking'] = Smoking
        data['PassiveSmoker'] = PassiveSmoker
        data['Symptoms'] = Symptoms
        data['WeightLoss'] = WeightLoss
        data['BalancedDiet'] = BalancedDiet
        data['Obesity'] = Obesity

        input_data = pd.DataFrame([data])
        input_data = input_data.reindex(columns=X_train.columns, fill_value=0)

        prediction = model.predict(input_data)
        
        if prediction == 'High':
            motivate = "You are not defined by a diagnosis, you are defined by your strength and resilience in the face of adversity."
            motivate2 = "Remember, you are not alone in this fight. Your loved ones, medical team, and community are here to support you every step of the way."
            motivate3 = "Take care, we believe in you."
        elif prediction == 'Medium':
            motivate = "You are not defined by a diagnosis, you are defined by your strength and resilience in the face of adversity."
            motivate2 = "Remember, you are not alone in this fight. Your loved ones, medical team, and community are here to support you every step of the way."
            motivate3 = "Take care, we believe in you."
        else:
            motivate = "Every step you take towards your health is victory, regardless of the outcome. You are taking control and that is incredibly empowering."
            motivate2 = "Regardless of what lies ahead remember that you are capable and deserving of a healthy and fulfilling life. Let's face your fears together and emerge stronger on the other side."
            motivate3 = "Take care, You're alright."
            
        return render_template('result.html', prediction=prediction[0], motivate=motivate, motivate2=motivate2, motivate3=motivate3)
    
    else:
        medicine_data = pd.read_csv("content/meds2.csv")
        cancer_type = request.form['cancerType']
        diabetes_status = request.form['diabetes']
        
        relevant_medicine = medicine_data[(medicine_data['Cancer_Type'] == cancer_type) & (medicine_data['Diabetes'] == diabetes_status)]
    return render_template('medicine.html', medicine=relevant_medicine)

if __name__ == '__main__':
    app.run(debug=True)

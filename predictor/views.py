from django.shortcuts import render
from django import forms
import pickle
import pandas as pd

class PredictionForm(forms.Form):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ]
    SMOKING_CHOICES = [
        ('not current', 'Not Current'),
        ('former', 'Former'),
        ('No Info', 'No Info'),
        ('current', 'Current'),
        ('never', 'Never'),
        ('ever', 'Ever')
    ]
    
    gender = forms.ChoiceField(choices=GENDER_CHOICES, label='Gender')
    age = forms.IntegerField(label='Age', min_value=0, max_value=80)
    hypertension = forms.ChoiceField(choices=[(0, 'No'), (1, 'Yes')], label='Hypertension')
    heart_disease = forms.ChoiceField(choices=[(0, 'No'), (1, 'Yes')], label='Heart Disease')
    smoking_history = forms.ChoiceField(choices=SMOKING_CHOICES, label='Smoking History')
    bmi = forms.FloatField(label='BMI', min_value=10.16, max_value=71.55)
    HbA1c_level = forms.FloatField(label='HbA1c Level', min_value=0, max_value=20)
    blood_glucose_level = forms.FloatField(label='Blood Glucose Level')

def predict(request):
    form = PredictionForm()
    prediction = None

    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            try:
                model = pickle.load(open('best_CatBoost_model.pkl', 'rb'))

                # Prepare data for prediction
                form_data = {
                    'gender': [form.cleaned_data['gender']],
                    'age': [int(form.cleaned_data['age'])],
                    'hypertension': [int(form.cleaned_data['hypertension'])],
                    'heart_disease': [int(form.cleaned_data['heart_disease'])],
                    'smoking_history': [form.cleaned_data['smoking_history']],
                    'bmi': [form.cleaned_data['bmi']],
                    'HbA1c_level': [form.cleaned_data['HbA1c_level']],
                    'blood_glucose_level': [form.cleaned_data['blood_glucose_level']]
                }
                data = pd.DataFrame(form_data)

                prediction_result = model.predict(data)
                prediction = 'Diabetes' if prediction_result[0] == 1 else 'No Diabetes'

            except Exception as e:
                prediction = f"Error: {str(e)}"

    return render(request, 'predictor/form.html', {'form': form, 'prediction': prediction})

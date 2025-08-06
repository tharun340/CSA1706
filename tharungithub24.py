class DietAdvisor:
    def __init__(self):
        self.diet_plans = {
            'diabetes': 'Low sugar, high fiber diet',
            'hypertension': 'Low sodium, DASH diet',
            'obesity': 'Low calorie, balanced diet with exercise',
            'celiac': 'Gluten-free diet',
            'anemia': 'Iron-rich diet with vitamin C',
            'hyperthyroidism': 'Balanced diet with adequate calories',
            'hypothyroidism': 'High fiber, low calorie diet',
            'gout': 'Low purine diet',
            'cholesterol': 'Low saturated fat, high fiber diet'
        }

    def suggest_diet(self, disease):
        disease_lower = disease.lower()
        if disease_lower in self.diet_plans:
            return self.diet_plans[disease_lower]
        else:
            return 'No specific diet found. Consult a nutritionist.'
advisor = DietAdvisor()

print(advisor.suggest_diet('Diabetes'))       
print(advisor.suggest_diet('gout'))         
print(advisor.suggest_diet('Flu'))            

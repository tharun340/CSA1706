class MedicalDiagnosis:
    def __init__(self):
        self.disease_symptoms = {
            'flu': {'fever', 'cough', 'headache', 'fatigue'},
            'cold': {'cough', 'sneezing', 'sore_throat'},
            'malaria': {'fever', 'chills', 'sweating', 'headache'},
            'dengue': {'fever', 'headache', 'rash', 'joint_pain'}
        }

    def diagnose(self, symptoms):
        """
        Return list of diseases for which all symptoms are present.
        :param symptoms: iterable of symptoms (strings)
        :return: list of matching diseases
        """
        symptoms_set = set(symptoms)
        matching_diseases = []
        for disease, disease_symptoms in self.disease_symptoms.items():
            if symptoms_set.issubset(disease_symptoms):
                matching_diseases.append(disease)
        return matching_diseases
if __name__ == "__main__":
    md = MedicalDiagnosis()

    symptoms_to_check = ['fever', 'headache']
    matches = md.diagnose(symptoms_to_check)

    if matches:
        print(f"Diseases matching symptoms {symptoms_to_check}: {matches}")
    else:
        print(f"No diseases found matching symptoms {symptoms_to_check}.")

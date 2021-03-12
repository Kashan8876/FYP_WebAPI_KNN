from flask import Flask , jsonify , request
import pickle
import json





app = Flask(__name__)

Symptoms = ['Select Symptom','back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
    'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach','weight_gain','breathlessness',
    'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation','sunken_eyes',
    'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs','lethargy',
    'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool','fatigue','nausea','itching',
    'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs','anxiety','high_fever',
    'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails','spotting_ urination','dehydration',
    'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips','restlessness',
    'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints','sweating','indigestion',
    'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness','joint_pain','ulcers_on_tongue','loss_of_appetite',
    'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine','acidity','burning_micturition',
    'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_typhos','stomach_pain','cough','dark_urine',
    'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain','vomiting','headache',
    'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
    'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion','muscle_wasting','irregular_sugar_level',
    'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen','continuous_sneezing','weight_loss','yellowish_skin',
    'history_of_alcohol_consumption','blood_in_sputum','prominent_veins_on_calf','shivering','chills','cold_hands_and_feets','pain_behind_the_eyes',
    'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling','skin_rash','nodal_skin_eruptions',
    'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose','mood_swings','patches_in_throat',
    'yellow_crust_ooze']


        

@app.route('/post', methods=['POST','GET'])
def main():


    with open('KNN_FYP.pkl','rb') as f:

         clf = pickle.load(f)
	
    Symptom1 = request.form.get('Symptom1',Symptoms)
    Symptom2 = request.form.get('Symptom2',Symptoms)
    Symptom3 = request.form.get('Symptom3',Symptoms)
    Symptom4 = request.form.get('Symptom4',Symptoms)
    Symptom5 = request.form.get('Symptom5',Symptoms)
    Symptom6 = request.form.get('Symptom6',Symptoms)
    Symptom7 = request.form.get('Symptom7',Symptoms)
    Symptom8 = request.form.get('Symptom8',Symptoms)
    Symptom9 = request.form.get('Symptom9',Symptoms)
    Symptom10 = request.form.get('Symptom10',Symptoms)
    Symptom11 = request.form.get('Symptom11',Symptoms)
    Symptom12 = request.form.get('Symptom12',Symptoms)
    Symptom13 = request.form.get('Symptom13',Symptoms)
    Symptom14 = request.form.get('Symptom14',Symptoms)
    Symptom15= request.form.get('Symptom15',Symptoms)
    
    
    l2=[]
    for i in range(0,len(Symptoms)):


        l2.append(0)

    psymptoms = [Symptom1,Symptom2,Symptom3,Symptom4,Symptom5,Symptom6,Symptom7,Symptom8,Symptom9,Symptom10,Symptom11,Symptom12,Symptom13,Symptom14,Symptom15]
    for k in range(0,len(Symptoms)):
            for z in psymptoms:
                if(z==Symptoms[k]):

                    l2[k]=1

    inputtest = [l2]
    

    
    result = clf.predict(inputtest)
    

    return jsonify({'Disease': list(result)})

    
if __name__ == '__main__':
	app.run(debug=True) 













   



    



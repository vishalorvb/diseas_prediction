from django.shortcuts import render
import joblib

# Create your views here.
def home(request):
    return render(request,"home.html")

def result(request):
    model1 = joblib.load('finalized_model_1.sav')
    model2 = joblib.load('finalized_model_2.sav')
    model3 = joblib.load('finalized_model_3.sav')

    symptoms = []
    ans = dict()
    symptoms.append(request.POST['s1'])
    symptoms.append(request.POST['s2'])
    symptoms.append(request.POST['s3'])
    symptoms.append(request.POST['s4'])
    symptoms.append(request.POST['s5'])
    l1=['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
    'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
    'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
    'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
    'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
    'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
    'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
    'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
    'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
    'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
    'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
    'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
    'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
    'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
    'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
    'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
    'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
    'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
    'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
    'yellow_crust_ooze']

    l2=[]
    for i in range(0,len(l1)):
        l2.append(0)

    for k in range(0,len(l1)):
        for z in symptoms:
            if(z==l1[k]):
                l2[k]=1

    disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
    'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
    ' Migraine','Cervical spondylosis',
    'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
    'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
    'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
    'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
    'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
    'Impetigo']

    h='no'

    predicted1 = model1.predict([l2])
    predicted1 = predicted1[0]
    for a in range(0,len(disease)):
        if(predicted1 == a):
            h='yes'
            break

    if (h=='yes'):
        ans['Decision Tree'] = disease[a]
    else:
        ans['Decision Tree'] = "Not Found"

    # h = 'no'    
    # predicted1 = model2.predict([l2])
    # for a in range(0,len(disease)):
    #     if(predicted == a):
    #         h='yes'
    #         break

    # if (h=='yes'):
    #     ans['RandomForest '] = disease[a]
    # else:
    #     ans['RandomForest '] = "Not Found"
    
    h = 'no'
    predicted2 = model3.predict([l2])
    for a in range(0,len(disease)):
        if(predicted2 == a):
            h='yes'
            break

    if (h=='yes'):
        ans['Navie Bayes'] = disease[a]
    else:
        ans['Navie Bayes'] = "Not Found"
    #print(ans)
    return render(request,"result.html",{"ans":ans})
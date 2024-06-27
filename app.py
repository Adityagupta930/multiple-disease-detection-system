# from flask import Flask, render_template, request
# import pickle
# import numpy as np
# import datetime

# app = Flask(__name__)

# # Load models
# loaded_model = pickle.load(open("models/diabetes_model.sav", 'rb'))
# loaded_model2 = pickle.load(open("models/heart_disease_model.sav", 'rb'))
# loaded_model3 = pickle.load(open("models/Covid_disease_detection_using_symptoms_model.sav", 'rb'))
# loaded_model4 = pickle.load(open("models/Lung_cancer_using_symptoms_model.sav", 'rb'))

# @app.route('/')
# def welcome():
#     return render_template('Home.html')

# @app.route('/symptom', methods=['GET', 'POST'])
# def going_to_symptom():
#     return render_template('symptoms.html')

# @app.route('/diabetis', methods=['GET', 'POST'])
# def d():
#     return render_template('diabetis.html')

# @app.route('/submit_diabetis', methods=['POST'])
# def diabetis():
#     print("invoked diabetis function \n\n\n\n")
#     l = [str(i) for i in request.form.values()]

#     name = l.pop(0)
#     gender = l.pop(0)
#     dob = l.pop(0)
#     age = int(l.pop(0))
#     mobile = l.pop(0)
#     add = l.pop(0)
#     name_list = [float(l[x]) for x in range(len(l))]
#     name_list.append(float(age))
#     result = diabetis_prediction(name_list)
#     return render_template(
#         "result.html", 
#         res_ans=result, 
#         names_ans=name, 
#         sex_ans=gender, 
#         dob_ans=dob, 
#         age_ans=age, 
#         mobile_ans=mobile, 
#         date_ans=str(datetime.date.today()), 
#         address_ans=add
#     )

# def diabetis_prediction(input_data):
#     input_data_as_numpy_array = np.asarray(input_data)
#     input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
#     prediction = loaded_model.predict(input_data_reshaped)
#     print(prediction)
    
#     if prediction[0] == 0:
#         return 'The person is not diabetic'
#     else:
#         return 'The person is diabetic'

# @app.route('/covid', methods=['GET', 'POST'])
# def cv():
#     return render_template('covid.html')
# @app.route('/covid_symptoms' ,methods=['POST'])
# def covid():
#     # print("invoked diabetis function \n\n\n\n")
#     l = [str(i) for i in request.form.values()]

#     name = l.pop(0)
#     gender = l.pop(0)
#     dob = l.pop(0)
#     age = int(l.pop(0))
#     mobile = l.pop(0)
#     add = l.pop(0)
#     name_list = [float(l[x]) for x in range(len(l))]
#     name_list.append(float(age))
#     result = covid_prediction(name_list)
#     return render_template(
#         "result.html", 
#         res_ans=result, 
#         names_ans=name, 
#         sex_ans=gender, 
#         dob_ans=dob, 
#         age_ans=age, 
#         mobile_ans=mobile, 
#         date_ans=str(datetime.date.today()), 
#         address_ans=add
#     )
# def covid_prediction(input_data):
#     input_data_as_numpy_array = np.asarray(input_data)
#     input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
#     prediction = loaded_model.predict(input_data_reshaped)
#     print(prediction)

#     if prediction[0] == 0:
#         return 'The person is not Covid 19 '
#     else:
#         return 'The person is covid'


# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template, request
import pickle
import numpy as np
import datetime

app = Flask(__name__)
# loaded_model = pickle.load(open("models/diabetes_model.sav", 'rb'))
# loaded_model2 = pickle.load(open("models/heart_disease_model.sav", 'rb'))
# loaded_model3 = pickle.load(open("models/Covid_disease_detection_using_symptoms_model.sav", 'rb'))
# loaded_model4 = pickle.load(open("models/Lung_cancer_using_symptoms_model.sav", 'rb'))
diabetis_model = pickle.load(open(r"models/diabetes_model.sav", 'rb'))
covid_model = pickle.load(open(r"models/Covid_disease_detection_using_symptoms_model.sav", 'rb'))
lungs_model = pickle.load(open(r"models/Lung_cancer_using_symptoms_model.sav", 'rb'))
heart_model = pickle.load(open(r"models/heart_disease_model.sav", 'rb'))

@app.route('/')
def welcome():
    return render_template('Home.html')

@app.route('/symptom', methods=['GET', 'POST'])
def going_to_symptom():
    return render_template('symptoms.html')


@app.route('/diabetis',methods=['GET','POST'])
def d():
    return render_template('diabetis.html')

@app.route('/submit_diabetis' ,methods=['POST'])
def diabetis():
    l=[str(i) for i in request.form.values()]
    # print("\n\n\n\n\n\n\n\n")
    # print(l)
    name=l.pop(0)
    gender=l.pop(0)
    dob=l.pop(0)
    age=int(l.pop(0))
    mobile=l.pop(0)
    add=l.pop(0)
    name_list=[float(l[x]) for x in range(len(l))]
    name_list.append(float(age))
    result=diabetis_prediction(name_list)
    return render_template("result.html",res_ans=result,names_ans=name,sex_ans=gender,dob_ans=dob,age_ans=age,mobile_ans=mobile,date_ans=str(datetime.date.today()),address_ans=add)

def diabetis_prediction(input_data):
	input_data_as_numpy_array = np.asarray(input_data)
    
	input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    

	prediction = diabetis_model.predict(input_data_reshaped)
	print(prediction)
    
	if (prediction[0] == 0):
		return 'The person is not diabetic'
	else:
		return 'The person is diabetic'
@app.route('/covid')
def cv():
    return render_template('covid.html')

@app.route('/submit_covid' ,methods=['POST'])
# def covid():
#     l=[str(i) for i in request.form.values()]
#     # print("\n\n\n\n\n\n\n\n")
#     # print(l)
#     name=l.pop(0)
#     gender=l.pop(0)
#     dob=l.pop(0)
#     age=int(l.pop(0))
#     mobile=l.pop(0)
#     add=l.pop(0)
#     name_list=[float(l[x]) for x in range(len(l))]
#     name_list.append(float(age))
#     result=covid_prediction(name_list)
#     return render_template("result.html",res_ans=result,names_ans=name,sex_ans=gender,dob_ans=dob,age_ans=age,mobile_ans=mobile,date_ans=str(datetime.date.today()),address_ans=add)
def covid_symp():
    l=[i for i in request.form.values()]
  
    name=l.pop(0)
    gender=l.pop(0)
    dob=l.pop(0)
    age=int(l.pop(0))
    mobile=l.pop(0)
    add=l.pop(0)
    name_list=[int(i) for i in l]
    result=covid_prediction(name_list)
    return render_template("result.html",res_ans=result,names_ans=name,sex_ans=gender,dob_ans=dob,age_ans=age,mobile_ans=mobile,date_ans=str(datetime.date.today()),address_ans=add)
    

def covid_prediction(input_data):
    input_data_as_numpy_array=np.asarray(input_data)
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
    prediction=covid_model.predict(input_data_reshaped)
    if(prediction[0]==0):
        return 'The person does not have covid'
    else:
        return 'The person has covid disease'
    
@app.route('/lung' ,methods= ["GET","POST"])
def lungs():
    return render_template('lung.html')    
@app.route('/submit_lungs' ,methods= ["POST"])
def lung_sym():
    l=[i for i in request.form.values()]
    name= l.pop(0)
    gender= l.pop(0)
    dob= l.pop(0)
    age= int(l.pop(0))
    
    
    mobile= l.pop(0)
    add= l.pop(0)
    name_list= [int(i) for i in l]
    result= lung_prediction(name_list)
    return render_template("result.html",res_ans=result,names_ans=name,sex_ans=gender,dob_ans=dob,age_ans=age,mobile_ans=mobile,date_ans=str(datetime.date.today()),address_ans=add)


def lung_prediction(input_data):
    input_data_as_numpy_array=np.asarray(input_data)
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
    prediction=lungs_model.predict(input_data_reshaped)
    if(prediction[0]==0):
        return 'The person does not have covid'
    else:
        return 'The person has covid disease'
    
@app.route('/heart' ,methods= ["GET","POST"])
def hearts():
    return render_template('heart.html')    
@app.route('/submit_heart' ,methods= ["POST"])
def heart_sym():
    l=[i for i in request.form.values()]
    name= l.pop(0)
    gender= l.pop(0)
    dob= l.pop(0)
    age= int(l.pop(0))
    
    
    mobile= l.pop(0)
    add= l.pop(0)
    name_list= [int(i) for i in l]
    result= heart_prediction(name_list)
    return render_template("result.html",res_ans=result,names_ans=name,sex_ans=gender,dob_ans=dob,age_ans=age,mobile_ans=mobile,date_ans=str(datetime.date.today()),address_ans=add)


def heart_prediction(input_data):
    input_data_as_numpy_array=np.asarray(input_data)
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
    prediction=heart_model.predict(input_data_reshaped)
    if(prediction[0]==0):
        return 'The person does not have covid'
    else:
        return 'The person has covid disease'


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask ,render_template,request
import joblib
app=Flask(__name__)
reg=joblib.load("reg.h5")
scalar=joblib.load("scalar.h5")
bm={"=bm1":[1,0,0,0,0,0],"=bm2":[0,1,0,0,0,0],"=bm3":[0,0,1,0,0,0],"=bm4":[0,0,0,1,0,0],"=bm5":[0,0,0,0,1,0],"=bm6":[0,0,0,0,0,1]}
ins={"=in1":[1,0],"=in2":[0,1]}
gl={"gl1":[1,0,0,0],"gl2":[0,1,0,0],"gl3":[0,0,1,0],"gl4":[0,0,0,1]}
@app.route('/',methods=['Get'])
def home():
    return render_template('index.html')

@app.route('/predict',methods=['Get'])
def predict():
    data=[ int(request.args['Pregnancies']),

    int(request.args['Glucose']),
    
    int(request.args["BloodPressure"]),
    int(request.args["SkinThickness"]),
    int(request.args["Insulin"]),
    
    int(request.args["BMI"]),
    
    int(request.args["DiabetesPedigreeFunction"]),
    int(request.args["Age"])
    ]
    data+=[i for i in ins[request.args["in"]]]
    data+=[i for i in gl[request.args['gl']]]
    data+=[i for i in bm[request.args["bm"]]]
    regrssion=reg.predict(scalar.transform([data]))
    x=1
    if regrssion==1:
        x=str(regrssion)+" you have diabetes "
    else:
        x=str(regrssion)+" you Ok"    
    

    return render_template ('result.html',profit=x)

if __name__ =='__main__':
    app.run(debug=True)
    
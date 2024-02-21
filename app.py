







from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
std=StandardScaler()

app = Flask(__name__)


model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    bedrooms = request.form["Bedrooms"]
    bathrooms = request.form["bathrooms"]
    sqft_living = request.form["sqft_living"]
    sqft_lot = request.form["sqft_lot"]
    floors = request.form["floors"]
    waterfront = request.form["waterfront"]
    view = request.form["view"]
    condition = request.form["condition"]
    grade = request.form["grade"]
    sqft_above = request.form["sqft_above"]
    sqft_basement = request.form["sqft_basement"]
    sqft_living15 = request.form["sqft_living15"]
    sqft_lot15 = request.form["sqft_lot15"]
    final=[[bedrooms,bathrooms,sqft_living,sqft_lot,floors,waterfront,view,condition,grade,sqft_above,sqft_basement,sqft_living15,sqft_lot15 ]]
    #print(int_features)
    print(final)
    #final_std=std.fit_transform(final)
   #print(final_std)
    #prediction=
    #output='{0:.{1}f}'.format(prediction[0],0)
    return render_template('index.html',pred='Predicted  House Price is : ${}'.format(int(model.predict(final))))
    final=0
    
   


if __name__ == '__main__':
    app.run(debug=True)






































#from flask import Flask,request, url_for, redirect, render_template
#import pickle
#import numpy as np
#from sklearn.preprocessing import StandardScaler
#std=StandardScaler()

#app = Flask(__name__)

#model=pickle.load(open('model.pkl','rb'))


#@app.route('/')
#def home():
#    return render_template("index.html")


#@app.route('/predict',methods=['POST','GET'])
#def predict():
#    int_features=[int(x) for x in request.form.values()]
#    final_std=[np.array(int_features)]
#    print(int_features)
    #print(final)
    #final_std=std.fit_transform(final)
 #   print(final_std)
 #   prediction=model.predict(final_std)
 #   output='{0:.{1}f}'.format(prediction[0],0)
 #   return render_template('index.html',pred='Predicted  House Price is : ${}'.format(output))
   


#if __name__ == '__main__':
    #app.run(debug=True)

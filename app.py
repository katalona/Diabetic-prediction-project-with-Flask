from flask import Flask, request, render_template
import pickle
import numpy as np
app = Flask("__name__")

q = ""

def conditions(query1, query2, query3, query4, query5, query6, query7, query8):
  check1 = all([query1.isdigit(), int(query1) in [0, 1, 2]])
  check2 = all([query2.isdigit(), query6.isdigit(), query7.isdigit(), query8.isdigit()])
  check3 = all([query3.isdigit(), int(query3) in range(2)])
  check4 = all([query4.isdigit(), int(query3) in range(2)])
  check5 = all([query5.isdigit(), int(query3) in range(6)])
  return all([check1, check2, check3, check4, check5])
    

@app.route("/")
def loadPage():
  return render_template('home.html', query="")

@app.route("/predict", methods=['POST'])
def predict():
  inputQuery1 = request.form['query1']
  inputQuery2 = request.form['query2']
  inputQuery3 = request.form['query3']
  inputQuery4 = request.form['query4']
  inputQuery5 = request.form['query5']
  inputQuery6 = request.form['query6']
  inputQuery7 = request.form['query7']
  inputQuery8 = request.form['query8']
  
  ml_model = pickle.load(open('model_SVC_0.2.pkl', 'rb'))
  if conditions(inputQuery1, inputQuery2, inputQuery3, inputQuery4, inputQuery5, inputQuery6, inputQuery7, inputQuery8):
    data = [[inputQuery1, inputQuery2, inputQuery3, inputQuery4, inputQuery5, inputQuery6, inputQuery7, inputQuery8]]
    pred = ml_model.predict(data)
    if pred == 0:
      result = 'Диабета нет'
    else:
      result = 'Диабет есть'
  else:
    result = f'Вы ввели неверные данные\nПерепроверьте данные'
  
  return render_template('home.html', output1=result, query1=request.form['query1'], query2=request.form['query2'], query3=request.form['query3'], query4=request.form['query4'], query5=request.form['query5'], query6=request.form['query6'], query7=request.form['query7'], query8=request.form['query8'])


if __name__ == "__main__":
    app.run(port=5000)

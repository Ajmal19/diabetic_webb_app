from keras.models import load_model
from flask import Flask, render_template, request


app = Flask('mywebapp')

model = load_model('/ws_webapp/Dia_Model80.h5')

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/output', methods= ['GET'])
def web_app():
    n1 =  request.args.get('preg')
    n2 =  request.args.get('glucose')
    n3 =  request.args.get('bp')
    n4 =  request.args.get('tricep')
    n5 =  request.args.get('insulin')
    n6 =  request.args.get('bmi')
    n7 =  request.args.get('dpf')
    n8 =  request.args.get('age')
    predict_value = model.predict([[int(n1), int(n2), int(n3), int(n4), int(n5), float(n6), float(n7), int(n8)]])
    #return (str(round(predict_value[0][0])))
    output_c = str(round(predict_value[0][0]))
    return render_template('output.html', result=output_c)


app.run(host='172.17.0.2' , port=1234)



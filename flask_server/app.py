from flask import Flask, render_template, request
import requests
import  json
import numpy as np
import os
from werkzeug.utils import secure_filename
from tensorflow.keras.preprocessing import image
from datetime import datetime

IMAGE_FOLDER = os.path.join('static', 'image')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files["image"]
        filename = secure_filename(file.filename)
        filename = filename+'_'+datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        img = image.img_to_array(image.load_img(filepath,
                                            target_size=(300,300)))
        img = np.expand_dims(img, axis =0)
        images= np.vstack([img])
        data = {"signature_name": "serving_default", "instances": images.tolist()}
        json_data = json.dumps(data)
        headers = {"content-type": "application/json"}
        json_response = requests.post('http://localhost:8501/v1/models/covid:predict', data=json_data, headers=headers)
        print(json_response.json())
        predictions = json.loads(json_response.text)['predictions']
        for i in predictions[0]:
            if i<0.5:
                res = "COVID Pneumonia Negative"
            else:
                res = "COVID Pneumonia Positive"
    
    return render_template('index.html',prediction_text=res, image=filepath)

if __name__=="__main__":
    app.run(debug=True)
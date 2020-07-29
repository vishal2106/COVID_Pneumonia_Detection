# COVID Pneumonia Prediction
A project using tensorflow model to train X ray images and identify if the person has COVID pneumonia or not (Go under notebook/ to checkout the .ipyng notebook for more details on training). The model is then used to serve client requests for predictions using TF-serving and flask.

### Tech
* [Flask] - Used to process the input and render output to the client
* [Tensorflow] - Used CNN architecture to train weights for X-ray images, also used TF-serving so that it's easy to make version control of model and any change in model is not affected in client's code.
* [Docker] - Used to serve tensorflow model for predictions

### Architecture
![GitHub Logo](/readme_images/architecture.png)

### Try it out

```sh
$ git clone https://github.com/vishal2106/COVID_Pneumonia_Detection.git
$ cd COVID_Pneumonia_Detection
$ cd flask_server
$ pip install -r requirements
$ python app.py
```
## In another terminal run the tensorflow image (Make sure you have docker installed)
```sh
$ cd COVID_Pneumonia_Detection
$ sudo bash serving.sh
```
### Go to localhost:5000 in your browser to try out the app

### Todos

 - Improve UI using React.js
 - Work on docker-compose to make it production ready


   

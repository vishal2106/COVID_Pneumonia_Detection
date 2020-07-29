sudo docker run -p 8501:8501 --mount type=bind,source="$(pwd)"/tmp/,target=/models/covid -e MODEL_NAME=covid -t tensorflow/serving

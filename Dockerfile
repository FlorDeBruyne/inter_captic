FROM python:3.8-slim
WORKDIR /app
RUN apt-get update && apt-get install -y libgl1-mesa-glx  libglib2.0-0

COPY afbeelding_metadata.py .
RUN pip install --upgrade pip
RUN pip install opencv-contrib-python
CMD ["python", "afbeelding_metadata.py"]
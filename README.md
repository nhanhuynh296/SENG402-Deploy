# Retinal images quality assurance
----
Automated computer vision methods, particularly of fundus images for diabetic retinopathy diagnosis, have been
explored for many years, but without success to-date. Nevertheless, the advent of “deep-learning” techniques now
appears to offer significant promise for fundus images.

## Models

Different deep learning models are in `server/static/*.h5`. The golden models are using the annotated images labelled by
a professional
The model `model_full.h5` are annotated by a large (~20000) image dataset by Chen He which yielded the best result out
of all models.

## Client

Developed using Vue 3.0 with vuetify.

```shell
cd client
npm install
npm run serve
```

## Server

Developed using Flask as it is in Python which conveniently serve as a run time for our hosted model.

### Creating new environment and install dependencies

```shell
python3 -m venv venv
source /venv/bin/activate
# Installing requirements
pip3 install -r requirements.txt
```

### Run app

```shell
python3 -m run
```
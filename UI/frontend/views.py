import pickle
import re
from tensorflow.keras.models import load_model
from django.shortcuts import render
from django.http import HttpResponse
from . import utils
COLORS = {
    'spam': 'bg-danger',
    'ham': 'bg-primary',
    'social': 'bg-success',
    'promotion': 'bg-info',
}

VECTORIZER = pickle.load(open('models/vectorizer.pkl', 'rb'))
ENCODER = pickle.load(open('models/encoder.pkl', 'rb'))
SVM_MODEL = pickle.load(open('models/model.pkl', 'rb'))


def index(request):
    return render(request, template_name='UI/templates/index.html')


def predict(request):
    if request.method == 'POST':
        email = request.POST['email'].lower()
        email = re.sub(r'[^a-z\s]', ' ', email)
        email = re.sub(r'\s+', ' ', email)
        email = utils.stem(email)
        print(email)
        x = VECTORIZER.transform([email])
        svm_pred = SVM_MODEL.predict(x)[0]
        x = x.toarray().reshape(1, -1, 1)

        LSTM_MODEL = load_model('./models/model.h5')
        pred = LSTM_MODEL.predict_classes(x)
        lstm_pred = ENCODER.inverse_transform(pred)[0]
        print(lstm_pred[0])
        return render(request,
                      template_name='UI/templates/predictions.html',
                      context={
                          'svm': svm_pred.title(),
                          'lstm': lstm_pred.title(),
                          'svm_color': COLORS[svm_pred],
                          'lstm_color': COLORS[lstm_pred],
                          'email': email
                      })
    return HttpResponse('Error 404')

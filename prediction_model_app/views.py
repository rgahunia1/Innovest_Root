from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from datetime import date

from django.contrib import messages
from django.contrib.auth.models import User , auth
from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.views import APIView
from prediction_model_app.services.prediction import Prediction
from prediction_model_app.services.training import Training 

#from .models import patient , doctor , diseaseinfo , consultation ,rating_review
#from chats.models import Chat,Feedback

# Create your views here.


#loading trained_model
#import joblib as jb
#model = jb.load('trained_model')

def home(request):

  if request.method == 'GET':
        
      if request.user.is_authenticated:
        return render(request,'homepage/index.html')

      else :
        return render(request,'homepage/index.html')


class TrainChurnModelView(APIView): 
    def get(self,request):
        train_obj=Training()
        response_dict=train_obj.train(request)
        response=response_dict['response']
        status_value=response_dict['status']
        return Response(response,status_value)

class PredChurnModelView(APIView): 
    def post(self,request):
        pred_obj=Prediction()
        response_dict=pred_obj.predict(request)
        response=response_dict['response']
        status_value=response_dict['status']
        return Response(response,status_value)

# Create your views here.
def sofi_ui(request):

    if request.method == 'GET':

      doctorid = request.session['sofiusername']
      duser = User.objects.get(username=doctorid)

    
      return render(request,'sofi/sofi_ui/profile.html',{"duser":duser})


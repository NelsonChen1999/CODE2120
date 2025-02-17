
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from .models import *
import os, sys
from tkinter import *
import math

# Create your views here.

@csrf_exempt
def ligma(request):
	log = []
	#jsob = {"topLeft": 50, "bottomRight": 250}
	jsob = {"shape": "circle", "radius": 7}
	if request.method == "POST":
		try:
			data = request.POST["data"]
			received = json.loads(data)
			jsob.update(received)

			shape = str(jsob["shape"])
			r = int(jsob["radius"])
			shape.lower()
			if shape == "circle":
				a = math.pi*r*r
			elif shape == "sphere":
				a = 4*math.pi*r*r
			elif shape =="circumference":
				a = 2*math.pi*r

			return JsonResponse({"Area":a})
		
		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			other = sys.exc_info()[0].__name__
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			errorType = str(exc_type)
			return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
	else:
		#return HttpResponse("ONLY POST REQUESTS")

		return JsonResponse(jsob)
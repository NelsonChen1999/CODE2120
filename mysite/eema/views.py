
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from .models import *
import os,sys
from tkinter import *

# Create your views here.

@csrf_exempt
def shape(request):
	log = []
	jsob = {"number": 12, "index": 2}
	if request.method == "POST":
		try:
			data = request.POST["data"]
			received = json.loads(data)
			jsob.update(received)

			'''topLeft = int(jsob["topLeft"])
			bottomRight = int(jsob["bottomRight"])

			root = Tk()
			root.geometry('300x300')

			c = Canvas (root, height=300, width=300, bg='white')

			l = c.create_line(topLeft, topLeft, bottomRight, bottomRight)

			c.pack()

			root.mainloop()'''

			number = int(jsob["number"])
			index = int(jsob["index"])

			



		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			other = sys.exc_info()[0].__name__
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			errorType = str(exc_type)
			return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
	else:
		#return HttpResponse("ONLY POST REQUESTS")

		return JsonResponse(jsob)
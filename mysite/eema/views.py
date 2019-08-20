from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from .models import *
import os,sys
from tkinter import Tk, Canvas, Frame, BOTH

# Create your views here.

@csrf_exempt
def shape(request):
	log = []
	jsob = {"startNumber": 0, "length": 10}
	if request.method == "POST":
		try:
			data = request.POST["data"]
			recieved = json.loads(data)
			jsob.update(recieved)

			class Example(Frame):

				def __init__(self):
					super().__init__()

					self.initUI()

				def initUI(self):

					self.master.title("Shapes")
					self.pack(fill=BOTH, expand=1)

					canvas = Canvas(self)
					canvas.create_oval(10, 10, 80, 80, outline='black', fill='red', width=5

					canvas.pack(fill=BOTH, expand=1)

			def main():

				root = Tk()
				ex = Example()
				root.geometry("330x220+300+300")
				root.mainloop()

			if __name__ == '__main__':
				main()
			

			return JsonResponse({'shape': numarray})
		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			other = sys.exc_info()[0].__name__
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			errorType = str(exc_type)
			return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
	else:
		return HttpResponse("ONLY POST REQUESTS")

		#return JsonResponse(jsob)
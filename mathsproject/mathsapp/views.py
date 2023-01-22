from django.shortcuts import render

# Create your views here.
def mathsoperation(request):
    return render(request, "mathsoperation.html")

def clac(request):
    x = int(request.GET['num1'])
    y = int(request.GET['num2'])
    res = x+y
    less = x-y
    pro = x*y
    quo=x/y
    return render(request, "result.html", {'result': res,
                  'result1': less,'result2': pro,'result3': quo})

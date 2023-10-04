from django.shortcuts import render

# Create your views here.
def RosWebUI(request):
    return render(request, 'RosWebApp/index.html')
from django.shortcuts import render,HttpResponse
from .models import FileUpload

# Create your views here.
def home(request):
    if request.method=="POST":
        file2=request.FILES['upload']
        document=FileUpload.objects.create(file=file2)
        document.save()
        return HttpResponse("Your file uploaded")
    return render(request,"index.html")

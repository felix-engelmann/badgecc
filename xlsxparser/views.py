from django.shortcuts import render
from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField(label='xlsx Dokument')
    #submit = forms.SubmitField(label='hochladen')

# Create your views here.

def index(request):
    #return render(request, "parser/index.html")
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form = request.FILES['file']
        else:
            return render(request,"parser/index.html",{'form': form})
    else:
        form = UploadFileForm()
        return render(request,"parser/index.html",{'form': form})
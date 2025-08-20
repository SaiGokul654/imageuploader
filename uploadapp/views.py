from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Image

def upload(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')
    else:
        form = ImageForm()
    return render(request, 'upload.html', {'form': form})

def gallery(request):
    images = Image.objects.all()
    return render(request, 'gallery.html', {'images': images})

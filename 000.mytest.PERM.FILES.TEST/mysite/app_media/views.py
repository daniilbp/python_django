from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from app_media.forms import UploadFileForm, DocumentForm, MultiFileForm
from app_media.models import File


def upload_file(request):
    close_words_list = ['virus', 'bad', 'troyan', 'sad']
    if request.method == 'POST':
        upload_file_form = UploadFileForm(request.POST, request.FILES)
        if upload_file_form.is_valid():
            file = request.FILES['file']
            for word in close_words_list:
                if word in file.name:
                    return HttpResponse(content='Файл не прошел проверку', status=400)
            # return HttpResponse(content=(file.name, ' ', file.size / 1024, 'КБ'), status=200)
            return HttpResponse(content='Все хорошо!', status=200)
    else:
        upload_file_form = UploadFileForm()

    context = {
        'form': upload_file_form
    }
    return render(request, 'app_media/upload_file.html', context=context)


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = DocumentForm()
    return render(request, 'app_media/file_form_upload.html', {'form': form})


def upload_files(request):
    close_words_list = ['virus', 'bad', 'troyan', 'sad']
    if request.method == 'POST':
        form = MultiFileForm(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('file_field')
            for f in files:
                for word in close_words_list:
                    if word in f.name:
                        return HttpResponse(content=f'Файл {f.name} не прошел проверку', status=400)
                instance = File(file=f)
                instance.save()
            # return HttpResponse(content=(file.name, ' ', file.size / 1024, 'КБ'), status=200)
            return redirect('/')
    else:
        form = MultiFileForm()

    context = {
        'form': form
    }
    return render(request, 'app_media/upload_files.html', context=context)

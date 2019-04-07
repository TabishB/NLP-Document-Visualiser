from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse, JsonResponse

# For Document upload
from django.views.generic.edit import FormView
from django.core.files.storage import FileSystemStorage
from django.contrib.staticfiles.templatetags.staticfiles import static

#for running the analysis.py script
from django.core import management
from django.urls import reverse
from django.core.management.commands import loaddata
import subprocess


from api.views import WordsViewSet
from api.models import *
from visualiser.models import *
from visualiser.forms import DocumentForm
import json, os
import requests

def wordcloud(request, slug):
    # Query will get the document based on the home pages docname. This needs to be consistent with the URL.
    wordsObj = {}
    n_doc = Words.objects(document=slug).count()
    if n_doc > 1:
        wordsObj = Words.objects(document=slug).first()
    elif n_doc == 1:
        wordsObj = Words.objects.get(document=slug)
    else:
        return render(request, 'graphs.html', {'slug':slug})
    # wordsObj = Words.objects.all()
    #for testing purposes
    processedDocuments = Words.objects.only('document')
    p_doc_dict = json.loads(processedDocuments.to_json())
    return render(request, 'wordcloud.html', {
        'data':json.loads(wordsObj.to_json()),
        'available':p_doc_dict,
        'slug':slug
        })

#need to catch not found exception in models.
def topicalcloud(request, slug):
    topicObj = Topics.objects.get(document=slug)
    # return HttpResponse('Unfortunately ' + slug + ' is not in the database')
    topics = json.loads(Topics.objects.only('document').to_json())
    # sorted_words = sorted(data_dict['data']['keywords'], key=lambda k: k['frequency'], reverse=True)
    # data_dict['data'] = sorted_words
    return render(request, 'topicalcloud.html', {'data': json.loads(topicObj.to_json()), 'available':topics, 'slug':slug})

def barchart(request, slug):
    #Orders by the frequency (high to low) and only take the top 50
    wordsObj = {}
    n_doc = Words.objects(document=slug).count()
    if n_doc > 1:
        wordsObj = Words.objects(document=slug).first()
    elif n_doc == 1:
        wordsObj = Words.objects.get(document=slug)
    else:
        return render(request, 'graphs.html', {'slug':slug})    #for testing purposes
    processedDocuments = Words.objects.only('document')
    data_dict = json.loads(wordsObj.to_json())
    sorted_words = sorted(data_dict['words'], key=lambda k: k['frequency'], reverse=True)
    data_dict['words'] = sorted_words
    # print(sorted_words)
    p_doc_dict = json.loads(processedDocuments.to_json())
    return render(request, 'barchart.html', {'data':data_dict, 'available':p_doc_dict, 'slug':slug})

def bubblegraph(request, slug):
    #######TEST DATA
    # graphData = (Words.objects.filter(document=slug)).order_by('-words.frequency')[:10]
    wordsObj = {}
    n_doc = Words.objects(document=slug).count()
    if n_doc > 1:
        wordsObj = Words.objects(document=slug).first()
    elif n_doc == 1:
        wordsObj = Words.objects.get(document=slug)
    else:
        return redirect('home')
        # return render(request, 'graphs.html', {'slug':slug})
    processedDocuments = Words.objects.only('document')
    data_dict = json.loads(wordsObj.to_json())
    sorted_words = sorted(data_dict['words'], key=lambda k: k['frequency'], reverse=True)
    data_dict['words'] = sorted_words
    p_doc_dict = json.loads(processedDocuments.to_json())
    return render(request, 'bubblegraph.html', {'data':data_dict, 'available':p_doc_dict, 'slug':slug})

def fishbone(request, slug):
    fishObj = {}
    n_doc = Fish.objects(name=slug).count()
    if n_doc > 1:
        fishObj = Fish.objects(name=slug).first()
    elif n_doc == 1:
        fishObj = Fish.objects.get(name=slug)
    else:
        return redirect('home')

    fishdata = json.loads(fishObj.to_json())
    # print(fishdata)
    return render(request, 'fishbone.html', {'slug':slug, 'data': json.loads(fishObj.to_json())})

def embed_fishbone(request,slug):
    fishObj = {}
    n_doc = Fish.objects(name=slug).count()
    if n_doc > 1:
        fishObj = Fish.objects(name=slug).first()
    elif n_doc == 1:
        fishObj = Fish.objects.get(name=slug)
    else:
        return redirect('home')

    fishdata = json.loads(fishObj.to_json())
    # print(fishdata)
    return render(request, 'embed_fishbone.html', {'slug':slug, 'data': json.loads(fishObj.to_json())})

def fishbone_api(request,slug):
    fishObj = {}
    n_doc = Fish.objects(name=slug).count()
    if n_doc > 1:
        fishObj = Fish.objects(name=slug).first()
    elif n_doc == 1:
        fishObj = Fish.objects.get(name=slug)
    else:
        return redirect('home')

    fishdata = json.loads(fishObj.to_json())

    # print(fishdata)
    return JsonResponse(fishdata, safe=False)

def graphs(request, slug):
    visuals = []
    if Words.objects.filter(document=slug):
        pass
    else:
        print('no words found')
        visuals.append('words')
    if Topics.objects.filter(document=slug):
        pass
    else:
        print('no topics found')
        visuals.append('topics')
    return render(request, 'graphs.html', {'slug':slug, 'visuals':visuals})

def home(request):
    if request.method == 'POST':
        if 'add_item' in request.POST:

            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                doc = FileDoc.objects.latest('uploaded_at')
				# Runs the lDA  analysis with the relevant filename
				# last parameter needs to be the filename with the approporiate extenson i.e .txt, .json etc
                if doc.topics is None:
                    numOfTopics = -1
                else:
                    numOfTopics = doc.topics

                doc.status = 'In progress'
                output = subprocess.Popen(["python", "manage.py", "analysis", doc.file(), str(numOfTopics)])
                doc.save()
                return redirect('home')
            else:
                print("Form is not valid")
        elif 'delete_item' in request.POST:

           form = DocumentForm()
           item_to_delete = request.POST.get('delete_item')
           FileDoc.objects.filter(pk=item_to_delete).delete()
    else:

        form = DocumentForm()

    documents = FileDoc.objects.all().order_by('-uploaded_at')
    return render(request, 'home.html', {'form': form, 'documents': documents,})

from django.http import HttpResponse
from django.shortcuts import render
from collections import Counter

def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    words = fulltext.split()
    wc = Counter(words) 
    wl = wc.most_common(20)

    return render(request, 'count.html',{
        'fulltext':fulltext,
        'count':len(words),
        'wordlist':wl,
        })

def about(request):
    return render(request,'about.html')
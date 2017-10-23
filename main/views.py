from django.shortcuts import render
from konlpy.tag import Twitter

t = Twitter()

def poc(request):
    print(t)
    t.nouns("A"*10000)
    return None
# Create your views here.

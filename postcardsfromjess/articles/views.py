from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Article
from django.http import HttpResponse

def article_list(request):
    articles = Article.objects.all().order_by('date') # order by date which is in the urls.py file
    return render(request, 'articles/article_list.html', {'articles':articles}) # 3rd parameter is the data to send to the template

def article_detail(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article':article})
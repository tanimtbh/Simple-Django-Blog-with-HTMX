# from django.http.response import HttpResponse
from django.core.paginator import EmptyPage, Paginator
from django.shortcuts import render
from .models import Article
from django.views.generic import ListView


def article_list(request):
    articles = Article.objects.all().order_by('-date')
    #-----------pagination------------
    p=Paginator(articles,5)
    # print("NUMBER OF PAGES")
    # print(p.num_pages)
    page_num=request.GET.get('page', 1)
    try:
        page=p.page(page_num)
        print(page)
    except EmptyPage:
        page=p.page(1)
    #--------end pagination----------
    return render(request, 'articles/article_list.html', { 'articles': page })



def article_detail(request, id, slug):
    #return HttpResponse(slug)
    article= Article.objects.get(id=id, slug=slug)
    return render(request, 'articles/article_detail.html', {'article': article})





def CatList(request, category):
    articles = Article.objects.filter(category__name=category).order_by('-date')
    #-----------pagination------------
    p=Paginator(articles,2)
    # print("NUMBER OF PAGES")
    # print(p.num_pages)
    page_num=request.GET.get('page', 1) # deafult 1 
    try:
        page=p.page(page_num)
        # print(page)
    except EmptyPage:
        page=p.page(1)
    #--------end pagination----------
    return render(request, 'articles/article_by_category.html', { 'articles': page, 'category_name': category})



def test(request):
    #return HttpResponse(slug)

    return render(request, 'articles/component/test.html')


def article_inline_list(request):
    articles = Article.objects.all().order_by('-date')
    #-----------pagination------------
    p=Paginator(articles,5)
    # print("NUMBER OF PAGES")
    # print(p.num_pages)
    page_num=request.GET.get('page', 1)
    try:
        page=p.page(page_num)
        print(page)
    except EmptyPage:
        page=p.page(1)
    #--------end pagination----------
    return render(request, 'articles/component/article_inline_list.html', { 'articles': page })

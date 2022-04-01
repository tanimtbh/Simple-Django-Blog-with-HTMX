from django.conf.urls import url
from django.urls import path
from . import views


app_name='articles'


urlpatterns = [
    url(r'^$', views.article_list, name="list"),
    url(r'partial/', views.article_inline_list, name="inline_list"),
    #url(r'^(?P<slug>[\w-]+)/$', views.article_detail), #old way
    path('<int:id>/<slug:slug>/', views.article_detail, name="detail"), # new way django3
    # path('category1/<category>', views.CatListView.as_view(), name="category1"),
    path('category/<str:category>', views.CatList, name="category_url"),
    path('test/', views.test, name="test_url")
]



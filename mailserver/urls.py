from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.http import Http404, HttpResponse

admin.site.site_header = "Code Mail Admin"
admin.site.site_title = "Code mail Admin Portal"
admin.site.index_title = "Welcome to code mail admin"


def views(request):
    return HttpResponse("<h1>404</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include('app.urls')),
    re_path(r'.*', views, name="http 404")
]


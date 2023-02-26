from django.urls import path ,re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',views.index),
    path('ragistration/',views.ragistration),
    path('login/',views.login),
    path('Login_data/', views.login_form),
    path('table/', views.table),
    path('update_view/<int:uid>/', views.update_view),
    path('update_form_data/', views.update_form_data),
    re_path(r'^delete/(?P<pk>[0-9]+)/$', views.delete, name="delete")
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views


app_name = 'prona'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^prona_dataset$', views.prona_dataset, name='prona_dataset'),
    url(r'^(?P<biznes_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^search-results/$', views.prona_query, name='search-results'),
    url(r'^prona/(?P<user>[0-9]+)/$', views.pronat_mia, name='pronat_mia'),
    url(r'^(?P<pk>[0-9]+)/detail/$', views.prona_detail, name='prona_detail'),
    url(r'^prona/add/$', login_required(views.PronaCreate.as_view()), name='prona-add'),
    url(r'^prona/(?P<pk>[0-9]+)/update/$', login_required(views.PronaUpdate.as_view()), name='prona-update'),
    url(r'^prona/(?P<pk>[0-9]+)/delete/$', login_required(views.PronaDelete.as_view()), name='prona-delete'),
    url(r'^login/$', views.LoginView, name='login'),
    url(r'^logout/$', views.LogoutView, name='logout'),
    url(r'^register/$', views.RegisterView, name='register'),
]

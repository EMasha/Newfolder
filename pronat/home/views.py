# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate,  login, logout
from models import *
from forms import UserLoginForm, UserRegistrationForm
from django.core.serializers import serialize
from django.http import HttpResponse
from django import forms
from leaflet.forms.fields import PointField
from leaflet.forms.widgets import LeafletWidget
from django.db.models import Q


# Create your views here.
def home (request):
    a = biznes.objects.all()
    return render(request,'prona/home.html',{'a': a})

def prona_dataset(request):
    pronat = serialize('geojson', prona.objects.all())
    return HttpResponse(pronat, content_type='json')
def detail (request, biznes_id):
    a = biznes.objects.all()
    b = prona.objects.all()
    d = b.filter(id_biznes_id = biznes_id)
    return render(request,'prona/prona.html',{'d': d, 'a':a})

def prona_query (request):
    if request.method == 'GET':
        queryset_list = prona.objects.all()
        query = request.GET.get("search", None)
        if query:
            queryset_list = queryset_list.filter(
                Q(id_vendodhje__id_rruga__emri__icontains=query)|
                Q(id_vendodhje__id_zona__zona__icontains=query)
            )

        return render(request,'prona/search-results.html',{'queryset_list': queryset_list}, content_type='json')
def prona_detail(request, pk):
    c = get_object_or_404(prona, pk=pk)
    e = prona.objects.filter(pk = pk)
    f = c.hits
    g = f+1
    h = e.update(hits = g)
    return render(request, 'prona/prona_detail.html', {'c': c, 'h': h })

class YourMapWidget(LeafletWidget):
    geometry_field_class = 'geom'
class PronaAdd(forms.ModelForm):
    geom = PointField()
    class Meta:
        model = prona
        fields = ['id_vendodhje', 'id_lloji', 'cmimi', 'dhoma', 'banjo', 'size', 'titulli', 'pershkrim', 'id_biznes', 'status', 'url', 'hits', 'creation_date', 'modif_date', 'sponsorizuar', 'geom', 'id_user',]
        widgets = {'geom': YourMapWidget()}


class PronaCreate(CreateView):
    model = prona
    form_class = PronaAdd
    template_name = 'prona/prona_form.html'


    def save_model(self, request, obj, ):
        if not obj.User.id:
            obj.User = request.user
        obj.save()


class PronaUpdate(UpdateView):
    model = prona
    fields = ['id_vendodhje', 'id_lloji', 'cmimi', 'dhoma', 'banjo', 'size', 'titulli', 'pershkrim', 'id_biznes', 'status', 'url', 'hits', 'creation_date', 'modif_date', 'sponsorizuar', 'geom']
    template_name = 'prona/prona_form.html'


class PronaDelete(DeleteView):
    model = prona
    success_url = reverse_lazy('prona:home')

def LoginView(request):
    print (request.user.is_authenticated())
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        print (request.user.is_authenticated())
        return redirect("/home/")

    return render(request, "prona/login_form.html", {"form": form})

def RegisterView(request):
    print (request.user.is_authenticated())
    forms = UserRegistrationForm(request.POST or None)
    if forms.is_valid():
        user = forms.save(commit=False)
        password = forms.cleaned_data.get('password')
        user.set_password(password)
        user.save()

        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect("/home/")

    return render(request, "prona/registration_form.html", {"forms": forms})

def LogoutView(request):
    logout(request)
    print (request.user.is_authenticated())
    return redirect("/home/")
    return render(request, 'prona/home.html', {})

def pronat_mia (request, user):
    e = prona.objects.all()
    f = e.filter(id_user_id = user)
    return render(request,'prona/pronat_mia.html', {'f': f})

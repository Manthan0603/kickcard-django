from typing import cast

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db.models.lookups import IsNull
from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from .forms import *
from .models import KickCard
from django.views.generic import CreateView,UpdateView,DetailView,TemplateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

# Create your views here.


def customerRegister(request):
    form = CustomerSignUpForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        pin = form.cleaned_data['pin']
        donor = form.cleaned_data['is_donor']

        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password, pin=pin)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("login")
    context = {
        'form': form
    }
    return render(request, 'signup.html', context)


def customerLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        pin = request.POST['pin']
        user = authenticate(username=username, password=password, pin=pin)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("index")
            else:
                return render(request, 'login.html', {'error_message': 'Your account disable'})
        else:
            return render(request, 'login.html', {'error_message': 'Invalid Login'})
    return render(request, 'login.html')

def Signout(request):
    logout(request)
    return redirect('login')
def Home(request):
    return render(request, 'home.html')

def Index(request,):
    profile = request.user
    return render(request, 'index.html',{'profile':profile})

def Services(request):
    return render(request, 'services.html')

def Contact(request):
    return render(request, 'contact.html')

def About(request):
    return render(request, 'about.html')



class AddPostView(CreateView):
    model = KickCard
    form_class = AddRationCard
    template_name = 'addrationcard.html'
    success_url = reverse_lazy('index')

    def get_initial(self):
         return {'user': self.request.user}

class UserUpdateView(UpdateView):
    model = KickCard
    form_class = AddRationCard
    template_name = 'updateform.html'
    success_url = reverse_lazy('index')


class CancelRationCard(CreateView):
    template_name = 'cancelration.html'
    model = CancelKickCard
    form_class = Cancelform
    success_url = reverse_lazy('index')

    # def form_valid(self, form):
    #     messages.success(self.request, 'Form submission successful')
    #     return super().form_valid(form)

    def get_initial(self):
         return {'cancel': self.request.user.user.id}



def Dashboard(request):
    check = BookedRation.objects.filter(booked = request.user.user.id).exists()
    print(check)
    if check == True:
        grain = 0
        rice = 0
        toor = 0
        kero = 0
        context = {'grain': grain, 'rice': rice,'kero':kero,'toor':toor}
        return render(request, 'Dashboard.html',context)
    else:
        data = KickCard.objects.get(id = request.user.user.id)
        ct = data.CardType
        income = data.TotalIncome
        member = data.TotalMembers
        if ct == 'APL' and income < 6000:
            grain = float(member) * 3.50
            rice = float(member) * 1.50
        elif ct == 'BPL' and income < 3600:
            grain = float(member) * 5.00
            rice = float(member) * 3.00
        kero = 1
        toor = 1
        context = {'grain': grain, 'rice': rice,'kero':kero,'toor':toor}
        return render(request, 'Dashboard.html',context)


class DeshboardView(CreateView):
    template_name = 'Dashboard.html'
    model = BookedRation
    form_class = Booked
    success_url = reverse_lazy('index')

    def get_initial(self):
        return {'booked': self.request.user.id}


    def get_context_data(self, **kwargs):
        context = super(DeshboardView, self).get_context_data(**kwargs)
        data = BookedRation.objects.filter(booked = self.request.user.user.id).exists()
        grain,rice = 1,1
        if data == True:
            context['grain'] = 0
            context['rice'] = 0
            context['toor'] = 0
            context['kero'] = 0
            context['check'] = 0
            return context
        else:
            data = KickCard.objects.get(id =self.request.user.user.id)
            ct = data.CardType
            income = data.TotalIncome
            member = data.TotalMembers
            if ct == 'APL' and income < 6000:
                grain = float(member) * 3.50
                rice = float(member) * 1.50
            elif ct == 'BPL' and income < 3600:
                grain = float(member) * 5.00
                rice = float(member) * 3.00
            context['grain'] = grain
            context['rice'] = rice
            context['toor'] = 1
            context['kero'] = 1
            context['check'] = 1
            return context

class ContactView(CreateView):
    model = ContectUs
    template_name = 'contact.html'
    fields = '__all__'
    success_url = reverse_lazy('index')

    # def form_valid(self,form):
    #     super(ContactView,self).form_valid(form)
    #     messages.success(self.request, 'Item created successfully!')
    #     import pdb
    #     pdb.set_trace()
    #     return HttpResponseRedirect(self.get_success_url())
    # def form_invalid(self,form):
    #     return self.render_to_response(self.get_context_data(form=form))
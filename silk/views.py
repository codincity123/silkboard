import email
from urllib import request
from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpResponse
from .forms import *
from django.views.generic.edit import FormView
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView
from django.core.mail import send_mail
from .filters import *
from .updateforms import *

# Create your views here.
def index(request):
    return render(request,'Index/index.html',{})


def logout_request(request):
    logout(request)
    messages.info(request,"Logged out successfully!")
    return redirect("/")


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if not user.is_superuser == True:
                    login(request, user)
                    messages.info(request,f"You are now logged in as {username}")
                    return redirect('/')
                else:
                    login(request, user)
                    messages.info(request,f"You are now logged in as {username}")
                    return redirect('users')
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "login/login.html",
                    context={"form":form})

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from .sendmail import sendMailUser

class mod1(LoginRequiredMixin,FormView):
    form_class = seedCropPerformanceForm
    success_url ="/"
    template_name = "module1/module1.html"
    
    def form_valid(self, form):
        mydict = {'username': self.request.user}
        form.instance.unit_name = self.request.user
        form.save()
        messages.add_message(self.request, messages.SUCCESS, 'Successfully Added !')
        return redirect('moddata1')

class mod2(LoginRequiredMixin,FormView):
    form_class = seedCocoonPurchaseForm
    success_url ="/"
    template_name = "module23/module2.html"
    def form_valid(self, form):
        form.instance.unit_name = self.request.user
        form.save()
        messages.add_message(self.request, messages.SUCCESS, 'Successfully Added !')
        return redirect('moddata2')

class mod3(LoginRequiredMixin,FormView):
    form_class = seedDflProductionAndPreservationForm
    success_url ="/"
    template_name = "module23/module3.html"
    

    def form_valid(self, form):
        form.instance.unit_name = self.request.user
        form.save()
        messages.add_message(self.request, messages.SUCCESS, 'Successfully Added !')
        return redirect('moddata3')

class mod4(LoginRequiredMixin,FormView):
    form_class = dflsReleaseAndSupplyForm
    success_url ="/"
    template_name = "module23/module4.html"
    def form_valid(self, form):
        
        form.instance.unit_name = self.request.user
        form.save()
        messages.add_message(self.request, messages.SUCCESS, 'Successfully Added !')
        return redirect('moddata4')

# class mod5(LoginRequiredMixin,FormView):
#     form_class = dflsPreservationAndSupplyForm
#     success_url ="/"
#     template_name = "module23/module5.html"
#     def form_valid(self, form):
#         form.instance.unit_name = self.request.user
#         form.save()
#         messages.add_message(self.request, messages.SUCCESS, 'Successfully Added !')
#         return redirect('moddata5')

# class mod6(LoginRequiredMixin,FormView):
#     form_class = dflsSupplyForm
#     success_url ="/"
#     template_name = "module23/module6.html"
#     def form_valid(self, form):
#         form.instance.unit_name = self.request.user
#         form.save()
#         messages.add_message(self.request, messages.SUCCESS, 'Successfully Added !')
#         return redirect('moddata6')

@login_required()
def moddata1(request):
    # data = seedCropPerformance.objects.filter(unit_name = request.user)
    # d = seedCropPerformance.objects.values_list('Date')
    # return render(request,'module1/moddata1.html',{'data':data})
    data = seedCropPerformance.objects.filter(unit_name = request.user).order_by("-Date")
    myfilter = seedCropPerformanceFilters(request.GET,queryset=data)
    data = myfilter.qs
    return render(request,'module1/moddata1.html',{'data':data,'myfill':myfilter})
@login_required()
def moddata2(request):
    # data = seedCocoonPurchase.objects.filter(unit_name = request.user)
    # d = seedCocoonPurchase.objects.values_list('Date')
    # return render(request,'module23/moddata2.html',{'data':data})

    data = seedCocoonPurchase.objects.filter(unit_name = request.user).order_by("-Date")
    myfilter = seedCocoonPurchaseFilter(request.GET,queryset=data)
    data = myfilter.qs
    return render(request,'module23/moddata2.html',{'data':data,'myfill':myfilter})
@login_required()
def moddata3(request):
    # data = seedCocoonAssesment.objects.filter(unit_name = request.user)
    # d = seedCocoonAssesment.objects.values_list('Date')
    # return render(request,'module23/moddata3.html',{'data':data})

    data = seedDflProductionAndPreservation.objects.filter(unit_name = request.user).order_by("-Date")
    myfilter = seedDflProductionAndPreservationFilter(request.GET,queryset=data)
    data = myfilter.qs
    return render(request,'module23/moddata3.html',{'data':data,'myfill':myfilter})

@login_required()
def moddata4(request):
    # data = seedDflProduction.objects.filter(unit_name = request.user)
    # d = seedDflProduction.objects.values_list('Date')
    # return render(request,'module23/moddata4.html',{'data':data})

    data = dflsReleaseAndSupply.objects.filter(unit_name = request.user).order_by("-Date")
    myfilter = dflsReleaseAndSupplyFilter(request.GET,queryset=data)
    data = myfilter.qs
    return render(request,'module23/moddata4.html',{'data':data,'myfill':myfilter})



@login_required()
def updatemod1(request,id):
    data = get_object_or_404(seedCropPerformance, p1_seed_lot_no=id)
    form = updateseedCropPerformanceForm(instance=data)                                                               

    if request.method == "POST":
        form = updateseedCropPerformanceForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request, "Data is updated")
            return redirect('moddata1')
    context = {
        "form":form
    }
    return render(request,'Index/update.html',context)

@login_required()
def updatemod2(request,id):
    data = get_object_or_404(seedCocoonPurchase, SSPC_Lot_No_Assigned=id)
    form = updateseedCocoonPurchaseForm(instance=data)                                                               

    if request.method == "POST":
        form = updateseedCocoonPurchaseForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request, "Data is updated")
            return redirect('moddata2')
 
    # add form dictionary to context
    context = {
        "form":form
    }
    return render(request,'Index/update.html',context)

@login_required()
def updatemod3(request,id):
    data = get_object_or_404(seedDflProductionAndPreservation, SSPC_Lot_No_Assigned=id)
    form = updateseedDflProductionAndPreservationForm(instance=data)                                                               

    if request.method == "POST":
        form = updateseedDflProductionAndPreservationForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request, "Data is updated")
            return redirect('moddata3')
 
    # add form dictionary to context
    context = {
        "form":form
    }
    return render(request,'Index/update.html',context)

@login_required()
def updatemod4(request,id):
    data = get_object_or_404(dflsReleaseAndSupply, id=id)
    form = updatedflsReleaseAndSupplyForm(instance=data)                                                               

    if request.method == "POST":
        form = updatedflsReleaseAndSupplyForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request, "Data is updated")
            return redirect('moddata4')
 
    # add form dictionary to context
    context = {
        "form":form
    }
    return render(request,'Index/update.html',context)

# @login_required()
# def updatemod5(request,id):
#     data = get_object_or_404(dflsPreservationAndSupply, lot_no=id)
#     form = dflsPreservationAndSupplyForm(instance=data)                                                               

#     if request.method == "POST":
#         form = dflsPreservationAndSupplyForm(request.POST, instance=data)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Data is updated")
#             return redirect('moddata5')
 
#     # add form dictionary to context
#     context = {
#         "form":form
#     }
#     return render(request,'Index/update.html',context)

# @login_required()
# def updatemod6(request,id):
#     data = get_object_or_404(dflsSupply, lot_no=id)
#     form = dflsSupplyForm(instance=data)                                                               

#     if request.method == "POST":
#         form = dflsSupplyForm(request.POST, instance=data)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Data is updated")
#             return redirect('moddata6')
 
#     # add form dictionary to context
#     context = {
#         "form":form
#     }
#     return render(request,'Index/update.html',context)


# def fillmod1(request):
#     data = seedCropPerformance.objects.all().order_by("-Date")
#     myfilter = seedCropPerformanceFilters(request.GET,queryset=data)
#     data = myfilter.qs
#     return render(request,'admin_panel/index.html',{'data':data,'myfill':myfilter})
import profile
from django.shortcuts import render,get_object_or_404,redirect
from silk.models import *
from .filters import *
import xlwt
from django.http import HttpResponse
import datetime
from .forms import *
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required,user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth import login,logout,authenticate
# Create your views here.


def admin_logout_request(request):
    logout(request)
    messages.info(request,"Logged out successfully!")
    return redirect("/")


def admin_login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_superuser == True:
                login(request, user)
                messages.info(request,f"You are now logged in as {username}")
                return redirect('users')
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "admin_panel/login.html",
                    context={"form":form})

@login_required(login_url='admin_login')
@user_passes_test(lambda u: u.is_superuser)
def del_user(request, username):
    try:
        u = User.objects.get(username = username)
        u.delete()
        messages.success(request, "The staff is deleted")            

    except User.DoesNotExist:
        messages.error(request, "User doesnot exist")    
        return redirect('users')

    # except Exception as e: 
    #     return render(request, 'front.html',{'err':e.message})

    return redirect('users')


@login_required(login_url='admin_login')
@user_passes_test(lambda u: u.is_superuser)
def admin_home(request):
    data = seedCropPerformance.objects.all().order_by("-Date")
    myfilter = seedCropPerformanceFilters(request.GET,queryset=data)
    data = myfilter.qs
    return render(request,'admin_panel/index.html',{'data':data,'myfill':myfilter})

@login_required(login_url='admin_login')
@user_passes_test(lambda u: u.is_superuser)
def export_users_xls(request):
    data = seedCropPerformance.objects.all().order_by("-Date")
    myfilter = seedCropPerformanceFilters(request.GET,queryset=data)
    data = myfilter.qs
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'
    wb = xlwt.Workbook(encoding='utf-8',)
    ws = wb.add_sheet('Users')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['Name_of_the_Adopted_Seed_Rearer','Reg_Certificate_No_of_ASR','p1_seed_lot_no','p1_race','no_of_dfls_brushed','date_of_hatching','date_of_spinning','hatching','seed_crop_inspected_by','seed_crop_remarks','date_of_cocoon_assesment','cocoon_yield_per_100dfls','no_of_cocoon_per_kg','no_of_good_cocoon_per_kg','no_of_defective_cocoon_per_kg','no_of_male_cocoon_per_kg','no_of_female_cocoon_per_kg','pupation','fitness_of_seed_cocoon_per_kg','Date']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = data.all().values_list('Name_of_the_Adopted_Seed_Rearer','Reg_Certificate_No_of_ASR','p1_seed_lot_no','p1_race','no_of_dfls_brushed','date_of_hatching','date_of_spinning','hatching','seed_crop_inspected_by','seed_crop_remarks','date_of_cocoon_assesment','cocoon_yield_per_100dfls','no_of_cocoon_per_kg','no_of_good_cocoon_per_kg','no_of_defective_cocoon_per_kg','no_of_male_cocoon_per_kg','no_of_female_cocoon_per_kg','pupation','fitness_of_seed_cocoon_per_kg','Date')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            if isinstance(row[col_num],datetime.date):
                date_time = row[col_num].strftime('%Y-%m-%d')
                ws.write(row_num, col_num,date_time, font_style)
            else:
                ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

@login_required(login_url='admin_login')
@user_passes_test(lambda u: u.is_superuser)
def adminMod2(request):
    data = seedCocoonPurchase.objects.all().order_by("-Date")
    myfilter = seedCocoonPurchaseFilter(request.GET,queryset=data)
    data = myfilter.qs
    return render(request,'admin_panel/mod2.html',{'data':data,'myfill':myfilter})


@login_required(login_url='admin_login')
@user_passes_test(lambda u: u.is_superuser)
def export_users_xls2(request):
    data = seedCocoonPurchase.objects.all().order_by("-Date")
    myfilter = seedCocoonPurchaseFilter(request.GET,queryset=data)
    data = myfilter.qs
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'
    wb = xlwt.Workbook(encoding='utf-8',)
    ws = wb.add_sheet('Users')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['Seed_Cocoons_Purchased_or_Received_From','Reg_Certificate_No','date_of_seed_cocoon_procurement','actual_no_of_cocoon_per_kg','Total_Qty_of_Seed_Cocoons_Procured_by_number','pupation_perc','seed_cocoon_price_per_kg','Total_Amount_Paid_to_ASR_per_Unit_rs','Transaction_ID','SSPC_Lot_No_Assigned','Seed_Cocoons_Diverted_to_Other_Unit','Actual_Qty_of_Seed_Cocoons_Diverted_to_Units_kg','Actual_Qty_of_Seed_Cocoons_Diverted_to_Units_no','Actual_Qty_of_Seed_Cocoons_used_for_processing_kg','Actual_Qty_of_Seed_Cocoons_used_for_processing_no','Date']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = data.all().values_list('Seed_Cocoons_Purchased_or_Received_From','Reg_Certificate_No','date_of_seed_cocoon_procurement','actual_no_of_cocoon_per_kg','Total_Qty_of_Seed_Cocoons_Procured_by_number','pupation_perc','seed_cocoon_price_per_kg','Total_Amount_Paid_to_ASR_per_Unit_rs','Transaction_ID','SSPC_Lot_No_Assigned','Seed_Cocoons_Diverted_to_Other_Unit','Actual_Qty_of_Seed_Cocoons_Diverted_to_Units_kg','Actual_Qty_of_Seed_Cocoons_Diverted_to_Units_no','Actual_Qty_of_Seed_Cocoons_used_for_processing_kg','Actual_Qty_of_Seed_Cocoons_used_for_processing_no','Date')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            if isinstance(row[col_num],datetime.date):
                date_time = row[col_num].strftime('%Y-%m-%d')
                ws.write(row_num, col_num,date_time, font_style)
            else:
                ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

#mod3
@login_required(login_url='admin_login')
@user_passes_test(lambda u: u.is_superuser)
def adminMod3(request):
    data = seedDflProductionAndPreservation.objects.all().order_by("-Date")
    myfilter = seedDflProductionAndPreservationFilter(request.GET,queryset=data)
    data = myfilter.qs
    return render(request,'admin_panel/mod3.html',{'data':data,'myfill':myfilter})

@login_required(login_url='admin_login')
@user_passes_test(lambda u: u.is_superuser)
def export_users_xls3(request):
    data = seedDflProductionAndPreservation.objects.all().order_by("-Date")
    myfilter = seedDflProductionAndPreservationFilter(request.GET,queryset=data)
    data = myfilter.qs
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'
    wb = xlwt.Workbook(encoding='utf-8',)
    ws = wb.add_sheet('Users')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['SSPC_Lot_No_Assigned','Combination','Qty_of_DFLs_Produced_by_Weight_kg','Qty_of_DFLs_Produced_by_no','Qty_of_DFLs_treated_by_Weight_kg','Qty_of_DFLs_treated_by_no','Qty_of_Hibernated_DFLs_Preserved_by_Weight_kg','Qty_of_Hibernated_DFLs_Preserved_by_no','DFLs_Preserved_at_CSP_Name','Preservation_Schedule','Date_of_Preservation_at_Cold_Storage','Qty_of_Pierced_Cocoons_Obtained_Kg','Sale_Proceeds_from_Pierced_Cocoons_Rs','Sale_Proceeds_from_Others_if_any_Rs','Date']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = data.all().values_list('SSPC_Lot_No_Assigned','Combination','Qty_of_DFLs_Produced_by_Weight_kg','Qty_of_DFLs_Produced_by_no','Qty_of_DFLs_treated_by_Weight_kg','Qty_of_DFLs_treated_by_no','Qty_of_Hibernated_DFLs_Preserved_by_Weight_kg','Qty_of_Hibernated_DFLs_Preserved_by_no','DFLs_Preserved_at_CSP_Name','Preservation_Schedule','Date_of_Preservation_at_Cold_Storage','Qty_of_Pierced_Cocoons_Obtained_Kg','Sale_Proceeds_from_Pierced_Cocoons_Rs','Sale_Proceeds_from_Others_if_any_Rs','Date')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            if isinstance(row[col_num],datetime.date):
                date_time = row[col_num].strftime('%Y-%m-%d')
                ws.write(row_num, col_num,date_time, font_style)
            else:
                ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


#mod4
@login_required(login_url='admin_login')
@user_passes_test(lambda u: u.is_superuser)
def adminMod4(request):
    data = dflsReleaseAndSupply.objects.all().order_by("-Date")
    myfilter = dflsReleaseAndSupplyFilter(request.GET,queryset=data)
    data = myfilter.qs
    return render(request,'admin_panel/mod4.html',{'data':data,'myfill':myfilter})

@login_required(login_url='admin_login')
@user_passes_test(lambda u: u.is_superuser)
def export_users_xls4(request):
    data = dflsReleaseAndSupply.objects.all().order_by("-Date")
    myfilter = dflsReleaseAndSupplyFilter(request.GET,queryset=data)
    data = myfilter.qs
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'
    wb = xlwt.Workbook(encoding='utf-8',)
    ws = wb.add_sheet('Users')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['SSPC_Lot_No_Assigned','Date_of_Release','DFLs_Released_kg','Preservation_Loss_Kg','Winnowing_Loss_Kg','DFLs_Packed_for_Supply_Kg','DFLs_Packed_for_Supply_No','Date_of_Supply','Supplied_to','No_of_DFLs','Amount','Cash_Bill_Invoice_No_Date','Remarks','Processing_loss','No_of_DFLs_for_write_off','Date']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = data.all().values_list('SSPC_Lot_No_Assigned','Date_of_Release','DFLs_Released_kg','Preservation_Loss_Kg','Winnowing_Loss_Kg','DFLs_Packed_for_Supply_Kg','DFLs_Packed_for_Supply_No','Date_of_Supply','Supplied_to','No_of_DFLs','Amount','Cash_Bill_Invoice_No_Date','Remarks','Processing_loss','No_of_DFLs_for_write_off','Date')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            if isinstance(row[col_num],datetime.date):
                date_time = row[col_num].strftime('%Y-%m-%d')
                ws.write(row_num, col_num,date_time, font_style)
            else:
                ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


# # registration
@login_required(login_url='admin_login')
@user_passes_test(lambda u: u.is_superuser)
def register(request):   
    if request.method == 'POST':
        f = UserForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('users')

    else:
        f = UserForm()

    return render(request,'admin_panel/regist.html', {'form': f})


@login_required(login_url='admin_login')
@user_passes_test(lambda u: u.is_superuser)
def users(request):
    data = Profile.objects.all()
    return render(request,'admin_panel/users.html',{'data':data})


@login_required(login_url='admin_login')
@user_passes_test(lambda u: u.is_superuser)
def updatedata(request,id):
    data = get_object_or_404(Profile, id=id)
    form = UserProfileForm(instance=data)                                                               

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile is updated")
            return redirect('users')
    context = {
        "form":form
    }
    return render(request,'admin_panel/update.html',context)


@login_required(login_url='admin_login')
@user_passes_test(lambda u: u.is_superuser)
def mod1delete(request, username):
    try:
        u = seedCropPerformance.objects.get(p1_seed_lot_no = username)
        u.delete()
        messages.success(request, "Record is deleted")            

    except User.DoesNotExist:
        messages.error(request, "User doesnot exist")    
        return redirect('admin_home')

    # except Exception as e: 
    #     return render(request, 'front.html',{'err':e.message})

    return redirect('admin_home')


@login_required(login_url='admin_login')
@user_passes_test(lambda u: u.is_superuser)
def mod2delete(request, username):
    try:
        u = seedCocoonPurchase.objects.get(SSPC_Lot_No_Assigned = username)
        u.delete()
        messages.success(request, "Record is deleted")            

    except User.DoesNotExist:
        messages.error(request, "User doesnot exist")    
        return redirect('mod2')

    # except Exception as e: 
    #     return render(request, 'front.html',{'err':e.message})

    return redirect('mod2')

@login_required(login_url='admin_login')
@user_passes_test(lambda u: u.is_superuser)
def mod3delete(request, username):
    try:
        u = seedDflProductionAndPreservation.objects.get(SSPC_Lot_No_Assigned = username)
        u.delete()
        messages.success(request, "Record is deleted")            

    except User.DoesNotExist:
        messages.error(request, "User doesnot exist")    
        return redirect('mod3')

    # except Exception as e: 
    #     return render(request, 'front.html',{'err':e.message})

    return redirect('mod3')

@login_required(login_url='admin_login')
@user_passes_test(lambda u: u.is_superuser)
def mod4delete(request, id):
    try:
        u = dflsReleaseAndSupply.objects.get(id = id)
        u.delete()
        messages.success(request, "Record is deleted")            

    except User.DoesNotExist:
        messages.error(request, "User doesnot exist")    
        return redirect('mod4')

    # except Exception as e: 
    #     return render(request, 'front.html',{'err':e.message})

    return redirect('mod4')
    

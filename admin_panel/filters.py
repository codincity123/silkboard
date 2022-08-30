from dataclasses import field
from statistics import mode
from tkinter import Widget
from django.forms import CharField, DateInput
import django_filters
from silk.models import *
from django_filters import DateFilter,CharFilter
 
class seedCropPerformanceFilters(django_filters.FilterSet):
    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
            super(seedCropPerformanceFilters, self).__init__(data=data, queryset=queryset, request=request, prefix=prefix)
            self.filters['p1_seed_lot_no'].field.widget.attrs.update({"class":"form-control","placeholder":"Type..."})
            self.filters['unit_name'].field.widget.attrs.update({"class":"form-control","placeholder":"Unit Name"})
    start_date = DateFilter(field_name="Date", lookup_expr='gte',label="From",widget=DateInput(attrs={'type':'date',"class":"form-control","placeholder":"From"}))
    end_date = DateFilter(field_name="Date", lookup_expr='lte',label="To",widget=DateInput(attrs={'type':'date',"class":"form-control","placeholder":"To"}))
    class Meta:
        model = seedCropPerformance
        fields = ['unit_name','p1_seed_lot_no']


class seedCocoonPurchaseFilter(django_filters.FilterSet):
    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
            super(seedCocoonPurchaseFilter, self).__init__(data=data, queryset=queryset, request=request, prefix=prefix)
            self.filters['SSPC_Lot_No_Assigned'].field.widget.attrs.update({"class":"form-control","placeholder":"Type...",'type':'text'})
            self.filters['unit_name'].field.widget.attrs.update({"class":"form-control","placeholder":"Unit Name"})
    start_date = DateFilter(field_name="Date", lookup_expr='gte',label="From",widget=DateInput(attrs={'type':'date',"class":"form-control","placeholder":"From"}))
    end_date = DateFilter(field_name="Date", lookup_expr='lte',label="To",widget=DateInput(attrs={'type':'date',"class":"form-control","placeholder":"To"}))
    SSPC_Lot_No_Assigned = CharFilter()
    class Meta:
        model = seedCocoonPurchase
        fields = ['unit_name','SSPC_Lot_No_Assigned']


class seedDflProductionAndPreservationFilter(django_filters.FilterSet):
    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
            super(seedDflProductionAndPreservationFilter, self).__init__(data=data, queryset=queryset, request=request, prefix=prefix)
            self.filters['SSPC_Lot_No_Assigned'].field.widget.attrs.update({"class":"form-control","placeholder":"Type...",'type':'text'})
            self.filters['unit_name'].field.widget.attrs.update({"class":"form-control","placeholder":"Unit Name"})
    start_date = DateFilter(field_name="Date", lookup_expr='gte',label="From",widget=DateInput(attrs={'type':'date',"class":"form-control","placeholder":"From"}))
    end_date = DateFilter(field_name="Date", lookup_expr='lte',label="To",widget=DateInput(attrs={'type':'date',"class":"form-control","placeholder":"To"}))
    SSPC_Lot_No_Assigned = CharFilter()
    class Meta:
        model = seedDflProductionAndPreservation
        fields = ['unit_name','SSPC_Lot_No_Assigned']


class dflsReleaseAndSupplyFilter(django_filters.FilterSet):
    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
            super(dflsReleaseAndSupplyFilter, self).__init__(data=data, queryset=queryset, request=request, prefix=prefix)
            self.filters['SSPC_Lot_No_Assigned'].field.widget.attrs.update({"class":"form-control","placeholder":"Type...",'type':'text'})
            self.filters['unit_name'].field.widget.attrs.update({"class":"form-control","placeholder":"Unit Name"})
    start_date = DateFilter(field_name="Date", lookup_expr='gte',label="From",widget=DateInput(attrs={'type':'date',"class":"form-control","placeholder":"From"}))
    end_date = DateFilter(field_name="Date", lookup_expr='lte',label="To",widget=DateInput(attrs={'type':'date',"class":"form-control","placeholder":"To"}))
    SSPC_Lot_No_Assigned = CharFilter()
    class Meta:
        model = dflsReleaseAndSupply
        fields = ['unit_name','SSPC_Lot_No_Assigned']


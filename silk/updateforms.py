from django.forms import ModelForm
from .models import *
from django import forms
class updateseedCropPerformanceForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        self.fields["Name_of_the_Adopted_Seed_Rearer"].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Type...',
            })
        self.fields["Name_of_the_Adopted_Seed_Rearer"].label="Name of the Adopted Seed Rearer (ASR)"
        self.fields["Reg_Certificate_No_of_ASR"].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Type...',
            })
        self.fields["Reg_Certificate_No_of_ASR"].label="Reg. Certificate No of ASR"
        self.fields["p1_seed_lot_no"].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Type...',
            'readonly':'True',
            })
        self.fields["p1_seed_lot_no"].label="P1 Seed Lot No."
        self.fields["p1_race"].label="P1 Race"
        self.fields["no_of_dfls_brushed"].widget.attrs.update({
            'class':'form-control',
            'placeholder':'No Decimal..',
            })
        self.fields["no_of_dfls_brushed"].label="No. of DFLs Brushed"
        
        self.fields["date_of_hatching"].label="Date of Hatching"
        self.fields["date_of_spinning"].label="Date of Spinning"
        self.fields["hatching"].widget.attrs.update({
            'class':'form-control',
            'id':'hatch',
            'placeholder':'Upto One Decimal..',
            })
        self.fields["hatching"].label="Hatching %"
        self.fields["seed_crop_inspected_by"].widget.attrs.update({
            'class':'form-control',
            
            'placeholder':'Type...',
            })
        self.fields["seed_crop_inspected_by"].label="Seed Crop Inspected by"
        self.fields["seed_crop_remarks"].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Type...',
            })
        self.fields["seed_crop_remarks"].label="Seed Crop Remarks"
        self.fields["date_of_cocoon_assesment"].label="Date of Cocoon Assessment"
        self.fields["cocoon_yield_per_100dfls"].widget.attrs.update({
            'class':'form-control',
            'id':'yield',
            'placeholder':'Upto One Decimal..',
            })
        self.fields["cocoon_yield_per_100dfls"].label="Cocoon Yield/100 DFLs (Kg)"
        self.fields["no_of_cocoon_per_kg"].widget.attrs.update({
            'class':'form-control',
            'placeholder':'No Decimal..',
            })
        self.fields["no_of_cocoon_per_kg"].label="No. of Cocoons/ Kg "
        self.fields["no_of_good_cocoon_per_kg"].widget.attrs.update({
            'class':'form-control',
            'placeholder':'No Decimal..',
            })
        self.fields["no_of_good_cocoon_per_kg"].label="No. of Good Cocooons/Kg "
        self.fields["no_of_defective_cocoon_per_kg"].widget.attrs.update({
            'class':'form-control',
            'placeholder':'No Decimal..',
            })
        self.fields["no_of_defective_cocoon_per_kg"].label="No. of  Defective Cocooons/Kg "
        self.fields["no_of_male_cocoon_per_kg"].widget.attrs.update({
            'class':'form-control',
            'placeholder':'No Decimal..',
            })
        self.fields["no_of_male_cocoon_per_kg"].label="No. of Male Cocooons/Kg "
        self.fields["no_of_female_cocoon_per_kg"].widget.attrs.update({
            'class':'form-control',
            'placeholder':'No Decimal..',
            })
        self.fields["no_of_female_cocoon_per_kg"].label="No. of Female Cocooons/Kg "
        self.fields["pupation"].widget.attrs.update({
            'class':'form-control',
            'placeholder':'No Decimal..',
            })
        self.fields["pupation"].label="Pupation %/ "
        self.fields["fitness_of_seed_cocoon_per_kg"].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Type...',
            })
        self.fields["fitness_of_seed_cocoon_per_kg"].label="Fitness of Seed Cocoons for Purchase "


        
    class Meta:
        model = seedCropPerformance
        fields = "__all__"
        exclude= ['unit_name']
        ordering = ['-Date']
        widgets={
            'cocoon_yield_per_100dfls':forms.TextInput(attrs={"oninput":"validate(this)"}),
            'seed_crop_remarks':forms.TextInput(attrs={"oninput":"this.value = this.value.replace(/[^a-z 0-9 A-Z]/g, '').replace(/(\..*)\./g, '$1')"}),
            'seed_crop_inspected_by':forms.TextInput(attrs={"oninput":"this.value = this.value.replace(/[^a-z A-Z]/g, '').replace(/(\..*)\./g, '$1')"}),
            'hatching':forms.TextInput(attrs={"oninput":"check(this)"}),
            'no_of_dfls_brushed':forms.TextInput(attrs={"oninput":"this.value = this.value.replace(/[^0-9]/g, '').replace(/(\..*)\./g, '$1')"}),
            'Name_of_the_Adopted_Seed_Rearer': forms.TextInput(attrs={"oninput":"this.value = this.value.replace(/[^a-zA-Z.]/g, '').replace(/(\..*)\./g, '$1')"}),
            'date_of_hatching': forms.DateInput(attrs={'class':'form-control ','pattern=': '\d{4}-\d{2}-\d{2}', 'lang': 'pl', 'format': 'yyyy-mm-dd','type':'date'}),
            'date_of_spinning': forms.DateInput(attrs={'class':'form-control ','pattern=': '\d{4}-\d{2}-\d{2}', 'lang': 'pl', 'format': 'yyyy-mm-dd','type':'date'}),
            'date_of_cocoon_assesment': forms.DateInput(attrs={'class':'form-control ','pattern=': '\d{4}-\d{2}-\d{2}', 'lang': 'pl', 'format': 'yyyy-mm-dd','type':'date'}),
            'no_of_good_cocoon_per_kg':forms.TextInput(attrs={"oninput":"this.value = this.value.replace(/[^0-9]/g, '').replace(/(\..*)\./g, '$1')"}),
            'no_of_defective_cocoon_per_kg':forms.TextInput(attrs={"oninput":"this.value = this.value.replace(/[^0-9]/g, '').replace(/(\..*)\./g, '$1')"}),
            'no_of_male_cocoon_per_kg':forms.TextInput(attrs={"oninput":"this.value = this.value.replace(/[^0-9]/g, '').replace(/(\..*)\./g, '$1')"}),
            'no_of_female_cocoon_per_kg':forms.TextInput(attrs={"oninput":"this.value = this.value.replace(/[^0-9]/g, '').replace(/(\..*)\./g, '$1')"}),
            'no_of_cocoon_per_kg':forms.TextInput(attrs={"oninput":"this.value = this.value.replace(/[^0-9]/g, '').replace(/(\..*)\./g, '$1')"}),
            'pupation':forms.TextInput(attrs={"oninput":"this.value = this.value.replace(/[^0-9]/g, '').replace(/(\..*)\./g, '$1')"}),
            'fitness_of_seed_cocoon_per_kg':forms.TextInput(attrs={"oninput":"this.value = this.value.replace(/[^a-z 0-9 A-Z]/g, '').replace(/(\..*)\./g, '$1')"}),


        }
        

class updateseedCocoonPurchaseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        self.fields["Seed_Cocoons_Purchased_or_Received_From"].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Type...',
            })
        self.fields["Seed_Cocoons_Purchased_or_Received_From"].label="Seed Cocoons Purchased / Received From"
        self.fields["Reg_Certificate_No"].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Type...',
            })
        self.fields["Reg_Certificate_No"].label="Reg. Certificate No"
        self.fields["date_of_seed_cocoon_procurement"].label="Date of Seed Cocoon Procurement"
        self.fields["actual_no_of_cocoon_per_kg"].widget.attrs.update({
            'class':'form-control',
            'placeholder':'No Decimal..',
            'id':'field4',
            })
        self.fields["actual_no_of_cocoon_per_kg"].label="Actual No. of Cocoons/ Kg "
        self.fields["Total_Qty_of_Seed_Cocoons_Procured_by_weight_kg"].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Upto Three Decimal..',
            'id':'field5',
            })
        self.fields["Total_Qty_of_Seed_Cocoons_Procured_by_weight_kg"].label="Total Qty. of Seed Cocoons Procured - by weight (Kg)"
        self.fields["Total_Qty_of_Seed_Cocoons_Procured_by_number"].widget.attrs.update({
            'class':'form-control',
            'readonly':'True',
            'id':'field6'
            })
        self.fields["Total_Qty_of_Seed_Cocoons_Procured_by_number"].label="Total Qty. of Seed Cocoons Procured - by number"
        self.fields["pupation_perc"].widget.attrs.update({
            'class':'form-control',
            'id':'pupation',
            
            })
        self.fields["pupation_perc"].label="Pupation %"
        self.fields["seed_cocoon_price_per_kg"].widget.attrs.update({
            'class':'form-control',
            'readonly':'True',
            'id':'cocoon_price',
            })
        self.fields["seed_cocoon_price_per_kg"].label="Seed Cocoon Price Per Kg (Rs)"
        self.fields["Total_Amount_Paid_to_ASR_per_Unit_rs"].widget.attrs.update({
            'class':'form-control',
            'readonly':'True',
            'id':'total',
            })
        self.fields["Total_Amount_Paid_to_ASR_per_Unit_rs"].label="Total Amount Paid to ASR/ Unit (Rs)"
        self.fields["Transaction_ID"].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Type...',
            
            })
        self.fields["Transaction_ID"].label="Transaction Id"
        self.fields["SSPC_Lot_No_Assigned"].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Type...',
            'readonly':'True',
            })
        self.fields["SSPC_Lot_No_Assigned"].label="SSPC Lot No Assigned"
        self.fields["Seed_Cocoons_Diverted_to_Other_Unit"].widget.attrs.update({
            'class':'form-control',
            
            })
        self.fields["Seed_Cocoons_Diverted_to_Other_Unit"].label="Seed Cocoons Diverted to Other Unit "
        self.fields["Actual_Qty_of_Seed_Cocoons_Diverted_to_Units_kg"].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Upto Three Decimal..',
            'id':'diverted_seed',
            })
        self.fields["Actual_Qty_of_Seed_Cocoons_Diverted_to_Units_kg"].label="Actual Qty.of Seed Cocoons Diverted to Units (kg)"
        self.fields["Actual_Qty_of_Seed_Cocoons_Diverted_to_Units_no"].widget.attrs.update({
            'class':'form-control',
            'readonly':' True',
            'id':'diverted_units',
            })
        self.fields["Actual_Qty_of_Seed_Cocoons_Diverted_to_Units_no"].label="Actual Qty.of Seed Cocoons Diverted to Units (No.)"
        self.fields["Actual_Qty_of_Seed_Cocoons_used_for_processing_kg"].widget.attrs.update({
            'class':'form-control',
            'readonly':'True',
            'id':'processing',
            })
        self.fields["Actual_Qty_of_Seed_Cocoons_used_for_processing_kg"].label="Actual Qty.of Seed Cocoons Used for Processing (kg)"
        self.fields["Actual_Qty_of_Seed_Cocoons_used_for_processing_no"].widget.attrs.update({
            'class':'form-control',
            'readonly':'True',
            'id':'processing_no',
            })
        self.fields["Actual_Qty_of_Seed_Cocoons_used_for_processing_no"].label="Actual Qty.of Seed Cocoons Used for Processing (No.)"
        
    class Meta:     
        model = seedCocoonPurchase
        fields = "__all__"
        exclude= ['unit_name']
        ordering = ['-Date']
        widgets={
            'date_of_seed_cocoon_procurement':forms.DateInput(attrs={'class':'form-control ','pattern=': '\d{4}-\d{2}-\d{2}', 'lang': 'pl', 'format': 'yyyy-mm-dd','type':'date'}),
            'Reg_Certificate_No':forms.TextInput(attrs={"oninput":"this.value = this.value.replace(/[^a-z 0-9 A-Z]/g, '').replace(/(\..*)\./g, '$1')"}),
            'Seed_Cocoons_Purchased_or_Received_From':forms.TextInput(attrs={"oninput":"this.value = this.value.replace(/[^a-z 0-9 A-Z]/g, '').replace(/(\..*)\./g, '$1')"}),
            'actual_no_of_cocoon_per_kg':forms.TextInput(attrs={"oninput":"this.value = this.value.replace(/[^0-9]/g, '').replace(/(\..*)\./g, '$1')"}),
            'Total_Qty_of_Seed_Cocoons_Procured_by_weight_kg': forms.TextInput(attrs={"oninput":"validate_procured(this)",}),
            "pupation_perc": forms.Select(attrs={"onchange":"pupation_price(this)",}),
            'seed_cocoon_price_per_kg': forms.TextInput(attrs={"onkeyup":"multi(this)",}),
            'Transaction_ID':forms.TextInput(attrs={"oninput":"this.value = this.value.replace(/[^a-z 0-9 A-Z]/g, '').replace(/(\..*)\./g, '$1')"}),
            'Actual_Qty_of_Seed_Cocoons_Diverted_to_Units_kg': forms.TextInput(attrs={"oninput":"validate_actual(this)"}),
            'Actual_Qty_of_Seed_Cocoons_Diverted_to_Units_no':forms.TextInput(attrs={"onkeyup":"validate_field14(this)"}),
            'Actual_Qty_of_Seed_Cocoons_used_for_processing_no':forms.TextInput(attrs={"onkeyup":"validate_field16(this)"}),
        }


class updateseedDflProductionAndPreservationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        self.fields["SSPC_Lot_No_Assigned"].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Type Existing Lot No..',
            'type':'text',
            'id':'lotno',
            'readonly':'True',
            })
        self.fields["SSPC_Lot_No_Assigned"].label="SSPC Lot No"
        
        self.fields["Combination"].widget.attrs.update({
            'class':'form-control',
            
            
            })
        self.fields["Combination"].label="Combination"
        self.fields["Qty_of_DFLs_Produced_by_Weight_kg"].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Upto Three Decimal..',
            'id':'mod3_f3',
            
            })
        self.fields["Qty_of_DFLs_Produced_by_Weight_kg"].label="Qty.of DFLs Produced - by Weight (Kg)"
        self.fields["Qty_of_DFLs_Produced_by_no"].widget.attrs.update({
            'class':'form-control',
           
            'readonly':'True',
            'id':'mod3_f4',
            
            })
        self.fields["Qty_of_DFLs_Produced_by_no"].label="Qty.of DFLs Produced - by Number"
        self.fields["Qty_of_DFLs_treated_by_Weight_kg"].widget.attrs.update({
            'class':'form-control',
            'id':'mod3_f5',
            'placeholder':'Upto Three Decimal',
            
            })
        self.fields["Qty_of_DFLs_treated_by_Weight_kg"].label="Qty.of DFLs Treated - by Weight (kg)"
        self.fields["Qty_of_DFLs_treated_by_no"].widget.attrs.update({
            'class':'form-control',
            'id':'mod3_f6',
            'readonly':'True',
            
            })
        self.fields["Qty_of_DFLs_treated_by_no"].label="Qty.of DFLs Treated - by Number"
        self.fields["Qty_of_Hibernated_DFLs_Preserved_by_Weight_kg"].widget.attrs.update({
            'class':'form-control',
            'readonly':'True',
             'id':'mod3_f7',

            
            })
        self.fields["Qty_of_Hibernated_DFLs_Preserved_by_Weight_kg"].label="Qty. of Hibernated DFLs Preserved - by Weight (kg)"
        self.fields["Qty_of_Hibernated_DFLs_Preserved_by_no"].widget.attrs.update({
            'class':'form-control',
            'readonly':'True',
            'id':'mod3_f8',
            
            })
        self.fields["Qty_of_Hibernated_DFLs_Preserved_by_no"].label="Qty. of Hibernated DFLs Preserved - by Number"
        self.fields["DFLs_Preserved_at_CSP_Name"].widget.attrs.update({
            'class':'form-control',
            
            
            })
        self.fields["DFLs_Preserved_at_CSP_Name"].label="DFLs Preserved at (CSP Name)"
        self.fields["Preservation_Schedule"].widget.attrs.update({
            'class':'form-control',
            
            
            })
        self.fields["Preservation_Schedule"].label="Preservation Schedule"
        self.fields["Date_of_Preservation_at_Cold_Storage"].widget.attrs.update({
            'class':'form-control',
            
            
            })
        self.fields["Date_of_Preservation_at_Cold_Storage"].label="Date of Preservation at Cold Storage"
        self.fields["Qty_of_Pierced_Cocoons_Obtained_Kg"].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Upto Three Decimal',
            'id':'mod3_f12',
            
            })
        self.fields["Qty_of_Pierced_Cocoons_Obtained_Kg"].label="Qty. of Pierced Cocoons Obtained (Kg)"
        self.fields["Sale_Proceeds_from_Pierced_Cocoons_Rs"].widget.attrs.update({
            'class':'form-control',
            'id':'mod3_f13',
            
            
            })
        self.fields["Sale_Proceeds_from_Pierced_Cocoons_Rs"].label="Sale Proceeds from Pierced Cocoons (Rs)"
        self.fields["Sale_Proceeds_from_Others_if_any_Rs"].widget.attrs.update({
            'class':'form-control',
            'placeholder':'',
            'id':'mod3_f14',
            
            })
        self.fields["Sale_Proceeds_from_Others_if_any_Rs"].label="Sale Proceeds from Others, if any (Rs)"
        

        
    class Meta:     
        model = seedDflProductionAndPreservation
        fields = "__all__"
        exclude=['unit_name']
        widgets={
             "SSPC_Lot_No_Assigned": forms.TextInput(attrs={}),
             'Qty_of_DFLs_Produced_by_Weight_kg':forms.TextInput(attrs={"oninput":"validate_dfls_produced(this)"}),
             'Qty_of_DFLs_treated_by_Weight_kg':forms.TextInput(attrs={"oninput":"validate_treated(this)"}),
             'Date_of_Preservation_at_Cold_Storage': forms.DateInput(attrs={'class':'form-control ','pattern=': '\d{4}-\d{2}-\d{2}', 'lang': 'pl', 'format': 'yyyy-mm-dd','type':'date'}),
             'Qty_of_Pierced_Cocoons_Obtained_Kg':forms.TextInput(attrs={"oninput":"validate_pierced(this)"}),
             'Sale_Proceeds_from_Pierced_Cocoons_Rs':forms.TextInput(attrs={"oninput":"validate_price(this)"}),
             'Sale_Proceeds_from_Others_if_any_Rs':forms.TextInput(attrs={"oninput":"validate_price_if(this)"}),
        }


class updatedflsReleaseAndSupplyForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        self.fields["SSPC_Lot_No_Assigned"].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Type Existing Lot No..',
            'type':'text',
            'readonly':'True',
            })
        self.fields["SSPC_Lot_No_Assigned"].label="SSPC Lot No"
        self.fields["Date_of_Release"].widget.attrs.update({
            'class':'form-control',
            
            
            })
        self.fields["Date_of_Release"].label="Date of Release"
        self.fields["DFLs_Released_kg"].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Upto Three Decimal..',
            'id':'mod4_f3',
            })
        self.fields["DFLs_Released_kg"].label="DFLs Released (kg)"
        self.fields["Preservation_Loss_Kg"].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Upto Three Decimal..',
            'id':'mod4_f4',
            
            })
        self.fields["Preservation_Loss_Kg"].label="Preservation Loss (Kg)"
        self.fields["Winnowing_Loss_Kg"].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Upto Three Decimal..',
            'id':'mod4_f5',
            
            })
        self.fields["Winnowing_Loss_Kg"].label="Winnowing Loss (Kg)"
        self.fields["DFLs_Packed_for_Supply_Kg"].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Upto Three Decimal',
            'id':'mod4_f6',
            
            })
        self.fields["DFLs_Packed_for_Supply_Kg"].label="DFLs Packed for Supply (Kg)"
        self.fields["DFLs_Packed_for_Supply_No"].widget.attrs.update({
            'class':'form-control',
            'placeholder':'No Decimal..',
            'id':'mod4_f7',
            
            })
        self.fields["DFLs_Packed_for_Supply_No"].label="DFLs Packed for Supply (No)"
        self.fields["Date_of_Supply"].widget.attrs.update({
            'class':'form-control',
            
            
            })
        self.fields["Date_of_Supply"].label="Date of Supply"
        self.fields["Supplied_to"].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Type...',
            
            })
        self.fields["Supplied_to"].label="Supplied to"
        self.fields["No_of_DFLs"].widget.attrs.update({
            'class':'form-control',
            'placeholder':'No Decimal..',
            
            })
        self.fields["No_of_DFLs"].label="No.of DFLs"
        self.fields["Amount"].widget.attrs.update({
            'class':'form-control',
            'placeholder':'No. Decimal',
            
            })
        self.fields["Amount"].label="Amount"
        self.fields["Cash_Bill_Invoice_No_Date"].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Type...',
            
            })
        self.fields["Cash_Bill_Invoice_No_Date"].label="Cash Bill/ Invoice No. & Date"
        self.fields["Remarks"].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Type...',
            
            })
        self.fields["Remarks"].label="Remarks"
        self.fields["Processing_loss"].widget.attrs.update({
            'class':'form-control',
            'placeholder':'Upto Three Decimal..',
            'id':'mod4_f15',
            
            })
        self.fields["Processing_loss"].label="Processing Loss (Gram) "
        self.fields["No_of_DFLs_for_write_off"].widget.attrs.update({
            'class':'form-control',
            'placeholder':'No Decimal..',
            
            })
        self.fields["No_of_DFLs_for_write_off"].label="No.of DFLs for Write-Off (Want of Demand)"
        
    class Meta:     
        model = dflsReleaseAndSupply
        fields = "__all__"
        exclude=['unit_name']
        widgets={
            
            'Supplied_to':forms.TextInput(attrs={"oninput":"this.value = this.value.replace(/[^A-Z a-z]/g, '').replace(/(\..*)\./g, '$1')"}),
            'No_of_DFLs':forms.TextInput(attrs={"oninput":"this.value = this.value.replace(/[^0-9]/g, '').replace(/(\..*)\./g, '$1')"}),
            'No_of_DFLs_for_write_off':forms.TextInput(attrs={"oninput":"this.value = this.value.replace(/[^0-9]/g, '').replace(/(\..*)\./g, '$1')"}),
            'Amount':forms.TextInput(attrs={"oninput":"this.value = this.value.replace(/[^0-9]/g, '').replace(/(\..*)\./g, '$1')"}),
            'Remarks':forms.TextInput(attrs={"oninput":"this.value = this.value.replace(/[^A-Z a-z0-9]/g, '').replace(/(\..*)\./g, '$1')"}),

            'Date_of_Release': forms.DateInput(attrs={'class':'form-control ','pattern=': '\d{4}-\d{2}-\d{2}', 'lang': 'pl', 'format': 'yyyy-mm-dd','type':'date'}),
            'Date_of_Supply': forms.DateInput(attrs={'class':'form-control ','pattern=': '\d{4}-\d{2}-\d{2}', 'lang': 'pl', 'format': 'yyyy-mm-dd','type':'date'}),

            'DFLs_Packed_for_Supply_No':forms.TextInput(attrs={"oninput":"this.value = this.value.replace(/[^0-9]/g, '').replace(/(\..*)\./g, '$1')"}),
            # "SSPC_Lot_No_Assigned": forms.TextInput(attrs={}),
            "DFLs_Released_kg":forms.TextInput(attrs={"oninput":"DFLs_Released(this)"}),
            "Preservation_Loss_Kg":forms.TextInput(attrs={"oninput":"Preservation_Loss(this)"}),
            "Winnowing_Loss_Kg":forms.TextInput(attrs={"oninput":"Winnowing_Loss(this)"}),
            "DFLs_Packed_for_Supply_Kg":forms.TextInput(attrs={"oninput":"DFLs_Packed_for_Supply(this)"}),
            "Processing_loss":forms.TextInput(attrs={"oninput":"Processing_gm(this)"}),
        }
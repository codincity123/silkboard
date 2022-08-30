from secrets import choice
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete

# Create your models here.
class Profile(models.Model):
	unit_name=models.OneToOneField(User,on_delete=models.CASCADE)
	unit_runs_by=models.CharField(max_length=50)
	unit_created_at=models.DateField(null=True)
	contact=models.CharField(max_length=12,null=True)
	weekly_target=models.PositiveIntegerField(null=True)
	monthly_target=models.PositiveIntegerField(null=True)
	address=models.CharField(max_length=80,null=True)
	address2=models.CharField(max_length=80,null=True)
	city=models.CharField(max_length=50,null=True)
	zipcode=models.CharField(max_length=6,null=True)
	state_choices = (("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))
	state=models.CharField(max_length=80,choices = state_choices,null=True)
	Date=models.DateField(auto_now_add=True)
	def __str__(self):
		return str(self.unit_name)

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
	if created:
		Profile.objects.create(unit_name=instance)


class seedCropPerformance(models.Model):
	race_data = (("CSR2","CSR2"),("CSR4","CSR4"),("CSR6","CSR6"),("CSR16","CSR16"),("CSR26","CSR26"),("CSR27","CSR27"),("FC1","FC1"),("FC2","FC2"),("SK6","SK6"),("SK7","SK7"),("SK6 X SK7","SK6 X SK7"),("NISTRAI","NISTARI"),("BCON1","BCON1"),("BCON4","BCON4"),("PURE MYSORE","PURE MYSORE"),("NB4D2","NB4D2"),("SH6","SH6"),("G11","G11"),("G19","G19"),("MV1","MV1"),("S8","S8"))
	unit_name=models.ForeignKey(User, on_delete=models.CASCADE)
	Name_of_the_Adopted_Seed_Rearer=models.CharField(max_length=50)
	Reg_Certificate_No_of_ASR=models.CharField(max_length=50,null=True)
	p1_seed_lot_no=models.CharField(max_length=50,primary_key=True)
	p1_race=models.CharField(choices=race_data,max_length=20)
	no_of_dfls_brushed=models.PositiveIntegerField()
	date_of_hatching=models.DateField(auto_now=False,auto_now_add=False)
	date_of_spinning=models.DateField(auto_now=False,auto_now_add=False)
	hatching=models.DecimalField(max_digits=5,decimal_places=1)
	seed_crop_inspected_by=models.CharField(max_length=50)
	seed_crop_remarks=models.CharField(max_length=80)
	date_of_cocoon_assesment=models.DateField(auto_now=False,auto_now_add=False)
	cocoon_yield_per_100dfls=models.DecimalField(max_digits=9,decimal_places=1)
	no_of_cocoon_per_kg=models.PositiveIntegerField()
	no_of_good_cocoon_per_kg=models.PositiveIntegerField()
	no_of_defective_cocoon_per_kg=models.PositiveIntegerField()
	no_of_male_cocoon_per_kg=models.PositiveIntegerField()
	no_of_female_cocoon_per_kg=models.PositiveIntegerField()
	pupation=models.PositiveIntegerField()
	fitness_of_seed_cocoon_per_kg=models.CharField(max_length=50)
	Date=models.DateField(auto_now_add=True)

	class Meta:
		ordering = ['-Date']

	def __str__(self):
		return str(self.p1_seed_lot_no)


class seedCocoonPurchase(models.Model):
	cocoon_divert=(("SSPC - Bangalore","SSPC - Bangalore"),("SSPC - Berhampore","SSPC - Berhampore"),("SSPC - Chintamani","SSPC - Chintamani"),("SSPC - Dakshibhavanipur","SSPC - Dakshibhavanipur"),("SSPC - Dehradun","SSPC - Dehradun"),("SSPC - Dharmapuri","SSPC - Dharmapuri"),("SSPC - Hindupur","SSPC - Hindupur"),("SSPC - Hosur","SSPC - Hosur"),("SSPC - Jorhat","SSPC - Jorhat"),("SSPC - K.R. Nagar","SSPC - K.R. Nagar"),("SSPC - Malavalli","SSPC - Malavalli"),("SSPC - Mysore","SSPC - Mysore"),("SSPC - Palakkad","SSPC - Palakkad"),("SSPC- Ramanagaram","SSPC- Ramanagaram"),("SSPC - Udhampur","SSPC - Udhampur"),("SSPC - Vijayapura","SSPC - Vijayapura"),("None","None"))
	choice_pupation=(("80","80"),("81","81"),("82","82"),("83","83"),("84","84"),("85","85"),("86","86"),("87","87"),("88","88"),("89","89"),("90","90"),("91","91"),("92","92"),("93","93"),("94","94"),("95","95"),("96-100","96-100"))
	Seed_Cocoons_Purchased_or_Received_From=models.CharField(max_length=50)
	Reg_Certificate_No=models.CharField(max_length=50)
	date_of_seed_cocoon_procurement=models.DateField(auto_now=False,auto_now_add=False)
	actual_no_of_cocoon_per_kg=models.PositiveIntegerField()
	Total_Qty_of_Seed_Cocoons_Procured_by_weight_kg=models.DecimalField(max_digits=10,decimal_places=3)
	Total_Qty_of_Seed_Cocoons_Procured_by_number=models.PositiveIntegerField()
	pupation_perc=models.CharField(choices=choice_pupation,max_length=25)
	seed_cocoon_price_per_kg=models.PositiveIntegerField()
	Total_Amount_Paid_to_ASR_per_Unit_rs=models.PositiveIntegerField()
	Transaction_ID=models.CharField(max_length=50)
	SSPC_Lot_No_Assigned=models.CharField(max_length=50,primary_key=True)
	Seed_Cocoons_Diverted_to_Other_Unit=models.CharField(max_length=80,choices=cocoon_divert)
	Actual_Qty_of_Seed_Cocoons_Diverted_to_Units_kg=models.DecimalField(max_digits=10,decimal_places=3)
	Actual_Qty_of_Seed_Cocoons_Diverted_to_Units_no=models.PositiveIntegerField()
	Actual_Qty_of_Seed_Cocoons_used_for_processing_kg=models.DecimalField(max_digits=10,decimal_places=3)
	Actual_Qty_of_Seed_Cocoons_used_for_processing_no=models.PositiveIntegerField()
	Date=models.DateField(auto_now_add=True)
	unit_name=models.ForeignKey(User, on_delete=models.CASCADE,null=True)

	class Meta:
		ordering = ['-Date']
	def __str__(self):
		return str(self.SSPC_Lot_No_Assigned)


class seedDflProductionAndPreservation(models.Model):
	
	cold_storage=(
		("CSP-Mysore","CSP-Mysore"),("CSP-Hosur","CSP-Hosur"),("CSP- Jorhat","CSP- Jorhat"),("CSP- Dehradun","CSP- Dehradun")
	)
	preservation_schd=(
		("3 Months","3 Months"),("4 Months","4 Months"),("6 Months","6 Months"),("10 Months","10 Months")
	)
	
	SSPC_Lot_No_Assigned=models.OneToOneField(seedCocoonPurchase,to_field="SSPC_Lot_No_Assigned",on_delete=models.CASCADE)
	hybrid=(("CSR2 X CSR4","CSR2 X CSR4"),("CSR4 X CSR2","CSR4 X CSR2"),("FC1 X FC2","FC1 X FC2"),("FC2 X FC1","FC2 X FC1"),("G11 X G19","G11 X G19"),("G19 X G11","G19 X G11"),("SH6 X NB4D2","SH6 X NB4D2"),("NB4D2 X SH6","NB4D2 X SH6 "),("MV1 X S8","MV1 X S8"),("CSR16 X S8","CSR16 X S8"))
	Combination=models.CharField(max_length=80,choices=hybrid)
	Qty_of_DFLs_Produced_by_Weight_kg=models.DecimalField(max_digits=10,decimal_places=3)
	Qty_of_DFLs_Produced_by_no=models.PositiveIntegerField()
	Qty_of_DFLs_treated_by_Weight_kg=models.DecimalField(max_digits=10,decimal_places=3)
	Qty_of_DFLs_treated_by_no=models.PositiveIntegerField()
	Qty_of_Hibernated_DFLs_Preserved_by_Weight_kg=models.DecimalField(max_digits=10,decimal_places=3)
	Qty_of_Hibernated_DFLs_Preserved_by_no=models.PositiveIntegerField()
	DFLs_Preserved_at_CSP_Name=models.CharField(max_length=50,choices=cold_storage)
	Preservation_Schedule=models.CharField(max_length=50, choices=preservation_schd)
	Date_of_Preservation_at_Cold_Storage=models.DateField(auto_now=False,auto_now_add=False)
	Qty_of_Pierced_Cocoons_Obtained_Kg=models.DecimalField(max_digits=10,decimal_places=3)
	Sale_Proceeds_from_Pierced_Cocoons_Rs=models.PositiveIntegerField()
	Sale_Proceeds_from_Others_if_any_Rs=models.PositiveIntegerField()
	Date=models.DateField(auto_now_add=True)
	unit_name=models.ForeignKey(User, on_delete=models.CASCADE,null=True)


	class Meta:
		ordering = ['-Date']
	def __str__(self):
		return str(self.SSPC_Lot_No_Assigned)



class dflsReleaseAndSupply(models.Model):
	SSPC_Lot_No_Assigned=models.ForeignKey(seedDflProductionAndPreservation, on_delete=models.CASCADE,null=True)
	Date_of_Release=models.DateField(auto_now=False,auto_now_add=False)
	DFLs_Released_kg=models.DecimalField(max_digits=10,decimal_places=3)
	Preservation_Loss_Kg=models.DecimalField(max_digits=10,decimal_places=3)
	Winnowing_Loss_Kg=models.DecimalField(max_digits=10,decimal_places=3)
	DFLs_Packed_for_Supply_Kg=models.DecimalField(max_digits=10,decimal_places=3)
	DFLs_Packed_for_Supply_No=models.PositiveIntegerField()
	Date_of_Supply=models.DateField(auto_now=False,auto_now_add=False)
	Supplied_to=models.CharField(max_length=50)
	No_of_DFLs=models.PositiveIntegerField()
	Amount=models.PositiveIntegerField()
	Cash_Bill_Invoice_No_Date=models.CharField(max_length=80)
	Remarks=models.CharField(max_length=100)
	Processing_loss=models.DecimalField(max_digits=10,decimal_places=3)
	No_of_DFLs_for_write_off=models.PositiveIntegerField()
	Date=models.DateField(auto_now_add=True)
	unit_name=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	class Meta:
		ordering = ['-Date']
	def __str__(self):
		return str(self.SSPC_Lot_No_Assigned)

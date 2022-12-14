# Generated by Django 3.2 on 2022-04-26 06:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='seedCocoonPurchase',
            fields=[
                ('Seed_Cocoons_Purchased_or_Received_From', models.CharField(max_length=50)),
                ('Reg_Certificate_No', models.CharField(max_length=50)),
                ('date_of_seed_cocoon_procurement', models.DateField()),
                ('actual_no_of_cocoon_per_kg', models.PositiveIntegerField()),
                ('Total_Qty_of_Seed_Cocoons_Procured_by_weight_kg', models.DecimalField(decimal_places=3, max_digits=10)),
                ('Total_Qty_of_Seed_Cocoons_Procured_by_number', models.PositiveIntegerField()),
                ('pupation_perc', models.CharField(choices=[('80', '80'), ('81', '81'), ('82', '82'), ('83', '83'), ('84', '84'), ('85', '85'), ('86', '86'), ('87', '87'), ('88', '88'), ('89', '89'), ('90', '90'), ('91', '91'), ('92', '92'), ('93', '93'), ('94', '94'), ('95', '95'), ('96-100', '96-100')], max_length=25)),
                ('seed_cocoon_price_per_kg', models.PositiveIntegerField()),
                ('Total_Amount_Paid_to_ASR_per_Unit_rs', models.PositiveIntegerField()),
                ('Transaction_ID', models.CharField(max_length=50)),
                ('SSPC_Lot_No_Assigned', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('Seed_Cocoons_Diverted_to_Other_Unit', models.CharField(choices=[('SSPC - Bangalore', 'SSPC - Bangalore'), ('SSPC - Berhampore', 'SSPC - Berhampore'), ('SSPC - Chintamani', 'SSPC - Chintamani'), ('SSPC - Dakshibhavanipur', 'SSPC - Dakshibhavanipur'), ('SSPC - Dehradun', 'SSPC - Dehradun'), ('SSPC - Dharmapuri', 'SSPC - Dharmapuri'), ('SSPC - Hindupur', 'SSPC - Hindupur'), ('SSPC - Hosur', 'SSPC - Hosur'), ('SSPC - Jorhat', 'SSPC - Jorhat'), ('SSPC - K.R. Nagar', 'SSPC - K.R. Nagar'), ('SSPC - Malavalli', 'SSPC - Malavalli'), ('SSPC - Mysore', 'SSPC - Mysore'), ('SSPC - Palakkad', 'SSPC - Palakkad'), ('SSPC- Ramanagaram', 'SSPC- Ramanagaram'), ('SSPC - Udhampur', 'SSPC - Udhampur'), ('SSPC - Vijayapura', 'SSPC - Vijayapura')], max_length=80)),
                ('Actual_Qty_of_Seed_Cocoons_Diverted_to_Units_kg', models.DecimalField(decimal_places=3, max_digits=10)),
                ('Actual_Qty_of_Seed_Cocoons_Diverted_to_Units_no', models.PositiveIntegerField()),
                ('Actual_Qty_of_Seed_Cocoons_used_for_processing_kg', models.DecimalField(decimal_places=3, max_digits=10)),
                ('Actual_Qty_of_Seed_Cocoons_used_for_processing_no', models.PositiveIntegerField()),
                ('Date', models.DateField(auto_now_add=True)),
                ('unit_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-Date'],
            },
        ),
        migrations.CreateModel(
            name='seedDflProductionAndPreservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Combination', models.CharField(choices=[('CSR2 X CSR4', 'CSR2 X CSR4'), ('CSR4 X CSR2', 'CSR4 X CSR2'), ('FC1 X FC2', 'FC1 X FC2'), ('FC2 X FC1', 'FC2 X FC1'), ('G11 X G19', 'G11 X G19'), ('G19 X G11', 'G19 X G11'), ('SH6 X NB4D2', 'SH6 X NB4D2'), ('NB4D2 X SH6', 'NB4D2 X SH6 '), ('MV1 X S8', 'MV1 X S8'), ('CSR16 X S8', 'CSR16 X S8')], max_length=80)),
                ('Qty_of_DFLs_Produced_by_Weight_kg', models.DecimalField(decimal_places=3, max_digits=10)),
                ('Qty_of_DFLs_Produced_by_no', models.PositiveIntegerField()),
                ('Qty_of_DFLs_treated_by_Weight_kg', models.DecimalField(decimal_places=3, max_digits=10)),
                ('Qty_of_DFLs_treated_by_no', models.PositiveIntegerField()),
                ('Qty_of_Hibernated_DFLs_Preserved_by_Weight_kg', models.DecimalField(decimal_places=3, max_digits=10)),
                ('Qty_of_Hibernated_DFLs_Preserved_by_no', models.PositiveIntegerField()),
                ('DFLs_Preserved_at_CSP_Name', models.CharField(choices=[('CSP-Mysore', 'CSP-Mysore'), ('CSP-Hosur', 'CSP-Hosur'), ('CSP- Jorhat', 'CSP- Jorhat'), ('CSP- Dehradun', 'CSP- Dehradun')], max_length=50)),
                ('Preservation_Schedule', models.CharField(choices=[('3 Months', '3 Months'), ('4 Months', '4 Months'), ('6 Months', '6 Months'), ('10 Months', '10 Months')], max_length=50)),
                ('Date_of_Preservation_at_Cold_Storage', models.DateField()),
                ('Qty_of_Pierced_Cocoons_Obtained_Kg', models.DecimalField(decimal_places=3, max_digits=10)),
                ('Sale_Proceeds_from_Pierced_Cocoons_Rs', models.PositiveIntegerField()),
                ('Sale_Proceeds_from_Others_if_any_Rs', models.PositiveIntegerField()),
                ('Date', models.DateField(auto_now_add=True)),
                ('SSPC_Lot_No_Assigned', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='silk.seedcocoonpurchase')),
                ('unit_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-Date'],
            },
        ),
        migrations.CreateModel(
            name='seedCropPerformance',
            fields=[
                ('Name_of_the_Adopted_Seed_Rearer', models.CharField(max_length=50)),
                ('Reg_Certificate_No_of_ASR', models.CharField(max_length=50, null=True)),
                ('p1_seed_lot_no', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('p1_race', models.CharField(choices=[('CSR2', 'CSR2'), ('CSR4', 'CSR4'), ('CSR6', 'CSR6'), ('CSR16', 'CSR16'), ('CSR26', 'CSR26'), ('CSR27', 'CSR27'), ('FC1', 'FC1'), ('FC2', 'FC2'), ('SK6', 'SK6'), ('SK7', 'SK7'), ('SK6 X SK7', 'SK6 X SK7'), ('NISTRAI', 'NISTARI'), ('BCON1', 'BCON1'), ('BCON4', 'BCON4'), ('PURE MYSORE', 'PURE MYSORE'), ('NB4D2', 'NB4D2'), ('SH6', 'SH6'), ('G11', 'G11'), ('G19', 'G19'), ('MV1', 'MV1'), ('S8', 'S8')], max_length=20)),
                ('no_of_dfls_brushed', models.PositiveIntegerField()),
                ('date_of_hatching', models.DateField()),
                ('date_of_spinning', models.DateField()),
                ('hatching', models.DecimalField(decimal_places=1, max_digits=5)),
                ('seed_crop_inspected_by', models.CharField(max_length=50)),
                ('seed_crop_remarks', models.CharField(max_length=80)),
                ('date_of_cocoon_assesment', models.DateField()),
                ('cocoon_yield_per_100dfls', models.DecimalField(decimal_places=1, max_digits=9)),
                ('no_of_cocoon_per_kg', models.PositiveIntegerField()),
                ('no_of_good_cocoon_per_kg', models.PositiveIntegerField()),
                ('no_of_defective_cocoon_per_kg', models.PositiveIntegerField()),
                ('no_of_male_cocoon_per_kg', models.PositiveIntegerField()),
                ('no_of_female_cocoon_per_kg', models.PositiveIntegerField()),
                ('pupation', models.PositiveIntegerField()),
                ('fitness_of_seed_cocoon_per_kg', models.CharField(max_length=50)),
                ('Date', models.DateField(auto_now_add=True)),
                ('unit_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-Date'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_runs_by', models.CharField(max_length=50)),
                ('unit_created_at', models.DateField(null=True)),
                ('contact', models.CharField(max_length=12, null=True)),
                ('weekly_target', models.PositiveIntegerField(null=True)),
                ('monthly_target', models.PositiveIntegerField(null=True)),
                ('address', models.CharField(max_length=80, null=True)),
                ('address2', models.CharField(max_length=80, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('zipcode', models.CharField(max_length=6, null=True)),
                ('state', models.CharField(choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh ', 'Arunachal Pradesh '), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu and Kashmir ', 'Jammu and Kashmir '), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal'), ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'), ('Chandigarh', 'Chandigarh'), ('Dadra and Nagar Haveli', 'Dadra and Nagar Haveli'), ('Daman and Diu', 'Daman and Diu'), ('Lakshadweep', 'Lakshadweep'), ('National Capital Territory of Delhi', 'National Capital Territory of Delhi'), ('Puducherry', 'Puducherry')], max_length=80, null=True)),
                ('Date', models.DateField(auto_now_add=True)),
                ('unit_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='dflsReleaseAndSupply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_of_Release', models.DateField()),
                ('DFLs_Released_kg', models.DecimalField(decimal_places=3, max_digits=10)),
                ('Preservation_Loss_Kg', models.DecimalField(decimal_places=3, max_digits=10)),
                ('Winnowing_Loss_Kg', models.DecimalField(decimal_places=3, max_digits=10)),
                ('DFLs_Packed_for_Supply_Kg', models.DecimalField(decimal_places=3, max_digits=10)),
                ('DFLs_Packed_for_Supply_No', models.PositiveIntegerField()),
                ('Date_of_Supply', models.DateField()),
                ('Supplied_to', models.CharField(max_length=50)),
                ('No_of_DFLs', models.PositiveIntegerField()),
                ('Amount', models.PositiveIntegerField()),
                ('Cash_Bill_Invoice_No_Date', models.CharField(max_length=80)),
                ('Remarks', models.CharField(max_length=100)),
                ('Processing_loss', models.DecimalField(decimal_places=3, max_digits=10)),
                ('No_of_DFLs_for_write_off', models.PositiveIntegerField()),
                ('Date', models.DateField(auto_now_add=True)),
                ('SSPC_Lot_No_Assigned', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='silk.seeddflproductionandpreservation')),
                ('unit_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-Date'],
            },
        ),
    ]

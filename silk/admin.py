from django.contrib import admin
from django.contrib.auth.models import User
from .models import *

# Register your models here.
admin.site.register(Profile)

admin.site.register(seedCropPerformance)
admin.site.register(seedCocoonPurchase)
admin.site.register(seedDflProductionAndPreservation)
admin.site.register(dflsReleaseAndSupply)
 
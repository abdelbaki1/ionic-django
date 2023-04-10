from django.contrib import admin
from .models import (
    Vehicle, UtilityVehicle, TouristVehicle, LuxuryVehicle, Driver, RentalAgency,
    Rental, Payment, BankAccount, Insurance, TechnicalInspection, VehicleStatus,
    RentalDuration, LocationAgency, Incident, QuarterlyStatistics, Reminder
)

# Register the models
admin.site.register(Vehicle)
admin.site.register(UtilityVehicle)
admin.site.register(TouristVehicle)
admin.site.register(LuxuryVehicle)
admin.site.register(Driver)
admin.site.register(RentalAgency)
admin.site.register(Rental)
admin.site.register(Payment)
admin.site.register(BankAccount)
admin.site.register(Insurance)
admin.site.register(TechnicalInspection)
admin.site.register(VehicleStatus)
admin.site.register(RentalDuration)
admin.site.register(LocationAgency)
admin.site.register(Incident)
admin.site.register(QuarterlyStatistics)
admin.site.register(Reminder)

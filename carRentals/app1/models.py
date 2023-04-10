from django.db import models
from django.contrib.auth.models import AbstractUser

class Vehicle(models.Model):
    id = models.AutoField(primary_key=True)
    license_plate = models.CharField(max_length=10)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    type = models.CharField(max_length=50)

    # class Meta:
    #     abstract = True


class UtilityVehicle(Vehicle):
    pass


class TouristVehicle(Vehicle):
    pass


class LuxuryVehicle(Vehicle):
    driver = models.ForeignKey('Driver', on_delete=models.CASCADE)


class Driver(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class RentalAgency(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)


class Rental(models.Model):
    id = models.AutoField(primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField()
    duration = models.ForeignKey('RentalDuration', on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True)
    agency = models.ForeignKey(RentalAgency, on_delete=models.CASCADE)


class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.FloatField()
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
    bank_account = models.ForeignKey('BankAccount', on_delete=models.CASCADE)


class BankAccount(models.Model):
    id = models.AutoField(primary_key=True)
    bank_name = models.CharField(max_length=50)


class Insurance(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)


class TechnicalInspection(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)


class VehicleStatus(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    mileage = models.FloatField()
    fuel_level = models.FloatField()
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)


class RentalDuration(models.Model):
    hours = models.IntegerField()
    days = models.IntegerField()


class LocationAgency(models.Model):
    rental_agency = models.OneToOneField(RentalAgency, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()


class Incident(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    description = models.TextField()


class QuarterlyStatistics(models.Model):
    vehicles = models.ManyToManyField(Vehicle)
    rentals = models.ManyToManyField(Rental)
    incidents = models.ManyToManyField(Incident)
    payments = models.ManyToManyField(Payment)


class Reminder(models.Model):
    date = models.DateField()
    description = models.TextField()
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE, null=True)
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE, null=True)
    technical_inspection = models.ForeignKey(TechnicalInspection, on_delete=models.CASCADE, null=True)

class token(models.Model):
    # user = models.ForeignKey(AbstractUser, on_delete=models.CASCADE)
    user_token = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.user_token
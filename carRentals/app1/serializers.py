from .models import Vehicle, UtilityVehicle, TouristVehicle, LuxuryVehicle, Driver, RentalAgency, Rental, Payment, BankAccount, Insurance, TechnicalInspection, VehicleStatus, RentalDuration, LocationAgency, Incident, QuarterlyStatistics, Reminder
from rest_framework import serializers

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class UtilityVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UtilityVehicle
        fields = '__all__'

class TouristVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TouristVehicle
        fields = '__all__'

class LuxuryVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = LuxuryVehicle
        fields = '__all__'

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'

class RentalAgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = RentalAgency
        fields = '__all__'

class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = '__all__'

class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = '__all__'

class TechnicalInspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicalInspection
        fields = '__all__'

class VehicleStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleStatus
        fields = '__all__'

class RentalDurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentalDuration
        fields = '__all__'

class LocationAgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationAgency
        fields = '__all__'

class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = '__all__'

class QuarterlyStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuarterlyStatistics
        fields = '__all__'

class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = '__all__'

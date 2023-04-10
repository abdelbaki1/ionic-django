from .serializers import VehicleSerializer
from django.shortcuts import render
from .models import UtilityVehicle, TouristVehicle, LuxuryVehicle, Driver, RentalAgency, Rental
from .serializers import VehicleSerializer, DriverSerializer, RentalAgencySerializer, RentalSerializer
from .models import Payment, BankAccount, Insurance, TechnicalInspection, VehicleStatus, RentalDuration
from .serializers import PaymentSerializer, BankAccountSerializer, InsuranceSerializer, TechnicalInspectionSerializer, VehicleStatusSerializer, RentalDurationSerializer
from rest_framework.filters import SearchFilter
from .models import (UtilityVehicle, TouristVehicle, LuxuryVehicle, Driver,
                     RentalAgency, Rental, Payment, BankAccount, Insurance,
                     TechnicalInspection, Vehicle, VehicleStatus, RentalDuration,
                     LocationAgency, Incident, QuarterlyStatistics, Reminder)
from .serializers import (UtilityVehicleSerializer, TouristVehicleSerializer,
                          LuxuryVehicleSerializer, DriverSerializer,
                          RentalAgencySerializer, RentalSerializer, PaymentSerializer,
                          BankAccountSerializer, InsuranceSerializer,
                          TechnicalInspectionSerializer, VehicleStatusSerializer,
                          RentalDurationSerializer, LocationAgencySerializer,
                          IncidentSerializer, QuarterlyStatisticsSerializer,
                          ReminderSerializer)
from django.contrib.auth.mixins import PermissionRequiredMixin
from .auth import JWTAuthentication
from .pagination import CustomPagination
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import generics, mixins, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import ListModelMixin, CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin


class GenericVehicleView(GenericAPIView):
    model: str = "Vehicle"
    authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class VehicleListView(GenericVehicleView, generics.ListCreateAPIView):
    # permission_required = ('view_vehicle')
    pagination_class = CustomPagination
    # permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]


class VehicleView(GenericVehicleView,
                  CreateModelMixin,
                  UpdateModelMixin,
                  RetrieveModelMixin,
                  DestroyModelMixin,
                  ):
    permission_classes = [IsAuthenticated]
    lookup_field = "id"
    lookup_url_kwarg = "pk"

    def post(self, request, *args, **kwargs):
        if (self.has_permission()):
            # user_activity_signal.send(
            #     sender=self.request.user, activity='have created a vehicle')
            return self.create(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def put(self, request, *args, **kwargs):
        # user_activity_signal.send(
        #     sender=self.request.user, activity='have updated a vehicle')
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        # print(request.user.user_permissions.all())
        # user_activity_signal.send(
            # sender=self.request.user, activity='have deleted a vehicle')
        return self.destroy(request, *args, **kwargs)


class PaymentListView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]


class PaymentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]


class BankAccountListView(generics.ListAPIView):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
    permission_classes = [permissions.IsAuthenticated]


class BankAccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer
    permission_classes = [permissions.IsAuthenticated]


class InsuranceListView(generics.ListCreateAPIView):
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer
    permission_classes = [permissions.IsAuthenticated]


class InsuranceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer
    permission_classes = [permissions.IsAuthenticated]


class TechnicalInspectionListView(generics.ListAPIView):
    queryset = TechnicalInspection.objects.all()
    serializer_class = TechnicalInspectionSerializer
    permission_classes = [permissions.IsAuthenticated]


class TechnicalInspectionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TechnicalInspection.objects.all()
    serializer_class = TechnicalInspectionSerializer
    permission_classes = [permissions.IsAuthenticated]


class VehicleStatusListView(generics.ListCreateAPIView):
    queryset = VehicleStatus.objects.all()
    serializer_class = VehicleStatusSerializer
    permission_classes = [permissions.IsAuthenticated]


class VehicleStatusDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VehicleStatus.objects.all()
    serializer_class = VehicleStatusSerializer
    permission_classes = [permissions.IsAuthenticated]


class RentalDurationListView(generics.ListAPIView):
    queryset = RentalDuration.objects.all()
    serializer_class = RentalDurationSerializer
    permission_classes = [permissions.IsAuthenticated]


class RentalDurationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RentalDuration.objects.all()
    serializer_class = InsuranceSerializer
    permission_classes = [permissions.IsAuthenticated]

# UtilityVehicle views


class UtilityVehicleListCreateView(generics.ListCreateAPIView):
    queryset = UtilityVehicle.objects.all()
    serializer_class = UtilityVehicleSerializer
    filter_backends = [SearchFilter]
    search_fields = ['license_plate', 'brand', 'model', 'type']


class UtilityVehicleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UtilityVehicle.objects.all()
    serializer_class = UtilityVehicleSerializer


# TouristVehicle views

class TouristVehicleListCreateView(generics.ListCreateAPIView):
    queryset = TouristVehicle.objects.all()
    serializer_class = TouristVehicleSerializer
    filter_backends = [SearchFilter]
    search_fields = ['license_plate', 'brand', 'model', 'type']


class TouristVehicleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TouristVehicle.objects.all()
    serializer_class = TouristVehicleSerializer


# LuxuryVehicle views

class LuxuryVehicleListCreateView(generics.ListCreateAPIView):
    queryset = LuxuryVehicle.objects.all()
    serializer_class = LuxuryVehicleSerializer
    filter_backends = [SearchFilter]
    search_fields = ['license_plate', 'brand', 'model',
                     'type', 'driver__first_name', 'driver__last_name']


class LuxuryVehicleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LuxuryVehicle.objects.all()
    serializer_class = LuxuryVehicleSerializer


# Driver views

class DriverListCreateView(generics.ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    filter_backends = [SearchFilter]
    search_fields = ['first_name', 'last_name']


class DriverRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


# RentalAgency views

class RentalAgencyListCreateView(generics.ListCreateAPIView):
    queryset = RentalAgency.objects.all()
    serializer_class = RentalAgencySerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'address']


class RentalAgencyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RentalAgency.objects.all()
    serializer_class = RentalAgencySerializer


# Rental views

class RentalListCreateView(generics.ListCreateAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    filter_backends = [SearchFilter]
    search_fields = ['vehicle__license_plate', 'vehicle__brand', 'vehicle__model',
                     'vehicle__type', 'driver__first_name', 'driver__last_name',
                     'agency__name', 'agency__address']


class RentalRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer


class LocationAgencyListCreateView(generics.ListCreateAPIView):
    queryset = LocationAgency.objects.all()
    serializer_class = LocationAgencySerializer


class LocationAgencyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LocationAgency.objects.all()
    serializer_class = LocationAgencySerializer


class IncidentListCreateView(generics.ListCreateAPIView):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer


class IncidentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer


class QuarterlyStatisticsListCreateView(generics.ListCreateAPIView):
    queryset = QuarterlyStatistics.objects.all()
    serializer_class = QuarterlyStatisticsSerializer


class QuarterlyStatisticsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuarterlyStatistics.objects.all()
    serializer_class = QuarterlyStatisticsSerializer


class QuarterlyStatisticsListCreateView(generics.ListCreateAPIView):
    queryset = QuarterlyStatistics.objects.all()
    serializer_class = QuarterlyStatisticsSerializer


class QuarterlyStatisticsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuarterlyStatistics.objects.all()
    serializer_class = QuarterlyStatisticsSerializer


class ReminderListCreateView(generics.ListCreateAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer


class ReminderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer

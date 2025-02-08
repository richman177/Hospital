from .serializers import *
from .models import *
from rest_framework import viewsets, generics,status
from .filters import DepartmentFilter, SpecialtyFilter, DoctorFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
# from .permissions import CheckDoctor


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = DepartmentFilter
    search_fields = ['department_name']


class SpecialtyViewSet(viewsets.ModelViewSet):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = SpecialtyFilter
    search_fields = ['specialty_name']


class DoctorListAPIView(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorListSerializer
    filterset_class = DoctorFilter
    filter_backends = [DjangoFilterBackend, OrderingFilter]


class DoctorDetailAPIView(generics.RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorDetailSerializer


class DoctorCreateAPIView(generics.CreateAPIView):
    serializer_class = DoctorCreateSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class AppointmentListAPIView(generics.ListAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentListSerializer


class AppointmentDetailAPIView(generics.RetrieveAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentDetailSerializer


class AppointmentCreateAPIView(generics.CreateAPIView):
    serializer_class = AppointmentCreateSerializer


class MedicalRecordListAPIView(generics.ListAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordListSerializer
    # permission_classes = [CheckDoctor]



class MedicalRecordDetailAPIView(generics.RetrieveAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordDetailSerializer
    # permission_classes = [CheckDoctor]



class MedicalRecordCreateAPIView(generics.CreateAPIView):
    serializer_class = MedicalRecordCreateSerializer
    # permission_classes = [CheckDoctor]


class FeedbackListAPIView(generics.ListAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackListSerializer


class FeedbackDetailAPIView(generics.RetrieveAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackDetailSerializer


class FeedbackCreateAPIView(generics.CreateAPIView):
    serializer_class = FeedbackCreateSerializer


class WardViewSet(viewsets.ModelViewSet):
    queryset = Ward.objects.all()
    serializer_class = WardSerializer
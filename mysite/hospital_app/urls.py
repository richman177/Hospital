from .views import *
from django.urls import path, include
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'users', UserProfileViewSet, basename='users'),
router.register(r'specialty', SpecialtyViewSet, basename='specialty'),
router.register(r'patient', PatientViewSet, basename='patient'),
router.register(r'ward', WardViewSet, basename='ward'),

urlpatterns = [
    path('', include(router.urls)),
    path('doctor/', DoctorListAPIView.as_view(), name='doctor_list'),
    path('doctor/<int:pk>/', DoctorDetailAPIView.as_view(), name='doctor_detail'),
    path('doctor/create/', DoctorCreateAPIView.as_view(), name='doctor_create'),

    path('appointment/', AppointmentListAPIView.as_view(), name='appointment_list'),
    path('appointment/<int:pk>/', AppointmentDetailAPIView.as_view(), name='appointment_detail'),
    path('appointment/create/', AppointmentCreateAPIView.as_view(), name='appointment_create'),

    path('medical_record/', MedicalRecordListAPIView.as_view(), name='medical_record_list'),
    path('medical_record/<int:pk>/', MedicalRecordDetailAPIView.as_view(), name='medical_record_detail'),
    path('medical_record/create/', MedicalRecordCreateAPIView.as_view(), name='medical_record_create'),

    path('feedback/', FeedbackListAPIView.as_view(), name='feedback_list'),
    path('feedback/<int:pk>/', FeedbackDetailAPIView.as_view(), name='feedback_detail'),
    path('feedback/create/', FeedbackCreateAPIView.as_view(), name='feedback_create'),
]
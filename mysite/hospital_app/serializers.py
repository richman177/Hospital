from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class DepartmentSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['department_name']


class SpecialtySimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = ['specialty_name']


class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = '__all__'


class DoctorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class DoctorSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['first_name']


class DoctorListSerializer(serializers.ModelSerializer):
    specialty = SpecialtySimpleSerializer(read_only=True, many=True)

    class Meta:
        model = Doctor
        fields = ['id', 'first_name', 'specialty', 'work_day']


class DoctorDetailSerializer(serializers.ModelSerializer):
    specialty = SpecialtySimpleSerializer(read_only=True, many=True)
    department = DepartmentSimpleSerializer()

    class Meta:
        model = Doctor
        fields = ['first_name', 'specialty', 'department', 'shift_start', 'shift_end', 'work_day', 'service_price']


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class AppointmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'


class AppointmentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'


class AppointmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'


class MedicalRecordListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = ['id', 'patient', 'doctor', 'diagnosis', 'treatment', 'prescribed_medication', 'created_at']


class MedicalRecordDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = '__all__'


class MedicalRecordCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = '__all__'


class FeedbackListSerializer(serializers.ModelSerializer):
    created_ad = serializers.DateTimeField(format('%d-%m-%Y  %T'))
    class Meta:
        model = Feedback
        fields = ['id', 'doctor', 'patient', 'rating', 'comment', 'created_ad']


class FeedbackDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'doctor', 'patient', 'rating', 'comment', 'created_ad']


class FeedbackCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'


class WardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = '__all__'
from django_filters import FilterSet
from .models import Department, Specialty, Doctor


class DepartmentFilter(FilterSet):
    class Meta:
        model = Department
        fields = {
            'department_name': ['exact'],
        }


class SpecialtyFilter(FilterSet):
    class Meta:
        model = Specialty
        fields = {
            'specialty_name': ['exact'],
        }


class DoctorFilter(FilterSet):
    class Meta:
        model = Doctor
        fields = {
            'service_price': ['gt', 'lt'],
            'work_day': ['exact']
        }
from django.contrib.auth import get_user_model
from rest_framework import serializers
from crud.users.models import Technology, TechnologyExperience, Applicant

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            ]
        
        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        }

class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = [
            "id",
            "first_name", 
            "last_name",
            "actual_address",
            "ci_field",
            "age"
            ]
        
        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "ci_field"}
        }

class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = [
            "id",
            "tech_name"
        ]

class TechnologyExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnologyExperience
        fields = [
            "applicant",
            "technology",
            "experience"
        ]
    
    def validate(self, data):
        ret = super().validate(data)
        technology = int (self.context['view'].request.data['technology'])
        applicant = int (self.context['view'].request.data['applicant'])
        if TechnologyExperience.objects.filter(applicant = applicant, technology = technology ):
            raise serializers.ValidationError('Reinserting of user experience in tech is not allowed')
        
        return ret
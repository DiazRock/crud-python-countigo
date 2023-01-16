from django.contrib.auth import get_user_model
from rest_framework import serializers
from crud.users.models import Technology, TechnologyExperience

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "first_name", 
            "last_name",
            "actual_address",
            "ci_field",
            "age"
            ]
        
        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        }

class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = [
            "name"
        ]

class TechnologyExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnologyExperience
        fields = [
            "user",
            "technology",
            "experience"
        ]
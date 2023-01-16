from django.http.response import Http404
from django.contrib.auth import get_user_model
from rest_framework import status, Response
from rest_framework.decorators import action
from rest_framework.mixins import (
    ListModelMixin, 
    RetrieveModelMixin, 
    UpdateModelMixin,
    CreateModelMixin)
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from crud.users.models import Technology, TechnologyExperience
from .serializers import UserSerializer, TechnologySerializer, TechnologyExperienceSerializer

User = get_user_model()


class UserViewSet(
        RetrieveModelMixin, 
        ListModelMixin, 
        UpdateModelMixin,
        CreateModelMixin, 
        GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "first_name"
    allowed_methods= ['POST', 'GET']

    def get_queryset(self, *args, **kwargs):
        #import ipdb; ipdb.set_trace()
        #assert isinstance(self.request.user.id, int)
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False)
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    
    

class TechnologyViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    GenericViewSet,
    CreateModelMixin):
    allowed_methods= ['POST', 'GET']
    serializer_class = TechnologySerializer
    queryset = Technology.objects.all()

class TechnologyExperienceViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    GenericViewSet,
    CreateModelMixin):
    allowed_methods= ['POST', 'GET']
    serializer_class = TechnologyExperienceSerializer
    queryset = TechnologyExperience.objects.all()
    

    @action(methods=['get'], detail=True,
            url_path='get-techs-experience-by-user')
    def get_techs_experience_by_user(self, request, user_id):
        """ Get the experience of the user in all techs"""
        technologies = TechnologyExperience.
                    objects.
                    filter(user = user_id).
                    values('technology', 'experience')
        
        
        return Response(
            [
                {
                "tech_name": Technology.objects.get(pk=t['technology']).name, 
                "experience": t['experience'] 
                } for t in technologies
            ]
            )

    @action(methods=['get'], detail=True,
            url_path='get-user-experience-by-tech')
    def get_user_experience_by_tech(self, request, tech_id):
        """ Get the experience of the user in all techs"""
        users_and_exp = TechnologyExperience.
                    objects.
                    filter(technology = tech_id).
                    values('user', 'experience')
        
        
        return Response(
            [
                {
                "user_name": User.objects.get(pk=t['user']).name, 
                "experience": t['experience'] 
                } for t in users_and_exp
            ]
            )
    
  

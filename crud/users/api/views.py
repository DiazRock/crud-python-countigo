from django.contrib.auth import get_user_model
from rest_framework import status
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

class TechnologyExperience(
    RetrieveModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    GenericViewSet,
    CreateModelMixin):
    allowed_methods= ['POST', 'GET']
    serializer_class = TechnologyExperience
    queryset = TechnologyExperience.objects.all()
    
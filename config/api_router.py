from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from crud.users.api.views import UserViewSet, TechnologyViewSet, TechnologyExperienceViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("technology", TechnologyViewSet)
router.register("technology-experience", TechnologyExperienceViewSet)

app_name = "api"
urlpatterns = router.urls

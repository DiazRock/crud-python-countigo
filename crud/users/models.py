from django.contrib.auth.models import AbstractUser
from django.db.models import (
    CharField,
    TextField,
    PositiveBigIntegerField,
    Model,
    ForeignKey,
    CASCADE
)
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.core.validators import MinLengthValidator


class User(AbstractUser):
    """
    Default custom user model for crud.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    #: First and last name do not cover name patterns around the globe
    first_name = CharField(
                        help_text ="Name of User", 
                        blank=False, 
                        max_length=255,
                        null=False,
                        default='John')

    last_name = CharField(
                        help_text ="Last Name of User",
                        blank=False,
                        max_length=255,
                        null=False,
                        default='Doe')

    actual_address = TextField(
                        help_text ="Address of User",
                        blank=True,
    )

    ci_regex = RegexValidator (
        regex = r'^[0][1-9]\d{9}$|^[1-9]\d{9}$',
        message = "CI must be conformed by eleven digits from 1 to 9"
    )
    ci_field = CharField(
        validators =[ci_regex, MinLengthValidator(11)], 
        max_length = 11, 
        blank = False,
        null = False,
        default='11111111111' )

    age = PositiveBigIntegerField (
        help_text = "Age of User",
        blank = False,
        null = False,
        default = 1
    )

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs = {"username": self.username})

class Technology(Model):
    name = CharField(
        max_length = 255,
        help_text = "Name of the technology"
        )

class TechnologyExperience(Model):
    user = ForeignKey(User, ondelete=CASCADE)
    technology = ForeignKey(Technology, ondelete=CASCADE)
    experience = IntegerField( 
        blank = False,
        null = False,
        default = 0)

from captcha.fields import ReCaptchaField
from django_registration.forms import RegistrationForm

from .models import User


class CustomUserCreationForm(RegistrationForm):
    """ Форма для регистрации пользователя """

    captcha = ReCaptchaField(label="I'm not a robot")

    class Meta(RegistrationForm.Meta):
        model = User
        fields = ('email', 'full_name')

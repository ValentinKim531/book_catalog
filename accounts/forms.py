from django import forms
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
    email = forms.CharField(required=True, label="Логин")
    password = forms.CharField(
        required=True, label="Пароль", widget=forms.PasswordInput
    )


class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(
        label="Пароль", strip=False, required=True, widget=forms.PasswordInput
    )
    password_confirm = forms.CharField(
        label="Подтвердите пароль",
        strip=False,
        required=True,
        widget=forms.PasswordInput,
    )
    email = forms.EmailField(required=True)

    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "password",
            "password_confirm",
            "first_name",
            "second_name",
        )
        labels = {
            "email": "Email",
            "password": "пароль",
            "password_confirm": "подтверждение пароля",
            "first_name": "Имя",
            "second_name": "Фамилия",
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Пароли не совпадают!")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get("password"))
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ("first_name", "second_name", "email")
        labels = {
            "first_name": "Имя",
            "second_name": "Фамилия",
            "email": "Email",
        }


class PasswordChangeForm(forms.ModelForm):
    password = forms.CharField(
        label="Новый пароль", strip=False, widget=forms.PasswordInput
    )
    password_confirm = forms.CharField(
        label="Подтвердите пароль", widget=forms.PasswordInput, strip=False
    )
    old_password = forms.CharField(
        label="Старый пароль", strip=False, widget=forms.PasswordInput
    )

    def clean_password_confirm(self):
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Пароли не совпадают!")
        return password_confirm

    def clean_old_password(self):
        old_password = self.cleaned_data.get("old_password")
        if not self.instance.check_password(old_password):
            raise forms.ValidationError("Старый пароль неправильный!")
        return old_password

    def save(self, commit=True):
        user = self.instance
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ["password", "password_confirm", "old_password"]

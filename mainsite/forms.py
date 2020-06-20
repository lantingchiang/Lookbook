from django import forms
from mainsite.models import User
from mainsite.models import Profile, Store
from allauth.account.forms import SignupForm
from phonenumber_field.modelfields import PhoneNumberField


class UserSignupForm(SignupForm):
    GENDER_CHOICES = [("F", "Female"), ("M", "Male"), ("O", "Other")]

    AGE_CHOICES = [
        ("A", "18-"),
        ("B", "18-25"),
        ("C", "25-35"),
        ("D", "35-45"),
        ("E", "45+"),
    ]

    first_name = forms.CharField(max_length=30, label="First Name")
    last_name = forms.CharField(max_length=30, label="Last Name")
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=False, label="Gender")
    age = forms.ChoiceField(choices=AGE_CHOICES, required=False, label="Age")
    phonenumber = PhoneNumberField()

    def signup(self, request, user):
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.save()

        new_profile = Profile(
            user=user,
            # TODO - add followed_tags = DEFAULT_FOLLOWED_TAGS
            phone_number=self.cleaned_data["phonenumber"],
            gender=self.cleaned_data["gender"],
            age=self.cleaned_data["age"],
        )

        new_profile.save()


class SellerSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label="First Name")
    last_name = forms.CharField(max_length=30, label="Last Name")
    store_name = forms.CharField(max_length=200, label="Store Name")
    location = forms.CharField(widget=forms.Textarea)
    phonenumber = PhoneNumberField()
    description = forms.CharField(widget=forms.Textarea)

    def signup(self, request, user):
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.is_seller = True
        user.save()

        new_store = Store(
            user=user,
            store_name=self.cleaned_data["store_name"],
            location=self.cleaned_data["location"],
            phonenumber=self.cleaned_data["phonenumber"],
            description=self.cleaned_data["description"],
        )

        new_store.save()

from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, TemplateView
from django.views import View
from allauth.account.views import SignupView

from mainsite.forms import UserSignupForm, SellerSignupForm


class HomeView(TemplateView):
    template_name = "home.html"


class FeedView(View):
    # https://docs.djangoproject.com/en/3.0/ref/contrib/syndication/

    def get(self, request):
        return HttpResponse(
            "This page should dynamically render looks \
                             based on followed tags, gender and location "
        )


class ProfileView(ListView):
    """
    Sends db entry to front end. Only get requests allowed
    """

    # model =
    # template_name =
    pass


class HashtagView(View):
    def get(self, request):
        """
        Front end will likely need to pass the hashtag name in some request field or in url.
        https://docs.djangoproject.com/en/3.0/topics/class-based-views/generic-display/#dynamic-filtering
        """
        return HttpResponse("Renders all looks labeled by this hashtag in chronological order")


class ProductView(View):
    """
    Renders information about product. Will likely link to SHOPPING CART.
    """

    def get(self, request):
        return HttpResponse("Product page")


class CustomSignupView(TemplateView):
    template_name = "accounts/signup.html"


class UserSignupView(SignupView):
    template_name = "accounts/user_signup.html"
    form_class = UserSignupForm


class SellerSignupView(SignupView):
    template_name = "accounts/seller_signup.html"
    form_class = SellerSignupForm

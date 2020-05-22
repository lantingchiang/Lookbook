from django.http import HttpResponse
from django.views.generic import ListView
from django.views import View


class HomeView(View):
    def get(self, request):
        return HttpResponse("This will be the home page")


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

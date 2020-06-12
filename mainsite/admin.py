from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from mainsite.models import (
    #User,
    Store,
    Hashtag,
    Look,
    Product,
    Profile,
)

# make these models edittable in admin site
#admin.site.register(User, UserAdmin)
# each object needs to be registered in separate line (stackoverflow)
admin.site.register(Store)
admin.site.register(Profile)
admin.site.register(Hashtag)
admin.site.register(Look)
admin.site.register(Product)

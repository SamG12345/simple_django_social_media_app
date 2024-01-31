from django.urls import path
from . import views

# main index or home page
urlpatterns = [ path("", views.index, name="index"), ]

# signin page 
urlpatterns += [ path("signin", views.signin, name="signin"), ]

# registration
urlpatterns += [ path("register", views.register, name="register"), ]

# logout
urlpatterns += [ path("signout", views.signout, name="signout"), ]

# profile
urlpatterns += [ path("profile/<int:id>", views.profile_view, name="profile"), ]

# profile image update
urlpatterns += [ path("profile/profile_image_upload", views.upload_pp, name="profile_image_upload"), ]

# like lekh
urlpatterns += [ path("like/<int:lekh_id>", views.like_lekh, name="like_lekh"), ]

# lekh view
urlpatterns += [ path("leakh/<int:lekh_id>", views.lekh_view, name="lekh_view"), ]

# lekh delete
urlpatterns += [ path("leakh/delete/<int:lekh_id>", views.delete_lekh, name="delete_lekh"), ]

# profiles
urlpatterns += [ path("profiles", views.profile_list, name="profiles"), ]

# comp
urlpatterns += [ path("comp/<int:id>", views.compain, name="comp"), ]

# search
urlpatterns += [ path("search", views.search_profile, name="search"), ]
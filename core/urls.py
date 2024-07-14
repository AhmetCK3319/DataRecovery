from django.urls import path
from .views import (
    create_blogPost_view,
    single_post_view,
    post_detail,
    update_blogPost_view,
    about_view,
    search,
)


urlpatterns = [
    path("create_post/", create_blogPost_view, name="new_post"),
    path("create_post/<int:id>/", update_blogPost_view, name="update_post"),
    path("single_post/", single_post_view, name="single_post"),
    path("post_detail/<int:id>/", post_detail, name="post_detail"),
    path("about/", about_view, name="about"),
    path("search/", search, name="search"),
]

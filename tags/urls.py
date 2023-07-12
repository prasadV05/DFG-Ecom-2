from django.urls import path, include
from tags.views import CreateTagViews
urlpatterns = [
    path('create/', CreateTagViews.as_view(), name='create_tag'),

]

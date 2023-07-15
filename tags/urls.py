from django.urls import path, include
from tags.views import CreateTagViews, DetailTagView
urlpatterns = [
    path('create/', CreateTagViews.as_view(), name='create_tag'),
    path('detail/<str:slug>/',DetailTagView.as_view(), name='details_tag')

]

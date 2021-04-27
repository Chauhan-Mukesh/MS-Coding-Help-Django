from django.urls import path

from . import views

urlpatterns = [
    path('category/', views.CategoriesList.as_view(), name='categories'),
    path('latest-posts/', views.LatestPostsList.as_view(), name="latest-posts"),
    path('category/<slug:category_slug>/', views.SubCategoryDetail.as_view()),
]

from django.urls import path

from . import views

urlpatterns = [
    path('category/', views.CategoriesList.as_view(), name='categories'),
    path('latest-posts/', views.LatestPostsList.as_view(), name="latest-posts"),
    path('posts/search/', views.Search),
    path('category/<slug:category_slug>/', views.SubCategoryDetail.as_view()),
    path('sub-category/<slug:sub_category_slug>/', views.SubCategoryPostList.as_view()),
    path('post/<slug:sub_category_slug>/<slug:post_slug>/', views.PostDetail.as_view()),
    path('contact-us/', views.ContactUsData, name='contact-us'),
    path('comment/', views.CommentOnPost, name='comment'),
    path('get-comments/', views.GetCommentsList.as_view(), name='get-comments')
]

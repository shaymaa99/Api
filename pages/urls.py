from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('hoppies',views.HoppiesViewSet,basename='hoppies')
router.register('hoppies_pk<int:id>',views.HoppiesViewSet_pk,basename='hoppies_pk')
router.register('Book',views.BookViewSet,basename='Book')
router.register('Video',views.VideoViewSet,basename='Video')
urlpatterns=[
    #path('HoppiesGenerics',views.HoppiesGenerics.as_view(),name='HoppiesGenerics'),
    #path('HoppiesGenerics_pk<int:id>/',views.HoppiesGenerics_pk.as_view(),name='HoppiesGenerics_pk')
]
urlpatterns+=router.urls

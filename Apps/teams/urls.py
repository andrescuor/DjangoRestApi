from django.urls import path, include
from Apps.teams import views


urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),

    # CRUD ENDPOINTS
    path('create/', views.TeamCreateView.as_view()),
    path('list/', views.TeamListApiView.as_view()),
    path('update/<pk>', views.TeamUpdateView.as_view()),
    path('delete/<pk>', views.TeamDeleteView.as_view()),
    path('review/<pk>', views.TeamRetrieveView.as_view()),

    # OTHER ENDPOINTS
    # Total de equipos registrados
    path('get-total/', views.TeamTotal.as_view()),


]
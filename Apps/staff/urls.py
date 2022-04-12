from django.urls import path, include
from Apps.staff import views


urlpatterns = [
    # CRUD ENDPOINTS
    path('create/', views.StaffCreateView.as_view()),
    path('list/', views.StaffListApiView.as_view()),

    path('review/<pk>', views.StaffRetrieveView.as_view()),
    path('update/<pk>', views.StaffUpdateView.as_view()),
    path('delete/<pk>', views.StaffDeleteView.as_view()),
    #path('staff/review/<pk>', views.StaffReviewView.as_view()),

    # OTHER ENDPOINTS
    # Tecnico mas viejo
    path('get-oldest/', views.StaffOldestManager.as_view()),
]
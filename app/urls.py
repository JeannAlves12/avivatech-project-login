from django.contrib import admin
from django.urls import path
from django.conf import settings # aula 040
from django.conf.urls.static import static
from account.views import register_view, login_view, logout_view
from tela.views import MeetingView, MeetingDetailView, NewMeetingCreateView, MeetingDeleteView, MeetingUpdateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('tela/', MeetingView.as_view(), name='tela'),
    path('meeting/<int:pk>/', MeetingDetailView.as_view(), name='meeting_detail'),
    path('new_meeting/', NewMeetingCreateView.as_view(), name='new_meeting'),
    path('meeting/<int:pk>/update/', MeetingUpdateView.as_view(), name='meeting_update'),
    path('meeting/<int:pk>/delete/', MeetingDeleteView.as_view(), name='meeting_delete'),
]

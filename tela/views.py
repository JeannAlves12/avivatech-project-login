from tela.models import Meeting
from tela.forms import MeetingForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


class MeetingView(ListView):
    model = Meeting
    template_name = 'meeting.html'
    context_object_name = 'tela'


class MeetingDetailView(DetailView):
    model = Meeting
    template_name = 'meeting_detail.html'


@method_decorator(login_required(login_url='login'), name='dispatch')
class NewMeetingCreateView(CreateView):
    model = Meeting
    form_class = MeetingForm
    template_name = 'new_meeting.html'
    success_url = '/tela/'

@method_decorator(login_required(login_url='login'), name='dispatch')
class MeetingUpdateView(UpdateView):
    model = Meeting
    form_class = MeetingForm
    template_name = 'meeting_update.html'

    def get_success_url(self):
        return reverse_lazy('meeting_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required(login_url='login'), name='dispatch')
class MeetingDeleteView(DeleteView):
    model = Meeting
    template_name = 'meeting_delete.html'
    success_url = '/tela/'
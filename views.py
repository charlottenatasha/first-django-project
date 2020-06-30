

# Create your views here.

from .models import Question
from django.views import generic
from django.utils import timezone



class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""

        return Question.objects.filter(pub_date__lte=timezone.now()).order_by ('-pub_date')[:5]

class DetailView(generic.DetailView):
    model= Question
    template_name = 'polls/detail.html'
    ...
    def get_queryset(self):

        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    model = Question
template_name ='polls/result.html'

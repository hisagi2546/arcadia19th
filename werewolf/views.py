from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Choice, Question, Village, Remark
from .forms import RemarkForm

class IndexView(generic.ListView):
    template_name = 'werewolf/index.html'
    context_object_name = 'latest_village_list'

    def get_queryset(self):
        return Village.objects.order_by('created_date')

def village(request, village_id):
    remark = get_object_or_404(Remark, pk=village_id)
    if request.method == "POST":
        form = RemarkForm(request.POST)
        if form.is_valid():
            remark = form.save(commit=False)
            remark.village_id = village_id
            remark.serial_no = 0
            remark.save()
            return HttpResponseRedirect(reverse('werewolf:village', args=(village_id,)))
    else:
        form = RemarkForm()
    latest_remark_list = Remark.objects.all()
    return render(request, 'werewolf/village.html', {'latest_remark_list':latest_remark_list, 'form':form})

class DetailView(generic.DetailView):
    model = Question
    template_name = 'werewolf/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'werewolf/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'werewolf/detail.html', {
            'question': question,
            'error_message': "投票先を選択してください",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('werewolf:results', args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'werewolf/results.html', {'question': question})

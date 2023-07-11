from django.forms import formset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from MainApp.models import Debate
from .forms import ChoiceFormSet, PollForm, ChoiceForm
from .models import Poll, Choice, Vote
# Create your views here.
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required

class poll_list(ListView):
    model = Poll
    template_name = 'poll_list.html'
    #return render(request, 'poll/poll_list.html')

def poll_detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'poll/poll_detail.html', {'poll':poll})

def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'poll/results.html', {'poll': poll})


def CreatePollView(request):
    ChoiceFormSet = formset_factory(ChoiceForm, extra=1)

    if request.method == 'POST':
        poll_form = PollForm(request.POST)
        choice_formset = ChoiceFormSet(request.POST, prefix='choices')

        if poll_form.is_valid() and choice_formset.is_valid():
            poll = poll_form.save(commit=False)
            poll.save()

            for choice_form in choice_formset:
                choice = choice_form.save(commit=False)
                choice.poll = poll
                choice.save()

            return redirect('poll_list')  # Redirect to the desired page after successful submission
    else:
        poll_form = PollForm()
        choice_formset = ChoiceFormSet(prefix='choices')

    return render(request, 'poll/create_poll.html', {
        'poll_form': poll_form,
        'choice_formset': choice_formset,
    })

@login_required
def vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    user = request.user
    if Vote.objects.filter(user=user, choice__poll=poll).exists():
        return render(request, 'poll/poll_detail.html', {'poll': poll, 'error_message': "You have already voted."})

    try:
        selected_choice_id = request.POST.get('choice')
        if selected_choice_id is None:
            raise KeyError
        selected_choice = poll.choice_set.get(pk=selected_choice_id)
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'poll/poll_detail.html', {'poll': poll, 'error_message': "Invalid choice"})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        Vote.objects.create(user=user, choice=selected_choice)
        return HttpResponseRedirect(reverse('results', args=(poll.id,)))

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from MainApp.models import Debate
from .models import Poll, Choice, Vote
# Create your views here.
from django.urls import reverse_lazy, reverse


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


from django.contrib.auth.decorators import login_required


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

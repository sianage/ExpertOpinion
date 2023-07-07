from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from MainApp.models import Debate
from .models import Poll, Choice
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

def vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice_id = request.POST.get('choice')
        print("selected_choice_id: ----------------------->",selected_choice_id)
        if selected_choice_id is None:
            print("selected choice is None? ----------------------->", selected_choice_id)
            raise KeyError
        selected_choice = poll.choice_set.get(pk=selected_choice_id)
    except KeyError:
        print("-----------------------------------> except KeyError")
        # Message for no choice selected
        return render(request, 'poll/poll_detail.html', {'poll': poll, 'error_message': "No choice selected"})
    except Choice.DoesNotExist as e:
        print("-----------------------------------------> choice does not exist")
        print("Choice.DoesNotExist Exception:", e)
        # Handle the case when the choice does not exist
        return render(request, 'poll/poll_detail.html', {'poll': poll, 'error_message': "Invalid choice"})
    else:
        print("-------------------------------------------> VOTED!")
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results', args=(poll.id,)))

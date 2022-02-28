from django.shortcuts import render
from django.forms import ModelForm
from app_poll.models import Poll


class PollForm(ModelForm):
    class Meta:
        model = Poll
        fields = (
            'full_name',
            'national_id',
            'vekalat_id',
            'vekalat_id',
            'osviat_kanoon_vokala',
            'vaziat_isargari',
        )


def index(request):
    form = PollForm()
    if request.method == 'POST':
        form = PollForm(request.POST)
        if form.is_valid():
            form.save()
    ctx = {
        'form': form,
        'poll_list': Poll.objects.all()
    }
    return render(request, 'index.html', ctx)

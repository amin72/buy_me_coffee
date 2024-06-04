from django.shortcuts import render

from .models import Creator


def creators(request):
    creators = Creator.objects.all()

    return render(request, 'creator/creators.html', {
        'creators': creators
    })

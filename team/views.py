from team.models import Team
from django.shortcuts import render

# Create your views here.


def team(request):
    
    all_team=Team.objects.all() 
    context={
        'team':all_team
        }
    return render(request, 'team.html',context)
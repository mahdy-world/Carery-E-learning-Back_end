from team.models import Team
from django.shortcuts import render

# Create your views here.

# Team Page
def team(request):
    
    all_team=Team.objects.all() 
    context={
        'team':all_team
        }
    return render(request, 'team.html',context)

#About Page
def about(request):
    
    return render (request,'about.html')
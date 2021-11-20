from team.models import Team
from django.shortcuts import redirect, render, render_to_response

# Create your views here.

# Team Page
def team(request):
    
    try:  
        all_team=Team.objects.all() 
        context={
            'team':all_team
            }
        return render(request, 'team.html',context)
    except:
        return render(request,'notFound.html')
#About Page
def about(request):
    
    return render (request,'about.html')
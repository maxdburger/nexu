from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from .models import Subject

# Create your views here.

@login_required
def subjects_view(request):
    if request.method == 'POST':
        name = request.POST.get('subject_name').strip()
        if name:
            slug = slugify(name)

        # add to model
        Subject.objects.get_or_create(
            user=request.user,
            name=name,
            defaults={'slug':slug}
        )

        return redirect('subjects')        

    subjects = Subject.objects.filter(user=request.user)
    return render(request, 'subjects.html', {'subjects': subjects})

@login_required
def subject_overview_view(request, slug):

    subject = get_object_or_404(
        Subject,
        user=request.user,
        slug=slug
    )
    
    return render(request, 'subject-overview.html', {'subject': subject})
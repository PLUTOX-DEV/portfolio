from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from .models import Project
from .models import Skill
from .forms import ContactForm



def home(request):
    projects = Project.objects.all().order_by('-created_at')[:3]
    return render(request, 'core/index.html', {'projects': projects})

# views.py

def about_view(request):
    frontend_skills = Skill.objects.filter(category='frontend')
    backend_skills = Skill.objects.filter(category='backend')
    return render(request, 'core/about.html', {
        'frontend_skills': frontend_skills,
        'backend_skills': backend_skills
    })


# 🔹 Contact Form View


def contact(request):
    form = ContactForm()
    success = False

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['email']

            try:
                send_mail(
                    subject=subject,
                    message=message,
                    from_email=sender,
                    recipient_list=['okeniyihakeem18@gmail.com'],  # ✅ Replace with your email
                    fail_silently=False,
                )
                success = True
                form = ContactForm()  # Clear the form
                # messages.success(request, "Your message was sent successfully!")
            except BadHeaderError:
                messages.error(request, "Invalid header found. Message not sent.")

    return render(request, 'core/contact.html', {'form': form, 'success': success})


# 🔹 All Projects View
def projects(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'core/projects.html', {'projects': projects})


# 🔹 Project Detail View
def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'core/project_detail.html', {'project': project})

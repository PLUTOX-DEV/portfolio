from django.db import models
from django.utils.text import slugify
from multiselectfield import MultiSelectField

# Font Awesome icon choices
ICON_CHOICES = [
    ("fa-brands fa-python", "Python"),
    ("fa-brands fa-html5", "HTML"),
    ("fa-brands fa-css3-alt", "CSS"),
    ("fa-brands fa-js", "JavaScript"),
    ("fa-solid fa-wind", "Tailwind CSS"),
    ("fa-solid fa-leaf", "Django"),
    ("fa-solid fa-database", "MySQL"),
    ("fa-brands fa-react", "React"),
    ("fa-solid fa-code", "Other"),
]

# Category options
CATEGORY_CHOICES = [
    ('frontend', 'Frontend'),
    ('backend', 'Backend'),
    ('database', 'Database'),
    ('devtools', 'Dev Tools'),
]
FRONTEND = 'frontend'
BACKEND = 'backend'
SKILL_CATEGORY_CHOICES = [
    
    
        (FRONTEND, 'Frontend'),
        (BACKEND, 'Backend'),
    ]

COLOR_CHOICES = [
    ('green', 'Green'),
    ('blue', 'Blue'),
    ('red', 'Red'),
]

# Shadow options
SHADOW_CHOICES = [
    ('green', 'hover:shadow-[0_0_20px_#00FF00]'),
    ('blue', 'hover:shadow-[0_0_20px_#3b82f6]'),
    ('red', 'hover:shadow-[0_0_20px_#ef4444]'),
]

# Technologies for multiselect
TECH_CHOICES = [
    ('HTML', 'HTML'),
    ('CSS', 'CSS'),
    ('JS', 'JavaScript'),
    ('Python', 'Python'),
    ('Django', 'Django'),
    ('React', 'React'),
]


class Skill(models.Model):
   
    
    name = models.CharField(max_length=100)
    proficiency = models.PositiveIntegerField()
    category = models.CharField(max_length=10, choices=SKILL_CATEGORY_CHOICES)
    icon = models.CharField(max_length=50, choices=ICON_CHOICES, default="fa-solid fa-code")

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    tech_stack = MultiSelectField(choices=TECH_CHOICES, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    skills = models.ManyToManyField(Skill, blank=True)
    icon = models.CharField(max_length=50, choices=ICON_CHOICES, default="fa-solid fa-code")
    color = models.CharField(max_length=10, choices=COLOR_CHOICES)
    shadow = models.CharField(max_length=10, choices=SHADOW_CHOICES)
    image = models.ImageField(upload_to='projects/', null=True, blank=True)
    demo_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True,  null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Project.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_tag_color(self):
        return {
            'green': 'text-[#00FF00]',
            'blue': 'text-blue-500',
            'red': 'text-red-500',
        }.get(self.color, 'text-white')

    def get_border_color(self):
        return {
            'green': 'border-[#00FF00]/20',
            'blue': 'border-blue-500/20',
            'red': 'border-red-500/20',
        }.get(self.color, 'border-white/20')

    def get_shadow_class(self):
        return {
            'green': 'hover:shadow-[0_0_20px_#00FF00]',
            'blue': 'hover:shadow-[0_0_20px_#3b82f6]',
            'red': 'hover:shadow-[0_0_20px_#ef4444]',
        }.get(self.shadow, '')


class Feature(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='features')
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

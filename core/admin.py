from django.contrib import admin
from .models import Project,Skill , Feature


admin.site.register(Skill)

class FeatureInline(admin.TabularInline):
    model = Feature
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [FeatureInline]
    list_display = ('title', 'created_at')

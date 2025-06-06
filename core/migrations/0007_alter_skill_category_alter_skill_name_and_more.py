# Generated by Django 5.2 on 2025-05-06 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_skill_proficiency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='category',
            field=models.CharField(choices=[('frontend', 'Frontend'), ('backend', 'Backend')], max_length=10),
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='skill',
            name='proficiency',
            field=models.PositiveIntegerField(),
        ),
    ]

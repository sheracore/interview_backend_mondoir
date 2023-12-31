# Generated by Django 3.2.19 on 2023-07-02 11:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cvs', '0005_auto_20230702_1115'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50, verbose_name='Content')),
                ('proficiency', models.IntegerField(choices=[(1, 'Familiar'), (2, 'Beginner'), (3, 'Intermediate'), (4, 'Advanced')], default=3, verbose_name='Proficiency')),
                ('cv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skill_cv', to='cvs.cv', verbose_name='CV')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Skill model',
                'verbose_name_plural': 'Skills',
            },
        ),
    ]

# Generated by Django 3.2.19 on 2023-07-02 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cvs', '0008_auto_20230702_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='company_name',
            field=models.CharField(max_length=50, verbose_name='Company Name'),
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('institution_name', models.CharField(max_length=50, verbose_name='Institution Name')),
                ('degree', models.IntegerField(choices=[(1, 'Master'), (2, 'Bachelor'), (3, 'Doctorate'), (4, 'Associate'), (5, 'Diploma'), (6, 'Certificate'), (7, 'Other')], default=2, verbose_name='Degree')),
                ('graduated_year', models.DateField(blank=True, null=True, verbose_name='Graduated Year')),
                ('cv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='education_cv', to='cvs.cv', verbose_name='CV')),
            ],
            options={
                'verbose_name': 'Education model',
                'verbose_name_plural': 'Educations',
            },
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('issuer', models.CharField(max_length=100, verbose_name='Issuer')),
                ('issuer_year', models.DateField(blank=True, null=True, verbose_name='Issuer Year')),
                ('cv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certificate_cv', to='cvs.cv', verbose_name='CV')),
            ],
            options={
                'verbose_name': 'Certificate model',
                'verbose_name_plural': 'Certificates',
            },
        ),
    ]
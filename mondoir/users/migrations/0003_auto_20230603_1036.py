# Generated by Django 3.2.19 on 2023-06-03 10:36

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import mondoir.users.models.usersinformation


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userinformation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformation',
            name='user',
            field=models.OneToOneField(editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='username',
            field=models.CharField(default=mondoir.users.models.usersinformation.default_username, max_length=18, validators=[django.core.validators.RegexValidator(code='invalid_username', message='Username must be Alphanumeric', regex='^\\w*-*\\w*$')], verbose_name='Username'),
        ),
    ]

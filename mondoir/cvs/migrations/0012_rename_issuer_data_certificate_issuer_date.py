# Generated by Django 3.2.19 on 2023-07-02 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cvs', '0011_auto_20230702_2111'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certificate',
            old_name='issuer_data',
            new_name='issuer_date',
        ),
    ]

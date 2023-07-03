# Generated by Django 3.2.19 on 2023-07-03 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('links', '0003_auto_20230703_0444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='link', to='contenttypes.contenttype', verbose_name='Content Type'),
        ),
    ]

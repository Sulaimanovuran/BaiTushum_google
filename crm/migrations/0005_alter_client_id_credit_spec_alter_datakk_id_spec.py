# Generated by Django 4.1.1 on 2022-10-12 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crm', '0004_alter_files_property_alter_images_property'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='id_credit_spec',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Кредитный специалист'),
        ),
        migrations.AlterField(
            model_name='datakk',
            name='id_spec',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Кредитный спец'),
        ),
    ]

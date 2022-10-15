# Generated by Django 4.1.2 on 2022-10-15 18:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BankingSystem', '0007_alter_profile_account_type_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

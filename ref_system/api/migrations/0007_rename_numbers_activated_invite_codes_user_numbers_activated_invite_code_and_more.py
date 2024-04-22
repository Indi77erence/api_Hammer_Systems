# Generated by Django 5.0.4 on 2024-04-21 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_rename_activated_invite_codes_user_numbers_activated_invite_codes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='numbers_activated_invite_codes',
            new_name='numbers_activated_invite_code',
        ),
        migrations.AddField(
            model_name='user',
            name='activated_invite_codes',
            field=models.CharField(blank=True, default=None, max_length=6, null=True, unique=True),
        ),
    ]
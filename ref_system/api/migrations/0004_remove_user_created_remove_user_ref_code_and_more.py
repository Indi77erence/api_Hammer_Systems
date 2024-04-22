# Generated by Django 5.0.4 on 2024-04-21 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_user_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='created',
        ),
        migrations.RemoveField(
            model_name='user',
            name='ref_code',
        ),
        migrations.AddField(
            model_name='user',
            name='activated_invite_codes',
            field=models.ManyToManyField(blank=True, related_name='activated_by', to='api.user'),
        ),
        migrations.AddField(
            model_name='user',
            name='invite_code',
            field=models.CharField(blank=True, max_length=6, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]

# Generated by Django 5.0.dev20230123050841 on 2023-01-24 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0003_event_submission"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="hackathon_participant",
            field=models.BooleanField(default=True, null=True),
        ),
    ]
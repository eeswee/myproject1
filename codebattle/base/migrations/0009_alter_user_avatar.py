# Generated by Django 5.0.dev20230123050841 on 2023-01-30 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0008_alter_user_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]
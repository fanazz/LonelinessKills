# Generated by Django 5.0.3 on 2024-03-25 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_lonelyhumanprofile_role_volunteerprofile_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lonelyhumanprofile',
            name='role',
            field=models.CharField(choices=[('LONELYHUMAN', 'lonely human'), ('VOLUNTEER', 'Volunteer')], default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='volunteerprofile',
            name='role',
            field=models.CharField(choices=[('LONELYHUMAN', 'lonely human'), ('VOLUNTEER', 'Volunteer')], default=None, max_length=20),
        ),
    ]

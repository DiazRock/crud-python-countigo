# Generated by Django 4.0.8 on 2023-01-16 01:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_name_user_actual_address_user_age_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the technology', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TechnologyExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.PositiveBigIntegerField(default=0)),
                ('technology', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.technology')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
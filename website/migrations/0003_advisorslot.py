# Generated by Django 4.2.5 on 2024-03-14 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0002_auctionitem_floor_count_auctionitem_house_size_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvisorSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')], max_length=20)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('message', models.TextField(blank=True, null=True)),
                ('max_user', models.IntegerField()),
                ('meet_link', models.CharField(blank=True, max_length=300, null=True)),
                ('booked_user_list', models.ManyToManyField(related_name='booked_users', to=settings.AUTH_USER_MODEL)),
                ('pending_user_list', models.ManyToManyField(related_name='pending_users', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slot', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

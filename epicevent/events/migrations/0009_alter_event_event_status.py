# Generated by Django 4.0.6 on 2022-08-12 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_alter_event_event_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status_event', to='events.eventstatus'),
        ),
    ]
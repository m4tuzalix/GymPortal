# Generated by Django 3.1.1 on 2020-09-10 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activityform',
            name='Confirmed',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='activityform',
            name='Activity',
            field=models.CharField(choices=[('M', 'MIDDLE'), ('L', 'LOW'), ('H', 'HIGH')], max_length=1),
        ),
        migrations.AlterField(
            model_name='activityform',
            name='Age',
            field=models.CharField(choices=[('A', '21-40'), ('O', '30+'), ('MA', '40-60'), ('Y', '18-21'), ('T', '15-18')], max_length=2),
        ),
    ]
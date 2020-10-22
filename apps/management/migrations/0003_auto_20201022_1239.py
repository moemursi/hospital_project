# Generated by Django 3.1.2 on 2020-10-22 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_auto_20201020_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicaldiagnosis',
            name='complaints',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='medicaldiagnosis',
            name='symptoms',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('Widowed', 'Widowed'), ('Married', 'Married'), ('Divorced', 'Divorced'), ('Single', 'Single')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='status',
            field=models.CharField(blank=True, choices=[('Completed', 'Completed'), ('Canceled', 'Canceled'), ('Pending', 'Pending')], max_length=100, null=True),
        ),
    ]
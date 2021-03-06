# Generated by Django 3.1.2 on 2020-10-22 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0001_initial'),
        ('management', '0003_auto_20201022_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='notes',
            field=models.ManyToManyField(blank=True, related_name='patient_notes', to='department.Note'),
        ),
        migrations.AlterField(
            model_name='bed',
            name='status',
            field=models.CharField(blank=True, choices=[('Assigned', 'Assigned'), ('Unassigned', 'Unassigned')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('Widowed', 'Widowed'), ('Married', 'Married'), ('Single', 'Single'), ('Divorced', 'Divorced')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_type',
            field=models.CharField(blank=True, choices=[('ER', 'Emergency'), ('Ward', 'Ward'), ('OPD', 'OPD')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='status',
            field=models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Canceled', 'Canceled'), ('Completed', 'Completed')], max_length=100, null=True),
        ),
    ]

# Generated by Django 2.2.2 on 2019-06-16 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Heart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveIntegerField()),
                ('sex', models.PositiveIntegerField(choices=[(1, 'male'), (0, 'female')], max_length=1)),
                ('chest_pain_type', models.PositiveIntegerField(choices=[(0, 'Type 0'), (1, 'Type 1'), (2, 'Type 2'), (3, 'Type 3')], max_length=1)),
                ('resting_blood_pressure_in_mm_HG', models.PositiveIntegerField()),
                ('serum_cholestrol_in_mg_dl', models.PositiveIntegerField()),
                ('is_fasting_blood_sugar_greater_than_120_mg_dl', models.PositiveIntegerField(choices=[(1, 'Greater than 120 mg/dl'), (0, 'Less than 120 mg/dl')], max_length=1)),
                ('resting_electrocardiograph', models.PositiveIntegerField(choices=[(0, 'Type 0'), (1, 'Type 1'), (2, 'Type 2')], max_length=1)),
                ('maximum_heart_rate_achieved', models.PositiveIntegerField()),
                ('exercise_induced', models.PositiveIntegerField(choices=[(1, 'YES'), (0, 'NO')], max_length=1)),
                ('ST_depression_induced_by_exrecise_relative_to_rest', models.FloatField()),
                ('slope_Type', models.PositiveIntegerField(choices=[(0, 'Type 0'), (1, 'Type 1'), (2, 'Type 2')], max_length=2)),
                ('number_of_major_vessels_colored_by_fluoroscopy', models.PositiveIntegerField()),
                ('thal', models.PositiveIntegerField(choices=[(3, 'Normal'), (6, 'Fixed Defect'), (7, 'Reversable Defect')], max_length=1)),
                ('target', models.PositiveIntegerField()),
            ],
        ),
    ]
# Generated by Django 4.1.1 on 2023-02-07 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0020_alter_predictiondata_bmi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictiondata',
            name='parentAgeDiabetes',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]

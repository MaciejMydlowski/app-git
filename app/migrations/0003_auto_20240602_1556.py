# Generated by Django 3.2.25 on 2024-06-02 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_posiadaneule_aktywny'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posiadaneule',
            name='aktywny',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='posiadaneule',
            name='ilosc_ramek',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1),
        ),
    ]
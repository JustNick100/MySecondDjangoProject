# Generated by Django 3.2.9 on 2022-03-20 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel_api', '0006_auto_20220320_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='level',
            field=models.CharField(help_text='level', max_length=20),
        ),
    ]

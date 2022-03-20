# Generated by Django 3.1.6 on 2021-10-19 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Intent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(blank=True, default='', max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatbot.category')),
                ('intent', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='chatbot.intent')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatbot.language')),
            ],
        ),
        migrations.CreateModel(
            name='ChatTracker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chatid', models.CharField(default='', max_length=255)),
                ('status', models.CharField(default='service', max_length=255)),
                ('language', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='chatbot.language')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='intent',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='chatbot.intent'),
        ),
        migrations.AddField(
            model_name='category',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatbot.language'),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(blank=True, max_length=1024)),
                ('intent', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='chatbot.intent')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatbot.question')),
            ],
        ),
    ]

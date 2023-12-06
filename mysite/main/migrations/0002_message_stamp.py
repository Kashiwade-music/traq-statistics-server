# Generated by Django 4.2.8 on 2023-12-05 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('userId', models.CharField(max_length=36)),
                ('channelId', models.CharField(max_length=36)),
                ('content', models.CharField(max_length=36)),
                ('createdAt', models.DateTimeField()),
                ('updatedAt', models.DateTimeField()),
                ('pinned', models.BooleanField()),
                ('threadId', models.CharField(max_length=36)),
            ],
        ),
        migrations.CreateModel(
            name='Stamp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=36)),
                ('stampId', models.CharField(max_length=36)),
                ('count', models.IntegerField()),
                ('createdAt', models.DateTimeField()),
                ('updatedAt', models.DateTimeField()),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stamps', to='main.message')),
            ],
        ),
    ]
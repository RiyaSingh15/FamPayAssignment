# Generated by Django 4.1 on 2022-08-28 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('published_at', models.DateTimeField()),
                ('thumbnails', models.JSONField()),
            ],
            options={
                'db_table': 'Videos',
            },
        ),
        migrations.AddIndex(
            model_name='videos',
            index=models.Index(fields=['title', 'description'], name='Videos_title_565e9e_idx'),
        ),
        migrations.AddIndex(
            model_name='videos',
            index=models.Index(fields=['published_at'], name='Videos_publish_625f18_idx'),
        ),
    ]
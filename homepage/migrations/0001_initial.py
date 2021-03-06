# Generated by Django 2.1.7 on 2019-04-23 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('book_logo', models.FileField(upload_to='')),
                ('book_title', models.CharField(max_length=200)),
                ('book_detail', models.CharField(max_length=1000)),
                ('book', models.FileField(blank=True, null=True, upload_to='static/homepage/')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_logo', models.FileField(upload_to='')),
                ('sub_title', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.Category')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.Subject'),
        ),
    ]

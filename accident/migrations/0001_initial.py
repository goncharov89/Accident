# Generated by Django 2.0.3 on 2018-05-21 12:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='accident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('tag', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('event', models.TextField()),
                ('accident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accident.accident')),
            ],
        ),
        migrations.CreateModel(
            name='status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='system',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('family_name', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='accident',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accident.users'),
        ),
        migrations.AddField(
            model_name='accident',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accident.status'),
        ),
        migrations.AddField(
            model_name='accident',
            name='system',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accident.system'),
        ),
    ]

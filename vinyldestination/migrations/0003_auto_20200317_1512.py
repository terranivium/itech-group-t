# Generated by Django 2.1.5 on 2020-03-17 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vinyldestination', '0002_auto_20200316_1612'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('year', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('slug', models.SlugField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'albums',
            },
        ),
        migrations.AlterModelOptions(
            name='artist',
            options={'verbose_name_plural': 'artists'},
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vinyldestination.Artist'),
        ),
    ]

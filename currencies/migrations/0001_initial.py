# Generated by Django 2.0.8 on 2018-11-28 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flag', models.ImageField(upload_to='flags')),
                ('symbol', models.CharField(max_length=3)),
                ('rate', models.DecimalField(decimal_places=4, default=1, max_digits=6)),
                ('name', models.CharField(max_length=3)),
            ],
        ),
    ]
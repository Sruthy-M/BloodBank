# Generated by Django 3.2.7 on 2021-10-02 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='donors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=3)),
                ('phone', models.CharField(max_length=10)),
                ('blood', models.CharField(max_length=5)),
            ],
        ),
    ]

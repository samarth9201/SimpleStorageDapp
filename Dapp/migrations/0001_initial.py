# Generated by Django 3.0.6 on 2020-05-23 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(editable=False, max_length=50)),
                ('abi', models.TextField(editable=False, null=True)),
                ('bytecode', models.TextField(editable=False, null=True)),
                ('address', models.TextField(editable=False, null=True)),
            ],
        ),
    ]

# Generated by Django 4.1 on 2023-04-04 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_alter_project_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_number',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
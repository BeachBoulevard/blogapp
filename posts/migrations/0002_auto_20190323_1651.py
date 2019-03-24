# Generated by Django 2.1 on 2019-03-23 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='body',
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='no title yet!', max_length=200),
        ),
    ]
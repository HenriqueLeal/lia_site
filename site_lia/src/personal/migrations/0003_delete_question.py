# Generated by Django 4.2.6 on 2023-10-27 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_alter_question_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Question',
        ),
    ]
# Generated by Django 2.0.7 on 2018-09-04 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0003_auto_20180825_0629'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
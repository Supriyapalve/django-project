# Generated by Django 4.0.5 on 2022-07-13 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipo', '0002_alter_ipo_models_contact_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='ipo_models',
            name='ipoamount',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

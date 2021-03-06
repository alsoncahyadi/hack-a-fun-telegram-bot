# Generated by Django 2.1.4 on 2019-02-12 13:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apple', '0010_auto_20190212_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='player',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='apple.Player', verbose_name='Player'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='staff',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Staff'),
        ),
    ]

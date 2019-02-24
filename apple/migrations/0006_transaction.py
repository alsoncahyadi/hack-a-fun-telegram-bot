# Generated by Django 2.1.4 on 2019-02-11 19:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apple', '0005_auto_20190212_0144'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Player ID')),
                ('point', models.IntegerField(verbose_name='Point')),
                ('game_type', models.SmallIntegerField(verbose_name='game_type')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='apple.Player', verbose_name='Player')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Staff')),
            ],
            options={
                'verbose_name': 'Transaction',
                'verbose_name_plural': 'Transactions',
            },
        ),
    ]

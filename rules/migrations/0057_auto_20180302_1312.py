# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-02 13:12


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rules', '0056_auto_20180223_0823'),
    ]

    operations = [
        migrations.CreateModel(
            name='RulesetTransformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(choices=[(b'action', b'Action'), (b'lateral', b'Lateral'), (b'none', b'None'), (b'suppressed', b'Suppressed'), (b'target', b'Target')], default=b'action', max_length=15)),
                ('value', models.CharField(default=b'none', max_length=15)),
                ('ruleset_transformation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rules.Ruleset')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='rulesettransformation',
            unique_together=set([('ruleset_transformation', 'key')]),
        ),
    ]

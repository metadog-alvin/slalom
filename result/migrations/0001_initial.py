# Generated by Django 4.0.4 on 2022-04-20 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enroll_id', models.IntegerField(null=True)),
                ('round_one_second', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('round_one_miss_conr', models.IntegerField(null=True)),
                ('round_one_result', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('round_two_second', models.IntegerField(null=True)),
                ('round_two_miss_conr', models.CharField(max_length=2, null=True)),
                ('round_two_result', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('skill_1', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('art_1', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('score_1', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('skill_2', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('art_2', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('score_2', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('skill_3', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('art_3', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('score_3', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('skill_4', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('art_4', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('score_4', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('skill_5', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('art_5', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('score_5', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('punish', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('final_result', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('rank', models.IntegerField(null=True)),
                ('integral', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'result',
            },
        ),
    ]

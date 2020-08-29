# Generated by Django 3.0.7 on 2020-06-26 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userchat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fonction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intitule', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='personne',
            name='amis',
            field=models.ManyToManyField(null=True, related_name='_personne_amis_+', to='userchat.Personne'),
        ),
        migrations.AddField(
            model_name='personne',
            name='gendar',
            field=models.CharField(default='None', max_length=3),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenu', models.TextField()),
                ('date_de_publication', models.DateField()),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userchat.Personne')),
            ],
        ),
    ]

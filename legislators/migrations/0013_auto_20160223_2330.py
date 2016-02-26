# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-23 23:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legislators', '0012_auto_20160223_2259'),
    ]

    operations = [
        migrations.CreateModel(
            name='StateCongressPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.CharField(max_length=255)),
                ('facebook_id', models.CharField(blank=True, max_length=255)),
                ('fax', models.CharField(blank=True, max_length=255, null=True)),
                ('first_name', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('in_office', models.BooleanField()),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True)),
                ('name_suffix', models.CharField(blank=True, max_length=255, null=True)),
                ('nickname', models.CharField(blank=True, max_length=255, null=True)),
                ('party', models.CharField(blank=True, choices=[('R', 'Republican'), ('D', 'Democrat'), ('I', 'Independent'), ('G', 'Green')], max_length=255)),
                ('phone', models.CharField(blank=True, max_length=255)),
                ('state', models.CharField(choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MH', 'Marshall Islands'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('FM', 'Micronesia'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('MP', 'Northern Marianas'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PW', 'Palau'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('VI', 'Virgin Islands'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], max_length=255)),
                ('state_name', models.CharField(blank=True, max_length=255, null=True)),
                ('term_end', models.DateField(blank=True, null=True)),
                ('term_start', models.DateField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('twitter_id', models.CharField(blank=True, max_length=255)),
                ('website', models.URLField(blank=True, max_length=255, null=True)),
                ('district', models.CharField(blank=True, max_length=255, null=True)),
                ('leg_id', models.CharField(max_length=255)),
                ('photo_url', models.URLField(blank=True, max_length=255, null=True)),
                ('office', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StateCongressPersonRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chamber', models.CharField(choices=[('H', 'House'), ('S', 'Senate'), ('O', 'Other'), ('U', 'Upper'), ('L', 'Lower')], max_length=255)),
                ('state', models.CharField(choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MH', 'Marshall Islands'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('FM', 'Micronesia'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('MP', 'Northern Marianas'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PW', 'Palau'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('VI', 'Virgin Islands'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], max_length=255)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='fedcongressperson',
            options={'verbose_name': 'Federal Congressperson', 'verbose_name_plural': 'Federal Congresspersons'},
        ),
        migrations.AlterField(
            model_name='fedcongressperson',
            name='chamber',
            field=models.CharField(choices=[('H', 'House'), ('S', 'Senate'), ('O', 'Other'), ('U', 'Upper'), ('L', 'Lower')], max_length=255),
        ),
        migrations.AlterField(
            model_name='fedcongressperson',
            name='facebook_id',
            field=models.CharField(blank=True, default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fedcongressperson',
            name='state_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

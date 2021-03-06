# Generated by Django 3.1.2 on 2020-12-16 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dataimport',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('day', models.CharField(blank=True, max_length=50)),
                ('year', models.IntegerField(blank=True)),
                ('month', models.CharField(blank=True, max_length=50)),
                ('date', models.IntegerField(blank=True)),
                ('ampm', models.CharField(blank=True, max_length=50)),
                ('country', models.CharField(blank=True, max_length=50)),
                ('province', models.CharField(blank=True, max_length=50)),
                ('county', models.CharField(blank=True, max_length=50)),
                ('district', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('suburbward', models.CharField(blank=True, max_length=50)),
                ('precise_location', models.CharField(blank=True, max_length=50)),
                ('latitude', models.FloatField()),
                ('longtitude', models.FloatField()),
                ('type', models.CharField(blank=True, max_length=50)),
                ('actor', models.CharField(blank=True, max_length=50)),
                ('subtype', models.CharField(blank=True, max_length=50)),
                ('tactic', models.CharField(blank=True, max_length=50)),
                ('severity', models.CharField(blank=True, max_length=50)),
                ('narrative', models.TextField()),
                ('ipt', models.CharField(blank=True, max_length=50)),
                ('amv', models.CharField(blank=True, max_length=50)),
                ('target', models.CharField(blank=True, max_length=50)),
                ('location_accuracy', models.CharField(blank=True, max_length=50)),
                ('primary_source', models.CharField(blank=True, max_length=50)),
                ('secondary_source', models.CharField(blank=True, max_length=50)),
                ('special_interest_group', models.CharField(blank=True, max_length=50)),
                ('male_cd', models.IntegerField(blank=True)),
                ('female_cd', models.IntegerField(blank=True)),
                ('child_cd', models.IntegerField(blank=True)),
                ('unknown_cd', models.IntegerField(blank=True)),
                ('foreign_national_cd', models.IntegerField(blank=True)),
                ('nationality_cd', models.IntegerField(blank=True)),
                ('male_ci', models.IntegerField(blank=True)),
                ('female_ci', models.IntegerField(blank=True)),
                ('child_ci', models.IntegerField(blank=True)),
                ('unknown_ci', models.IntegerField(blank=True)),
                ('foreign_national_ci', models.IntegerField(blank=True)),
                ('nationality_ci', models.IntegerField(blank=True)),
                ('un_od', models.IntegerField(blank=True)),
                ('diplomatic_od', models.IntegerField(blank=True)),
                ('politician_od', models.IntegerField(blank=True)),
                ('media_com_inj', models.IntegerField(blank=True)),
                ('gok_secfor_com_inj', models.IntegerField(blank=True)),
                ('gok_police_com_inj', models.IntegerField(blank=True)),
                ('gok_civ_com_inj', models.IntegerField(blank=True)),
                ('gsu_com_inj', models.IntegerField(blank=True)),
                ('ap_com_inj', models.IntegerField(blank=True)),
                ('kws_com_inj', models.IntegerField(blank=True)),
                ('kpr_com_inj', models.IntegerField(blank=True)),
                ('hasm_com_inj', models.IntegerField(blank=True)),
                ('myc_com_d', models.IntegerField(blank=True)),
                ('gok_secfor_com_d', models.IntegerField(blank=True)),
                ('gok_police_com_d', models.IntegerField(blank=True)),
                ('gok_civ_com_d', models.IntegerField(blank=True)),
                ('gsu_com_d', models.IntegerField(blank=True)),
                ('ap_com_d', models.IntegerField(blank=True)),
                ('kws_com_d', models.IntegerField(blank=True)),
                ('kpr_com_d', models.IntegerField(blank=True)),
                ('hasm_com_d', models.IntegerField(blank=True)),
                ('myc_abd', models.IntegerField(blank=True)),
                ('ngo_abd', models.IntegerField(blank=True)),
                ('nationality_abd', models.IntegerField(blank=True)),
                ('un_abd', models.IntegerField(blank=True)),
                ('civilian_abd', models.IntegerField(blank=True)),
                ('gok_sf_abd', models.IntegerField(blank=True)),
                ('gok_civ_abd', models.IntegerField(blank=True)),
                ('political_abd', models.IntegerField(blank=True)),
                ('status_abd', models.IntegerField(blank=True)),
                ('duration', models.IntegerField(blank=True)),
            ],
        ),
    ]

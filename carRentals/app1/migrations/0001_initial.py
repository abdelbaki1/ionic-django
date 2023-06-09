# Generated by Django 3.2.18 on 2023-04-02 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bank_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.FloatField()),
                ('bank_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.bankaccount')),
            ],
        ),
        migrations.CreateModel(
            name='RentalAgency',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RentalDuration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours', models.IntegerField()),
                ('days', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('license_plate', models.CharField(max_length=10)),
                ('brand', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TouristVehicle',
            fields=[
                ('vehicle_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app1.vehicle')),
            ],
            bases=('app1.vehicle',),
        ),
        migrations.CreateModel(
            name='UtilityVehicle',
            fields=[
                ('vehicle_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app1.vehicle')),
            ],
            bases=('app1.vehicle',),
        ),
        migrations.CreateModel(
            name='VehicleStatus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('mileage', models.FloatField()),
                ('fuel_level', models.FloatField()),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='TechnicalInspection',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.rentalagency')),
                ('driver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.driver')),
                ('duration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.rentalduration')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('description', models.TextField()),
                ('insurance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.insurance')),
                ('rental', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.rental')),
                ('technical_inspection', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.technicalinspection')),
            ],
        ),
        migrations.CreateModel(
            name='QuarterlyStatistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incidents', models.ManyToManyField(to='app1.Incident')),
                ('payments', models.ManyToManyField(to='app1.Payment')),
                ('rentals', models.ManyToManyField(to='app1.Rental')),
                ('vehicles', models.ManyToManyField(to='app1.Vehicle')),
            ],
        ),
        migrations.AddField(
            model_name='payment',
            name='rental',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.rental'),
        ),
        migrations.CreateModel(
            name='LocationAgency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('rental_agency', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app1.rentalagency')),
            ],
        ),
        migrations.AddField(
            model_name='insurance',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.vehicle'),
        ),
        migrations.CreateModel(
            name='LuxuryVehicle',
            fields=[
                ('vehicle_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app1.vehicle')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.driver')),
            ],
            bases=('app1.vehicle',),
        ),
    ]

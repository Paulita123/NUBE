# Generated by Django 3.2.9 on 2021-11-20 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_afiliacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Implicado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('acusacion', models.CharField(max_length=45)),
                ('culpable', models.BooleanField(default=False)),
                ('pena', models.CharField(max_length=45)),
                ('comentarios', models.CharField(max_length=45)),
                ('afiliado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='afiliados', to='app.afiliacion')),
                ('proceso', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='procesos', to='app.proceso')),
            ],
        ),
    ]

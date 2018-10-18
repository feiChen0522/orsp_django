# Generated by Django 2.1.1 on 2018-10-18 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20181013_1124'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.City')),
                ('provice', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.Province')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
    ]

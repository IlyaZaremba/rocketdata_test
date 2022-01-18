# Generated by Django 3.2.3 on 2022-01-18 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_auto_20220118_0625'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ['fio'], 'verbose_name': 'Сотрудник', 'verbose_name_plural': 'Сотрудники'},
        ),
        migrations.RemoveField(
            model_name='employee',
            name='employment_date',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='lft',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='paid_salary',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='rght',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='salary',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='tree_id',
        ),
        migrations.AddField(
            model_name='employee',
            name='chief',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='employees.employee', verbose_name='Начальник'),
        ),
        migrations.AddField(
            model_name='employee',
            name='date_of_employment',
            field=models.DateField(default='2022-01-01', verbose_name='Дата приема на работу'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='fio',
            field=models.CharField(default='01.01.2022', max_length=150, verbose_name='ФИО'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='salary_amount',
            field=models.DecimalField(decimal_places=2, default=2, max_digits=10, verbose_name='Размер заработной платы'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='salary_paid',
            field=models.DecimalField(decimal_places=2, default=12, max_digits=10, verbose_name='Выплаченная зарплата'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='level',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='5', max_length=1, verbose_name='Уровень иерархии'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(max_length=100, verbose_name='Должность'),
        ),
        migrations.CreateModel(
            name='EmployeeAPIKey',
            fields=[
                ('id', models.CharField(editable=False, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('prefix', models.CharField(editable=False, max_length=8, unique=True)),
                ('hashed_key', models.CharField(editable=False, max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('name', models.CharField(default=None, help_text='A free-form name for the API key. Need not be unique. 50 characters max.', max_length=50)),
                ('revoked', models.BooleanField(blank=True, default=False, help_text='If the API key is revoked, clients cannot use it anymore. (This cannot be undone.)')),
                ('expiry_date', models.DateTimeField(blank=True, help_text='Once API key expires, clients cannot use it anymore.', null=True, verbose_name='Expires')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='api_keys', to='employees.employee')),
            ],
            options={
                'verbose_name': 'API ключ сотрудника',
                'verbose_name_plural': 'API ключи сотрудников',
                'ordering': ('-created',),
                'abstract': False,
            },
        ),
    ]
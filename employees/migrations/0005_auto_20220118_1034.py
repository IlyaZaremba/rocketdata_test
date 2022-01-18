# Generated by Django 3.2.3 on 2022-01-18 07:34

from decimal import Decimal
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employees', '0004_auto_20220118_0754'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'Сотрудник', 'verbose_name_plural': 'Сотрудники'},
        ),
        migrations.RemoveField(
            model_name='employee',
            name='chief',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='date_of_employment',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='fio',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='salary_amount',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='salary_paid',
        ),
        migrations.AddField(
            model_name='employee',
            name='employment_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата приема на работу'),
        ),
        migrations.AddField(
            model_name='employee',
            name='lft',
            field=models.PositiveIntegerField(default='2', editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='name',
            field=models.CharField(default='fds', max_length=256, verbose_name='ФИО'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='owner',
            field=models.ManyToManyField(blank=True, related_name='owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='employee',
            name='paid_salary',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0'))], verbose_name='Выплаченная зарплата'),
        ),
        migrations.AddField(
            model_name='employee',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='employees.employee', verbose_name='Босс'),
        ),
        migrations.AddField(
            model_name='employee',
            name='rght',
            field=models.PositiveIntegerField(default=2, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='salary',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0'))], verbose_name='Заработная плата'),
        ),
        migrations.AddField(
            model_name='employee',
            name='tree_id',
            field=models.PositiveIntegerField(db_index=True, default=2, editable=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='level',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(choices=[('МАСТЕР', 'мастер'), ('ПРОРАБ', 'прораб'), ('НАЧАЛЬНИК УЧАСТКА', 'начальник участка'), ('ГЛАНЫЙ ИНЖЕНЕР', 'главный инженер'), ('ДИРЕКТОР', 'директор')], default='МАСТЕР', max_length=100, verbose_name='Должность'),
        ),
        migrations.DeleteModel(
            name='EmployeeAPIKey',
        ),
    ]

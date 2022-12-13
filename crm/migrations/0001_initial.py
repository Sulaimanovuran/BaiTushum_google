# Generated by Django 4.1.4 on 2022-12-13 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activites_add', models.CharField(max_length=100, verbose_name='Добавить источник дохода')),
            ],
            options={
                'verbose_name': 'Сфера деятельности',
                'verbose_name_plural': 'Сфера деятельности',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='ФИО клиента')),
                ('credit_type', models.CharField(choices=[('LS', 'Лизинг'), ('CR', 'Кредит')], max_length=30, verbose_name='Тип кредита')),
                ('status', models.CharField(choices=[('success', 'Выдан'), ('processing', 'Обработка'), ('discussion', 'На рассмотрении'), ('denied', 'Отказано'), ('payback', 'Погашен за счет отступных'), ('judicial', 'Судебный')], max_length=30, verbose_name='Статус клиента')),
                ('credit_sum', models.CharField(max_length=30, verbose_name='Сумма кредита')),
                ('repaid_by_redemption', models.FileField(null=True, upload_to='Отступные документы/%Y/%m/%d', verbose_name='Отступные документы')),
                ('court_documents', models.FileField(null=True, upload_to='Судебные документы/%Y/%m/%d', verbose_name='Судебные документы')),
                ('marital_status', models.CharField(choices=[('married', 'Женат/Замужем'), ('divorced', 'Разведен'), ('widow/widower', 'Вдова/Вдовец'), ('single', 'Холост/Незамужем')], max_length=30, verbose_name='Семейное положение')),
                ('credit_history', models.FileField(default='Кредитная история отсутствует', null=True, upload_to='client_credit_history/%Y/%m/%d', verbose_name='Кредитная история')),
                ('phone', models.CharField(default='+996', max_length=100, unique=True, verbose_name='Номер телефона')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес прописки')),
                ('client_actual_address', models.CharField(default='Тот же что и по прописке', max_length=100, verbose_name='Адрес фактический')),
                ('income_statement', models.FileField(null=True, upload_to='client_income_statement/%Y/%m/%d', verbose_name='Справка о доходах')),
                ('contracts', models.FileField(null=True, upload_to='contracts_with_suppliers/%Y/%m/%d', verbose_name='Договора с подрядчиками и поставщиками')),
                ('report', models.FileField(null=True, upload_to='reports_with_suppliers/%Y/%m/%d', verbose_name='Oтчет подрядчиков и поставщиков об оказанной услугe')),
                ('monitoring_report', models.FileField(null=True, upload_to='media', verbose_name='Oтчет по мониторингу')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'ЧП/ИП',
                'verbose_name_plural': 'ЧП/ИП',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100, unique=True, verbose_name='Наименование компании')),
                ('inn', models.CharField(max_length=14, unique=True, verbose_name='ИНН Компании')),
                ('legal_address', models.CharField(max_length=100, verbose_name='Юридический адрес')),
                ('actual_address', models.CharField(max_length=100, verbose_name='Фактический адрес')),
                ('telephone', models.CharField(max_length=30, verbose_name='Номер телефона')),
                ('okpo', models.CharField(max_length=8, unique=True, verbose_name='ОКПО')),
                ('register_number', models.CharField(max_length=30, unique=True, verbose_name='Номер регистрации')),
                ('document', models.FileField(null=True, upload_to='company_files/%Y/%m/%d', verbose_name='Документ компании')),
            ],
            options={
                'verbose_name': 'Компания',
                'verbose_name_plural': 'Компании',
            },
        ),
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_meeting', models.BooleanField(default=False, verbose_name='Личная встреча')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('date', models.CharField(max_length=30, verbose_name='Дата')),
                ('time', models.CharField(max_length=30, verbose_name='Время')),
                ('desc', models.TextField(max_length=200, verbose_name='Содержание')),
                ('results_report', models.FileField(null=True, upload_to='results_report/%Y/%m/%d', verbose_name='Очет по результатам')),
                ('statistics', models.FileField(null=True, upload_to='statistics/%Y/%m/%d', verbose_name='Статистика')),
            ],
            options={
                'verbose_name': 'Переговоры',
                'verbose_name_plural': 'Переговоры',
            },
        ),
        migrations.CreateModel(
            name='DataKK',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания:')),
                ('credit_spec_report', models.FileField(null=True, upload_to='credit_spec/%Y/%m/%d', verbose_name='Заключение кредитного эксперта (скан):')),
                ('committee_decision', models.FileField(null=True, upload_to='decision/%Y/%m/%d', verbose_name='Решение КК (скан):')),
                ('all_contracts', models.FileField(null=True, upload_to='all_contracts/%Y/%m/%d', verbose_name='Все заключенные договора, перечень и сканы:')),
                ('scoring', models.CharField(blank=True, max_length=150, null=True, verbose_name='Скоринг:')),
            ],
            options={
                'verbose_name': 'Документ на КК',
                'verbose_name_plural': 'Документы на КК',
            },
        ),
        migrations.CreateModel(
            name='Guarantor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='ФИО залогодателя')),
                ('status', models.CharField(choices=[('married', 'Женат/Замужем'), ('divorced', 'Разведен'), ('widow/widower', 'Вдова/Вдовец'), ('single', 'Холост/Незамужем')], max_length=30, verbose_name='Семейное положение')),
                ('credit_history', models.FileField(null=True, upload_to='credit_history/%Y/%m/%d', verbose_name='Кредитная история')),
                ('phone', models.CharField(max_length=30, verbose_name='Номер телефона')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес прописки')),
                ('actual_address', models.CharField(max_length=100, verbose_name='Адрес фактический')),
                ('income_statement', models.FileField(null=True, upload_to='guarantor_income_statement/%Y/%m/%d', verbose_name='Справка о доходах')),
            ],
            options={
                'verbose_name': 'Поручителя',
                'verbose_name_plural': 'Поручители',
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100, verbose_name='Залоговое имущество')),
                ('address', models.CharField(max_length=100, verbose_name='Местонахождение залога')),
            ],
            options={
                'verbose_name': 'Залоговое имущество',
                'verbose_name_plural': 'Залоговые имущества',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='company_images/%Y/%m/%', verbose_name='Фото')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='crm.property', verbose_name='Залоговое имущество')),
            ],
            options={
                'verbose_name_plural': 'Фотографии залогового имущества',
            },
        ),
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='company_files/%Y/%m/%d', verbose_name='Файл')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='crm.property', verbose_name='Залоговое имущество')),
            ],
            options={
                'verbose_name': 'Документ на залоговое имущество',
                'verbose_name_plural': 'Документы на залоговое имущество',
            },
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_company', models.CharField(auto_created=True, max_length=50, verbose_name='Компания клиента')),
                ('full_name_director', models.CharField(max_length=100, verbose_name='ФИО представителя')),
                ('inn', models.CharField(max_length=20, verbose_name='ИНН')),
                ('credit_type', models.CharField(choices=[('LS', 'Лизинг'), ('CR', 'Кредит')], max_length=30, verbose_name='Тип кредита')),
                ('repaid_by_redemption', models.FileField(null=True, upload_to='Отступные документы/%Y/%m/%d', verbose_name='Отступные документы юр.лица')),
                ('court_documents', models.FileField(null=True, upload_to='Судебные документы/%Y/%m/%d', verbose_name='Судебные документы юр.лица')),
                ('status', models.CharField(choices=[('success', 'Выдан'), ('processing', 'Обработка'), ('discussion', 'На рассмотрении'), ('denied', 'Отказано'), ('payback', 'Погашен за счет отступных'), ('judicial', 'Судебный')], max_length=30, verbose_name='Статус клиента')),
                ('credit_sum', models.CharField(max_length=30, verbose_name='Сумма кредита')),
                ('credit_history', models.FileField(default='Кредитная история отсутствует', null=True, upload_to='client_credit_history/%Y/%m/%d', verbose_name='Кредитная история')),
                ('phone', models.CharField(default='+996', max_length=100, unique=True, verbose_name='Телефон компании')),
                ('address', models.CharField(max_length=100, verbose_name='Юр. адрес')),
                ('client_actual_address', models.CharField(default='Тот же что и юр. адрес', max_length=100, verbose_name='Адрес фактический')),
                ('contracts', models.FileField(null=True, upload_to='contracts_with_suppliers/%Y/%m/%d', verbose_name='Договора с подрядчиками и поставщиками')),
                ('report', models.FileField(null=True, upload_to='reports_with_suppliers/%Y/%m/%d', verbose_name='Oтчет подрядчиков и поставщиков об оказанной услугe')),
                ('monitoring_report', models.FileField(null=True, upload_to='media', verbose_name='Oтчет по мониторингу')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('average_salary', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Средний доход в месяц')),
                ('own_contribution', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Размер собвственного вклада')),
                ('assets', models.TextField(help_text='Актив - стоимость – дата приобретения', verbose_name='Активы на момент анализа')),
                ('current_loan', models.CharField(max_length=200, verbose_name='Текущие кредиты')),
                ('id_company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.company', verbose_name='Компания')),
            ],
            options={
                'verbose_name': 'Юридическое лицо',
                'verbose_name_plural': 'Юридические лица',
            },
        ),
    ]

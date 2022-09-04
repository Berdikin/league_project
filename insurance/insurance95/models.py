from django.core.validators import MaxValueValidator
from django.db import models

# Create your models here.
from django.urls import reverse


# class admins(models.Model):
#  admin_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='admin_id')
#  surname = models.CharField(max_length=35, verbose_name='Фамилия')
#  name = models.CharField(max_length=35, verbose_name="Имя")
#  patronymic = models.CharField(max_length=35, blank=True, verbose_name='Отчество')
#  login = models.CharField(max_length=35, verbose_name='Логин')
#  password = models.CharField(max_length=35, verbose_name='Пароль')
#  email = models.EmailField(max_length=100)
#  mobile_number = models.IntegerField(verbose_name="Телефон")

#  def __str__(self):
#     surname = str(self.surname) + ' '
#    name = str(self.name) + ' '
#    patronymic = str(self.patronymic)
#    FIO = surname + name + patronymic
#    return FIO

# class Meta:
#    verbose_name = 'Администратор'
#    verbose_name_plural = 'Администраторы'
#   ordering = ['admin_id']


class agent(models.Model):
    agent_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='agent_id')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания агента')
    surname = models.CharField(max_length=35, verbose_name='Фамилия')
    name = models.CharField(max_length=35, verbose_name="Имя")
    patronymic = models.CharField(max_length=35, blank=True, verbose_name='Отчество')
    login = models.CharField(max_length=35, verbose_name='Логин')
    password = models.CharField(max_length=35, verbose_name='Пароль')
    email = models.EmailField(max_length=100)
    mobile_number = models.IntegerField(verbose_name="Телефон")
#    admin = models.ForeignKey('admins', on_delete=models.PROTECT)

    def __str__(self):
        surname = str(self.surname) + ' '
        name = str(self.name) + ' '
        patronymic = str(self.patronymic)
        FIO = surname + name + patronymic
        return FIO

    class Meta:
        verbose_name = 'Агент'
        verbose_name_plural = 'Агенты'
        ordering = ['surname', 'name', 'patronymic']


class clients(models.Model):
    physical_entity = 'Физ. лицо'
    legal_entity = 'Юр. лицо'
    entity_choices = [
        (physical_entity, 'Физическое лицо'),
        (legal_entity, 'Юридическое лицо')
    ]
    client_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='client_id')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото клиента")
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания клиента')
    surname = models.CharField(max_length=35, verbose_name='Фамилия')
    name = models.CharField(max_length=35, verbose_name='Имя')
    patronymic = models.CharField(max_length=35, blank=True, verbose_name='Отчество')
    entity = models.CharField(max_length=35, choices=entity_choices, default=physical_entity,
                              verbose_name='Признак страхования')  # Можно будет включить Тру это сделает выбор между Юр и Физ лицом
    mobile_number = models.IntegerField(verbose_name='Телефон')
    passport = models.OneToOneField('passport_date', on_delete=models.PROTECT, verbose_name='Паспортные данные')

    def __str__(self):
        surname = str(self.surname) + ' '
        name = str(self.name) + ' '
        patronymic = str(self.patronymic)
        FIO = surname + name + patronymic
        return FIO

    def get_absolute_url(self):
        return reverse('client', kwargs={'client_id': self.client_id})

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['date_create', 'surname', 'name', 'patronymic']


class passport_date(models.Model):
    passport_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='passport_id')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    surname = models.CharField(max_length=35, verbose_name='Фамилия')
    name = models.CharField(max_length=35, verbose_name='Имя')
    patronymic = models.CharField(max_length=35, blank=True, verbose_name='Отчество')
    series = models.IntegerField(validators=[MaxValueValidator(9999)], verbose_name='Серия')
    number = models.IntegerField(verbose_name='Номер')
    data_issue = models.DateField(verbose_name='Дата выдачи')
    division_code = models.CharField(max_length=10, verbose_name='Код подразделения')
    issued_by = models.CharField(max_length=255, verbose_name='Выдан')
    date_birth = models.DateField(verbose_name='Дата рождения')
    place_birth = models.CharField(max_length=255, verbose_name='Место рождения')
    region = models.ForeignKey('region', on_delete=models.PROTECT, verbose_name='Регион')

    def __str__(self):
        surname = str(self.surname) + ' '
        name = str(self.name) + ' '
        patronymic = str(self.patronymic)
        FIO = surname + name + patronymic
        return FIO

    class Meta:
        verbose_name = 'Паспортные данные'
        verbose_name_plural = 'Паспортные данные'
        ordering = ['surname', 'name', 'patronymic', 'date_birth']


class region(models.Model):
    region_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='region_id')
    region_name = models.CharField(max_length=100)

    def __str__(self):
        return self.region_name

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'
        ordering = ['region_id', 'region_name']


class insurance(models.Model):
    insurance_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False,
                                       verbose_name='insurance_id')
    max_payment = models.DecimalField(max_digits=18, decimal_places=3, verbose_name='Страховая сумма(руб)')
    cost = models.DecimalField(max_digits=18, decimal_places=3, verbose_name='Стоимость(руб)')
    date_conclusion_contract = models.DateTimeField(auto_now_add=True, verbose_name='Дата заключения контракта')
    period_start_date = models.DateField(verbose_name='Дата начала')
    period_end_date = models.DateField(verbose_name='Дата окончания')
    type = models.ForeignKey('type_insurance', on_delete=models.PROTECT, verbose_name='Тип страховки')
    client_id = models.ForeignKey('clients', on_delete=models.PROTECT, verbose_name='Клиент')
    agent_id = models.ForeignKey('agent', on_delete=models.PROTECT, verbose_name='Агент') # Здесь прописать название таблицы Усер и подвязатьт таким обарзом
    region_id = models.ForeignKey('region', on_delete=models.PROTECT, verbose_name='Регион')

    def __str__(self):
        insurance = str(self.insurance_id)
        return insurance

    def get_absolute_url(self):
        return reverse('insurance', kwargs={'insurance_id': self.insurance_id})

    class Meta:
        verbose_name = 'Страховка'
        verbose_name_plural = 'Страховки'
        ordering = ['insurance_id']


class type_insurance(models.Model):
    type_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='type_id')
    type_name = models.CharField(max_length=100, db_index=True, verbose_name='Тип страховки')

    def __str__(self):
        return self.type_name

    def get_absolute_url(self):
        return reverse('type', kwargs={'type_id': self.type_id})

    class Meta:
        verbose_name = 'Тип страховки'
        verbose_name_plural = 'Типы страховки'
        ordering = ['type_id']


class additional_service(models.Model):
    additional_service_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False,
                                                verbose_name='additional_service_id')
    cost = models.DecimalField(max_digits=18, decimal_places=3, verbose_name='Стоимость')
    insurance = models.ForeignKey('insurance', on_delete=models.PROTECT, verbose_name='Основная страховка')
    type_service = models.ForeignKey('type_service', on_delete=models.PROTECT, verbose_name='Тип доп. услуги')

    class Meta:
        verbose_name = 'Дополнительные услуга'
        verbose_name_plural = 'Дополнительные услуги'
        ordering = ['additional_service_id']


class type_service(models.Model):
    type_service_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False,
                                          verbose_name='type_service_id')
    type_name = models.CharField(max_length=100, verbose_name='Тип дополнительной услуги')

    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name = 'Тип доп. услуги'
        verbose_name_plural = 'Тип доп. услуг'
        ordering = ['type_service_id']


class payments(models.Model):
    payment_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='payment_id')
    plat_date = models.DateField()
    plat = models.DecimalField(max_digits=18, decimal_places=3)
    debt = models.DecimalField(max_digits=18, decimal_places=3)
    insurance = models.ForeignKey('insurance', on_delete=models.PROTECT)

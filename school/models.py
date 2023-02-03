from django.db import models


class Course(models.Model):
    AGE_CATEGORY = [
        ('FROM_8_TO_10_Y_O', '8-10 лет'),
        ('FROM_10_TO_12_Y_O', '10-12 лет'),
        ('FROM_12_TO_14_Y_O', '12-14 лет'),
        ('FROM_14_TO_16_Y_O', '14-16 лет'),
    ]
    name = models.CharField(
        'Название курса',
        max_length=50
    )
    description = models.TextField(
        'Полное описание курса'
    )
    short_description = models.CharField(
        'Краткое описание курса',
        max_length=100
    )
    age_category = models.CharField(
        'Возрастная категория',
        max_length=30,
        choices=AGE_CATEGORY
    )
    duration = models.CharField(
        'Длительность курса',
        max_length=30
    )
    is_recomended = models.BooleanField(
        'Рекомендован?',
        default=False
    )
    main_image = models.ImageField(
        'Изображение курса',
        default='defautl_course_image.png'
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class School(models.Model):
    address = models.CharField(
        'Адрес школы',
        max_length=150
    )
    main_image = models.ImageField(
        'Фото школы'
    )
    city = models.CharField(
        'Город',
        max_length=50,
        blank=True
    )

    def __str__(self):
        return f'{self.address}'

    class Meta:
        verbose_name = 'Школа'
        verbose_name_plural = 'Школы'



class School_Courses(models.Model):
    TIME_TO_CLASS = [
        ('FROM_10_TO_12', 'С 10:00 до 12:00'),
        ('FROM_12_TO_14', 'С 12:00 до 14:00'),
        ('FROM_14_TO_16', 'С 14:00 до 16:00'),
        ('FROM_16_TO_18', 'С 16:00 до 18:00'),
        ('FROM_18_TO_20', 'С 18:00 до 20:00')
    ]

    DAYS_OF_WEEK_FOR_CLASSES = [
        ('MONDAY', 'Понедельник'),
        ('Tuesday', 'Вторник'),
        ('Wednesday', 'Среда'),
        ('Thursday', 'Четверг'),
        ('Friday', 'Пятница'),
    ]
    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        verbose_name='Школа'
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name='Курс'
    )
    class_day = models.CharField(
        'День недели',
        choices=DAYS_OF_WEEK_FOR_CLASSES,
        max_length=25
    )
    class_time = models.CharField(
        'Время',
        choices=TIME_TO_CLASS,
        max_length=25
    )

    def __str__(self):
        return f'{self.course} в {self.school}'

    class Meta:
        verbose_name = 'Курс в школе'
        verbose_name_plural = 'Курсы в школах'


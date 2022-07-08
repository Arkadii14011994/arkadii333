from django.db import models



class School(models.Model):
    GYMNASIUM = 'Gymnasium'
    LYCEUM = 'Lyceum'
    SECONDARY = 'Secondary'
    PRIVATE = 'Private'
    STATE = 'State'

    SCHOOL_STATUS = (
        (SECONDARY, 'Средняя'),
        (GYMNASIUM, 'Гимназия'),
        (LYCEUM, 'Лицей')
    )
    SCHOOL_TYPE = (
        ( PRIVATE, 'Частная'),
        (STATE, 'Государственная')
    )
    name = models.CharField(max_length=255,verbose_name='название школы')
    adress = models.CharField(max_length=500, verbose_name='Адрес')
    status_school = models.CharField(
        max_length=10, verbose_name='Статус школы',
        choices=SCHOOL_STATUS,default=GYMNASIUM
    )

    school_type = models.CharField(
        max_length=10, verbose_name='Тип школы',
        choices=SCHOOL_TYPE,default=STATE
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'school'
        verbose_name = 'Школа'
        verbose_name_plural = 'Школы'
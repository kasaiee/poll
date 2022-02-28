from django.db import models


ISARGARI_TYPES = (
    ('25', '25%'),
    ('50', '50%'),
    ('75', '75%'),
    ('90', '90%'),
)

class Poll(models.Model):
    full_name = models.CharField('نام و نام خانوادگی', max_length=120, null=True)
    vekalat_id = models.CharField('شماره پروانه وکالت', max_length=120, null=True)
    vaziat_isargari = models.CharField('وضعیت ایثارگری', choices=ISARGARI_TYPES, max_length=2, null=True)
    national_id = models.CharField('کد ملی', max_length=30, null=True)
    osviat_kanoon_vokala = models.CharField('عضویت کانون وکلا', max_length=70, null=True)

    def __str__(self):
        return self.full_name
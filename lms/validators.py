from rest_framework.serializers import ValidationError


class YouTubeValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        field_link_you_tube = 'https://www.youtube.com/'
        value_link = dict(value).get(self.field)
        if value_link != field_link_you_tube:
            raise ValidationError('Ошибка: ссылка на сторонний ресурс. Не соответсвует ссылке на видеохостинг YouTube')

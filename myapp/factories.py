import factory
from .models import Manga, MangaVolume, WeeklyRanking

class MangaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Manga

    title = factory.Faker('name')
    author = factory.Faker('name')
    description = factory.Faker('text')
    publication_date = factory.Faker('date_this_decade')

class MangaVolumeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MangaVolume

    manga = factory.SubFactory(MangaFactory)
    volume_number = factory.Sequence(lambda n: n)
    publication_date = factory.Faker('date_this_decade')

class WeeklyRankingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = WeeklyRanking

    ranking_date = factory.Faker('date_this_month')
    position = factory.Sequence(lambda n: n)
    manga_volume = factory.SubFactory(MangaVolumeFactory)
    sales = factory.Faker('random_number', digits=5)
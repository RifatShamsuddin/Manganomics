from django.test import TestCase
from myapp.models import Manga, MangaVolume, WeeklyRanking
from myapp.factories import MangaFactory, MangaVolumeFactory, WeeklyRankingFactory

class MangaTests(TestCase):
    def test_manga_creation(self):
        # Create a Manga instance using MangaFactory
        manga = MangaFactory.create()

        # Assertions to verify Manga instance creation
        self.assertIsInstance(manga, Manga)
        self.assertEqual(Manga.objects.count(), 1)  # Verify object count

    def test_manga_volume_creation(self):
        # Create related instances using factories
        manga = MangaFactory.create()
        volume = MangaVolumeFactory.create(manga=manga)

        # Assertions to verify MangaVolume instance creation
        self.assertEqual(volume.manga, manga)
        self.assertEqual(MangaVolume.objects.count(), 1)  # Verify object count

    def test_weekly_ranking_creation(self):
        # Create related instances using factories
        manga = MangaFactory.create()
        volume = MangaVolumeFactory.create(manga=manga)
        ranking = WeeklyRankingFactory.create(manga_volume=volume)

        # Assertions to verify WeeklyRanking instance creation
        self.assertEqual(ranking.manga_volume.manga, manga)
        self.assertEqual(WeeklyRanking.objects.count(), 1)  # Verify object count

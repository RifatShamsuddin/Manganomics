from django.db import models

class Manga(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    publication_date = models.DateField()

    # Additional fields can be added as needed

    def __str__(self):
        return self.title

class MangaVolume(models.Model):
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
    volume_number = models.IntegerField()
    publication_date = models.DateField()

    def __str__(self):
        return f"{self.manga.title} - Volume {self.volume_number}"


class WeeklyRanking(models.Model):
    ranking_date = models.DateField()
    position = models.IntegerField()
    manga_volume = models.ForeignKey(MangaVolume, on_delete=models.CASCADE)
    sales = models.IntegerField()

    def __str__(self):
        return f"{self.ranking_date} - #{self.position}: {self.manga_volume} - {self.sales}"
    

from django.contrib import admin
from .models import Manga, MangaVolume, WeeklyRanking

@admin.register(Manga)
class MangaAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'description','publication_date')
    search_fields = ('title', 'author')

@admin.register(MangaVolume)
class MangaVolumeAdmin(admin.ModelAdmin):
    list_display = ('manga', 'volume_number', 'publication_date')
    list_filter = ('publication_date',)
    search_fields = ('manga__title',)

@admin.register(WeeklyRanking)
class WeeklyRankingAdmin(admin.ModelAdmin):
    list_display = ('ranking_date', 'position', 'manga_volume','sales')
    list_filter = ('ranking_date',)
    search_fields = ('manga_volume__manga__title',)
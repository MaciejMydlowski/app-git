from django.contrib import admin

#from .models import Post
from .models import Przeglad
#from .models import MovieGenres, MovieActors, WatchedMovies, MovieReview #4,7
from .models import MatkiPszczele, TypUla, DodawanieUla
#admin.site.register(Post)
admin.site.register(Przeglad)

#7
#class MovieReviewInline(admin.TabularInline):
#    model = MovieReview
#class WatchedMoviesAdmin(admin.ModelAdmin):
#    inlines = [ MovieReviewInline ]
#7
#4
#admin.site.register(MovieGenres)
#admin.site.register(MovieActors)
#admin.site.register(WatchedMovies, WatchedMoviesAdmin)
#4
#admin.site.register(MovieReview)#7
admin.site.register(MatkiPszczele)
admin.site.register(TypUla)
admin.site.register(DodawanieUla)

from django.contrib import admin
from core.models import User, Team, Activity, Workout, Leaderboard

admin.site.register(User)
admin.site.register(Team)
admin.site.register(Activity)
admin.site.register(Workout)
admin.site.register(Leaderboard)

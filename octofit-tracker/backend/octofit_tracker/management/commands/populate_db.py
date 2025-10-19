from django.core.management.base import BaseCommand
from core.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Deleting old data...'))
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Creating teams...'))
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        self.stdout.write(self.style.SUCCESS('Creating users...'))
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel, is_superhero=True),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel, is_superhero=True),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc, is_superhero=True),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc, is_superhero=True),
        ]

        self.stdout.write(self.style.SUCCESS('Creating activities...'))
        Activity.objects.create(user=users[0], type='Web Swinging', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], type='Suit Training', duration=45, date=timezone.now().date())
        Activity.objects.create(user=users[2], type='Lasso Practice', duration=40, date=timezone.now().date())
        Activity.objects.create(user=users[3], type='Martial Arts', duration=50, date=timezone.now().date())

        self.stdout.write(self.style.SUCCESS('Creating workouts...'))
        w1 = Workout.objects.create(name='Hero Endurance', description='Endurance workout for heroes')
        w1.suggested_for.set([marvel, dc])
        w2 = Workout.objects.create(name='Strength Training', description='Strength workout for all')
        w2.suggested_for.set([marvel, dc])

        self.stdout.write(self.style.SUCCESS('Creating leaderboards...'))
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('Database populated with test data!'))

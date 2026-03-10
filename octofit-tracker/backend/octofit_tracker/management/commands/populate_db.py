from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel', members=['Iron Man', 'Spider-Man', 'Captain America'])
        dc = Team.objects.create(name='dc', members=['Superman', 'Batman', 'Wonder Woman'])

        # Create users
        User.objects.create(email='ironman@marvel.com', name='Iron Man', team='marvel')
        User.objects.create(email='spiderman@marvel.com', name='Spider-Man', team='marvel')
        User.objects.create(email='superman@dc.com', name='Superman', team='dc')
        User.objects.create(email='batman@dc.com', name='Batman', team='dc')

        # Create activities
        Activity.objects.create(user='Iron Man', type='run', duration=30, date='2026-03-10')
        Activity.objects.create(user='Spider-Man', type='swim', duration=45, date='2026-03-09')
        Activity.objects.create(user='Superman', type='fly', duration=60, date='2026-03-08')
        Activity.objects.create(user='Batman', type='cycle', duration=40, date='2026-03-07')

        # Create leaderboard
        Leaderboard.objects.create(team='marvel', points=150)
        Leaderboard.objects.create(team='dc', points=120)

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_for=['Iron Man', 'Batman'])
        Workout.objects.create(name='Swimming', description='Swim for 30 minutes', suggested_for=['Spider-Man'])
        Workout.objects.create(name='Flying', description='Fly for 1 hour', suggested_for=['Superman'])

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))

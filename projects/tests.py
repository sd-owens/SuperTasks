from django.test import TestCase
from datetime import date, timedelta

from django.contrib.auth.models import User

from .models import Project, Feature
from teams.models import Team

# Create your tests here.
class ProjectModelTests(TestCase):

    def setUp(self):
        self.test_user = User(username='test_user', password='test_user')
        self.test_team = Team(name="test_team")
        self.test_user.save()
        self.test_team.save()

    def test_not_overdue(self):
        """Verifies that the is_overdue check returns False
        if the project is not past the Due Date
        """
        today = date.today()
        tomorrow = today + timedelta(days=1)

        project = Project(name='not overdue', description='not overdue',
                            due_date=tomorrow)
        self.assertFalse(project.is_overdue())

    def test_overdue_past_due_date(self):
        """Verifies that the is_overdue check returns True
        if the project is past the Due Date
        """
        today = date.today()
        week_ago = today - timedelta(days=7)
        month_ago = today - timedelta(days=30)

        project = Project(name='overdue', description='overdue project',
                                   start_date=month_ago, due_date=week_ago)
        self.assertTrue(project.is_overdue())


    def test_overdue_past_due_date_but_completed(self):
        """Verifies that the is_overdue check returns False
        if the project is past the Due Date BUT the project
        is completed.
        """
        today = date.today()
        week_ago = today - timedelta(days=7)
        month_ago = today - timedelta(days=30)

        project = Project(name='completed', description='completed proejct',
                                   start_date=month_ago, due_date=week_ago, status=Project.ProjectStatus.COMPLETED)
        self.assertFalse(project.is_overdue())

    def test_set_to_done(self):
        "Verifies that setting a Project to done will set all of its Features to done."
        tomorrow = date.today() + timedelta(days=1)
        # Create a Project objects
        project = Project(name='test', description='test', due_date=tomorrow, project_team=self.test_team)
        project.save()

        # Create two Feature objects
        feature1 = project.feature_set.create(title='test1', name='test1', description='test1', due_date=tomorrow, assignee=self.test_user)
        feature1.save()
        feature2 = project.feature_set.create(title='test2', name='test2', description='test2', due_date=tomorrow, assignee=self.test_user)
        feature2.save()

        # Run the function we are testing
        project.set_to_done()

        # Test that the Project and its associated Features are all done
        self.assertEqual(project.status, Project.ProjectStatus.COMPLETED)
        for feature in project.feature_set.all():
            self.assertEqual(feature.status, Feature.FeatureStatus.DONE)

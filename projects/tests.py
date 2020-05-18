from django.test import TestCase
from datetime import date, timedelta

from .models import Project

# Create your tests here.
class ProjectModelTests(TestCase):

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

    # test that a project was made and modified
    def test_add_project(self):
        try:
            project = Project(name='completed', description='completed project', start_date=month_ago, due_date=week_ago, status=Project.ProjectStatus.COMPLETED)
            new_proj = Project.objects.get(name="completed")
            #edit project
            new_proj.name = "new_completed";
            self.assertEqual(new_proj.name, "new_completed")
            self.assertFalse(new_proj.is_overdue())
        except:
            self.fail("Failed Test: project did not match added project")

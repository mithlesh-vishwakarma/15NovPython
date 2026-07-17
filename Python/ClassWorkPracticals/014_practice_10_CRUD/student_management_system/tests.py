from django.test import TestCase
from django.urls import reverse

from student_management_system.models import Student


class StudentCrudTests(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            name="Alice",
            rollnumber=101,
            email="alice@example.com",
            age=20,
            contact=9876543210,
            course="BCA",
        )

    def test_update_student(self):
        response = self.client.post(
            reverse("update_data", args=[self.student.id]),
            {
                "name": "Alice Updated",
                "rollnumber": 202,
                "email": "alice.updated@example.com",
                "age": 21,
                "contact": 9123456780,
                "course": "MCA",
            },
        )

        self.assertRedirects(response, reverse("display_data"))
        self.student.refresh_from_db()
        self.assertEqual(self.student.name, "Alice Updated")
        self.assertEqual(self.student.course, "MCA")

    def test_delete_student(self):
        response = self.client.get(reverse("delete_data", args=[self.student.id]))

        self.assertRedirects(response, reverse("display_data"))
        self.assertFalse(Student.objects.filter(id=self.student.id).exists())

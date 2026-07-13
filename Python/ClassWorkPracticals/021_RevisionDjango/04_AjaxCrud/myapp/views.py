from django.shortcuts import render
from django.http import JsonResponse
from myapp.models import Student

# Create your views here.

def index(request):
    return render(request, "index.html")

def get_students(request):
    students = list(Student.objects.all().values('id', 'name', 'email', 'age'))
    return JsonResponse({'students': students}, status=200)

def add_student(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        age = request.POST.get("age", "").strip()

        if not name or not email or not age:
            return JsonResponse({"error": "All fields are required."}, status=400)

        try:
            age = int(age)
            if age <= 0:
                return JsonResponse({"error": "Age must be a positive integer."}, status=400)
        except ValueError:
            return JsonResponse({"error": "Invalid age format."}, status=400)

        if Student.objects.filter(email=email).exists():
            return JsonResponse({"error": "A student with this email already exists."}, status=400)

        student = Student.objects.create(name=name, email=email, age=age)
        return JsonResponse({
            "message": "Student registered successfully!",
            "student": {
                "id": student.id,
                "name": student.name,
                "email": student.email,
                "age": student.age
            }
        }, status=201)
    return JsonResponse({"error": "Invalid request method."}, status=405)

def update_student(request):
    if request.method == "POST":
        student_id = request.POST.get("id")
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        age = request.POST.get("age", "").strip()

        if not student_id or not name or not email or not age:
            return JsonResponse({"error": "All fields are required."}, status=400)

        try:
            age = int(age)
            if age <= 0:
                return JsonResponse({"error": "Age must be a positive integer."}, status=400)
        except ValueError:
            return JsonResponse({"error": "Invalid age format."}, status=400)

        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return JsonResponse({"error": "Student not found."}, status=404)

        if Student.objects.filter(email=email).exclude(id=student_id).exists():
            return JsonResponse({"error": "A student with this email already exists."}, status=400)

        student.name = name
        student.email = email
        student.age = age
        student.save()

        return JsonResponse({
            "message": "Student updated successfully!",
            "student": {
                "id": student.id,
                "name": student.name,
                "email": student.email,
                "age": student.age
            }
        }, status=200)
    return JsonResponse({"error": "Invalid request method."}, status=405)

def delete_student(request):
    if request.method == "POST":
        student_id = request.POST.get("id")
        if not student_id:
            return JsonResponse({"error": "Student ID is required."}, status=400)

        try:
            student = Student.objects.get(id=student_id)
            student.delete()
            return JsonResponse({"message": "Student deleted successfully!"}, status=200)
        except Student.DoesNotExist:
            return JsonResponse({"error": "Student not found."}, status=404)
    return JsonResponse({"error": "Invalid request method."}, status=405)
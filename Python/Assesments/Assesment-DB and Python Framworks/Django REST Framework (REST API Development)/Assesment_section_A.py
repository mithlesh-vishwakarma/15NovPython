# ============================================================
#               SECTION A - QUESTION & ANSWER
# ============================================================


# QUESTION 1:
# Explain why REST APIs are preferred for mobile and
# frontend-heavy apps.

# ANSWER:
# REST APIs are preferred because they allow the frontend
# and backend to communicate independently through HTTP.

# The frontend can be built using React, Angular, Vue,
# Android, iOS, etc., while the backend provides data
# through REST API endpoints.

# Example:

#     Mobile / React / Angular
#               |
#               | HTTP Request
#               ↓
#            REST API
#               |
#               ↓
#            Database

# The API usually sends and receives data in JSON format.

# Main benefits:
# - Frontend and backend are separated.
# - Same API can be used by different platforms.
# - JSON is easy to exchange between frontend and backend.
# - APIs are easy to scale and maintain.
# - Mobile and web applications can use the same backend.


# ------------------------------------------------------------

# QUESTION 2:
# Explain how serializers act as a validation layer and
# how to implement custom field-level validation.

# ANSWER:
# In Django REST Framework, serializers convert data between
# Python objects and JSON. They also validate incoming data
# before it is saved to the database.

# Flow:

#     JSON Request
#          ↓
#      Serializer
#          ↓
#       Validation
#          ↓
#        Model
#          ↓
#       Database

# Example:

#     from rest_framework import serializers

#     class DoctorSerializer(serializers.ModelSerializer):

#         class Meta:
#             model = Doctor
#             fields = "__all__"

# A custom field-level validation method is created using:

#     validate_<field_name>()

# Example:

#     def validate_name(self, value):

#         if len(value) < 3:
#             raise serializers.ValidationError(
#                 "Name must contain at least 3 characters."
#             )

#         return value

# If the value is invalid, ValidationError is raised and
# the data is not saved.


# ------------------------------------------------------------

# QUESTION 3:
# Explain the importance of using appropriate HTTP status
# codes (201 Created vs 200 OK) for API outcomes.

# ANSWER:
# HTTP status codes tell the client what happened with the
# request.

# 200 OK means the request was successful.

# Example:

#     GET /doctors/1/

#     Response:
#     200 OK

# This means the doctor was successfully retrieved.

# 201 Created means a new resource was successfully created.

# Example:

#     POST /doctors/

#     Response:
#     201 Created

# This means a new doctor record was successfully created.

# Common status codes:

#     200 OK
#     → Successful request

#     201 Created
#     → New resource created

#     400 Bad Request
#     → Invalid request

#     404 Not Found
#     → Resource not found

#     500 Internal Server Error
#     → Server-side error

# Using the correct status code allows the frontend or client
# to understand the result of the API request correctly.


# ------------------------------------------------------------

# QUESTION 4:
# Explain why pagination is required when listing doctors
# and how it impacts database performance.

# ANSWER:
# Pagination is required when there are many doctor records.

# Without pagination:

#     Database
#         ↓
#     100,000 doctors
#         ↓
#     API
#         ↓
#     Huge JSON response
#         ↓
#     Slow frontend

# With pagination, the API returns only a smaller set of
# records at a time.

# Example:

#     Page 1 → Doctors 1-10
#     Page 2 → Doctors 11-20
#     Page 3 → Doctors 21-30

# Benefits:

# - Smaller API responses.
# - Less data transferred.
# - Better frontend performance.
# - Lower memory usage.
# - More efficient handling of large datasets.

# Django REST Framework provides pagination classes such as:

#     PageNumberPagination

# and:

#     LimitOffsetPagination


# ------------------------------------------------------------

# QUESTION 5:
# Explain the benefits of ViewSets over APIView for rapid
# CRUD development.

# ANSWER:
# APIView requires developers to manually implement different
# HTTP methods such as GET, POST, PUT and DELETE.

# Example:

#     class DoctorList(APIView):

#         def get(self, request):
#             ...

#         def post(self, request):
#             ...

# With ModelViewSet, Django REST Framework provides standard
# CRUD operations with much less code.

# Example:

#     from rest_framework import viewsets

#     class DoctorViewSet(viewsets.ModelViewSet):

#         queryset = Doctor.objects.all()
#         serializer_class = DoctorSerializer

# ModelViewSet provides operations such as:

#     GET
#     → List / Retrieve

#     POST
#     → Create

#     PUT
#     → Update

#     PATCH
#     → Partial Update

#     DELETE
#     → Delete

# When combined with DefaultRouter, standard API URLs are
# automatically generated.

# Main benefits:

# - Less boilerplate code.
# - Faster CRUD development.
# - Standard CRUD behavior.
# - Automatic routing with routers.
# - Easier maintenance.


# ------------------------------------------------------------

# QUESTION 6:
# Explain the use of Atomic Transactions (transaction.atomic)
# when creating related doctor records to ensure data
# integrity.

# ANSWER:
# transaction.atomic() is used to make multiple database
# operations behave as one transaction.

# Suppose creating a doctor requires:

#     Create Doctor
#         ↓
#     Create Profile
#         ↓
#     Create Address

# If the Address creation fails, we do not want the Doctor
# and Profile to remain saved.

# Without a transaction:

#     Doctor   → CREATED
#     Profile  → CREATED
#     Address  → FAILED

# This can create partial or orphan data.

# With transaction.atomic():

#     START TRANSACTION
#           ↓
#     Create Doctor
#           ↓
#     Create Profile
#           ↓
#     Create Address
#           ↓
#        SUCCESS
#           ↓
#        COMMIT

# If something fails:

#     START TRANSACTION
#           ↓
#     Create Doctor
#           ↓
#     Create Profile
#           ↓
#        ERROR
#           ↓
#       ROLLBACK
#           ↓
#     All changes are undone

# Example:

#     from django.db import transaction

#     @transaction.atomic
#     def perform_create(self, serializer):
#         serializer.save()

# The main purpose of transaction.atomic() is to maintain
# database integrity and prevent partial or incomplete data
# from being committed.


# ============================================================
#                  SECTION A QUICK MEMORY
# ============================================================

# REST API
# → Frontend ↔ API ↔ Database

# Serializer
# → Convert + Validate data

# 200 OK
# → Successful request

# 201 Created
# → New resource created

# Pagination
# → Return data in smaller portions

# ModelViewSet
# → Fast CRUD development

# DefaultRouter
# → Automatically creates routes

# transaction.atomic()
# → All operations succeed or all rollback

# ============================================================
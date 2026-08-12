from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

"""
=============================================================================
Task 4: JSON vs XML Comparison
=============================================================================

JSON (JavaScript Object Notation):
- Lightweight, data-centric format using key-value pairs.
- Modern standard for web APIs due to native parsing in JavaScript and low overhead.

Sample Flipkart Product (JSON):
{
    "name": "Sony Wireless Headphones",
    "price": 2999.00
}

XML (eXtensible Markup Language):
- Document-centric markup language using custom tags.
- More verbose with schema support (XSD) and metadata attributes.

Sample Flipkart Product (XML):
<product>
    <name>Sony Wireless Headphones</name>
    <price>2999.00</price>
</product>
=============================================================================
"""

@api_view(['GET'])
def hello_spotify(request):
    return Response({"message": "Hello, Spotify Fans!"})


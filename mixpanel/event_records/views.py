from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import EventRecord
import json

@csrf_exempt
def create(request):
    """Create a new event record."""

    if request.method != "POST":
        return JsonResponse({'message': 'Invalid request method'}, status=405)

    data = json.loads(request.body)
    event_record = EventRecord.objects.create(
        name=data["name"],
        description=data["description"],
    )

    return JsonResponse({
        "id": event_record.id,
        "name": event_record.name,
        "description": event_record.description,
    })

def index(request):
    """List all event records."""
    if  request.method != "GET":
        return JsonResponse({'message': 'Invalid request method'}, status=405)

    event_records = EventRecord.objects.all()

    return JsonResponse({
        "event_records": [
            {
                "id": event_record.id,
                "name": event_record.name,
                "description": event_record.description,
            }
            for event_record in event_records
        ]
    })

def show(request, event_record_id):
    """Show a single event record."""
    if  request.method != "GET":
        return JsonResponse({'message': 'Invalid request method'}, status=405)

    event_record = EventRecord.objects.get(id=event_record_id)

    return JsonResponse({
        "id": event_record.id,
        "name": event_record.name,
        "description": event_record.description,
    })

@csrf_exempt
def update(request, event_record_id):
    """Update a single event record."""
    if  request.method != "PUT":
        return JsonResponse({'message': 'Invalid request method'}, status=405)

    data = json.loads(request.body)
    event_record = EventRecord.objects.get(id=event_record_id)
    event_record.name = data["name"]
    event_record.description = data["description"]
    event_record.save()

    return JsonResponse({
        "id": event_record.id,
        "name": event_record.name,
        "description": event_record.description,
    })

@csrf_exempt
def delete(request, event_record_id):
    """Delete a single event record."""
    if  request.method != "POST":
        return JsonResponse({'message': 'Invalid request method'}, status=405)

    event_record = EventRecord.objects.get(id=event_record_id)
    event_record.delete()

    return JsonResponse({
        "message": "Event record deleted successfully!"
    })
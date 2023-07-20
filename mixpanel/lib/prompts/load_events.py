from mixpanel.event_records.models import EventRecord



def load_events():
    """
    Load events from the database.
    """
    return EventRecord.objects.all()


def create_csv_string_from_events(events):
    """
    Create a CSV string from a list of events.
    """
    csv_string = "event_name,description\n"
    for event in events:
        csv_string += f"{event.event_name},{event.description}\n"
    return csv_string

def main():
    """
    Load events from the database and print them to the console.
    """
    events = load_events()
    csv_string = create_csv_string_from_events(events)
    print(csv_string)
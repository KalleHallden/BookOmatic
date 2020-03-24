class Event:
    def __init__(self, UserID, EventID, name, person_first_name, person_last_name, event_start, event_end, created_at):
        self.uuid = UserID
        self.eid = EventID
        self.name = name
        self.person_first_name = person_first_name
        self.person_last_name = person_last_name
        self.event_start = event_start
        self.event_end = event_end
        self.created_at = created_at
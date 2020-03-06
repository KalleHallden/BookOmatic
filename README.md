Description:
- This is a project that intends to automate the process of booking meetings.

Use case:
- :woman: gets an email from :man: wanting to book a meeting
- :woman: sends back a link to a site 
- :man: opens the site and sees a UI with available time slots
- :man: presses a time slot and creates a booking
- :woman: gets notified about the requested booking
- :woman: can approve or disapprove the booking

Requirements:
- Should be able to add events in google calendar
- Should be able to send email notifications
- Should be able to show available spots
- Should check user calendar in case they book something into available spots
- User should be able to pick which times are going to be available to book, weekly, monthly or yearly (for instance Tuesdays at 3 PM is available all year, Monday at 2 PM is only available today etc)
- The user that books meeting should be able to add in details for the meeting
    - Might have options like: type of meeting [Phone, Video, Face to Face]
    - Adding in a note for what the meeting is about 
    - Name of booker, name of the company
    - Phone number and email
    - if it's a video conference an option for adding a link to the site of the meeting is required
- Main user should be able to approve or disapprove booking 

Edge cases:
- :woman: is in the process of booking an appointment and :man: books it before :woman: finishes. So once :woman: is done it is no longer available.
    - Solution: When a user presses a time slot it becomes unavailable straight away. And if they cancel or get disapproved it will become available again.

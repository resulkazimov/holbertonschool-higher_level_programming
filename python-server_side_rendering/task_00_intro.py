#!/usr/bin/python3
import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Invalid input type: template should be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Invalid input type: attendees should be a list of dictionaries.")
        return

    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    for i, attendee in enumerate(attendees, start=1):
        processed_template = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            placeholder = "{" + key + "}"
            processed_template = processed_template.replace(placeholder, str(value))
        
        filename = "output_{}.txt".format(i)
        if os.path.exists(filename):
            pass
            
        with open(filename, "w", encoding="utf-8") as f:
            f.write(processed_template)

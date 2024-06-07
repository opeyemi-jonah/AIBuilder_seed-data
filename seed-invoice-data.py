import random
import datetime
import names

def generate_random_studentId():
    return ''.join(random.choices('0123456789', k=10))

def generate_random_date():
    start_date = datetime.date(2023, 1, 1)
    end_date = datetime.date(2024, 12, 31)
    return (start_date + (end_date - start_date) * random.random()).strftime("%d-%b-%y")

def generate_random_student_name(num_entries):
    first_names = [names.get_first_name() for _ in range(num_entries)]
    last_names = [names.get_last_name() for _ in range(num_entries)]
    return f"{random.choice(first_names)}, {random.choice(last_names)}"

def generate_random_charges(auth_no, item_number):

    if auth_no == "AUTH NO:":
        charges = [round(random.uniform(5, 1000), 2) for _ in range(1)]
        charges.append(sum(charges))
    else:
        charges = [round(random.uniform(5, 1000), 2) for _ in range(item_number)]
        charges.append(sum(charges))
    return '\n'.join([f"{charge:.2f}" for charge in charges])

def generate_random_entry(num_entries):
    fee_type = "\n" + random.choice([
        "Received FA", "Received OS", "Received FA & OS",
        "Received partial OS", "Received partial FA",
        "Received partial FA & OS"
    ])
    term = random.choice(["202380", "202390", "202400"])
    standard_fees = [
        "Technology/Facility Fee", "Administrative Service Fee",
        random.choice(["", "Student Payment Plan Fee"]),
        "Registration Fee", random.choice(["", "Book Store Charges (Included)"])
    ]
    joined_standard_fees = "\n".join(standard_fees)
    TUITION_TYPES = "\n" + random.choice([
        "Resident Tuition", "Summer Resident Tuition", "Fall Resident Tuition",
        "Spring NonResident Tuition", "Summer NonResident Tuition",
        "Fall NonResident Tuition", "Spring Summer out of District Tuition",
        "Fall out of District Tuition", "Spring out of District Tuition"
    ])
    auth_no = "\n" + random.choice(["AUTH NO:", ""])
    student_name = generate_random_student_name(num_entries)
    charges = generate_random_charges(auth_no.strip(), len(standard_fees) + 1)
    student_id = generate_random_studentId()
    date = generate_random_date()

    if auth_no.strip() == "AUTH NO:":
        return {
            "@odata.type": "#Microsoft.Dynamics.CRM.expando",
            "DESCRIPTION": {
                "@odata.type": "#Microsoft.Dynamics.CRM.expando",
                "value": f"{student_name}{fee_type}\nAdministrative Service Fee\nSTUDENT TOTALS",
                "displayName": "DESCRIPTION",
                "fieldType": "string",
                "text": f"{student_name}{fee_type}\nAdministrative Service Fee\nSTUDENT TOTALS",
            },
            "CHARGES": {
                "@odata.type": "#Microsoft.Dynamics.CRM.expando",
                "value": charges,
                "displayName": "CHARGES",
                "fieldType": "string",
                "text": charges
            },
            "ITEM_0025c1675f23ad10d3d1e0df32398367665": {
                "@odata.type": "#Microsoft.Dynamics.CRM.expando",
                "value": f"{student_id}{auth_no}\n{date}\n{date}",
                "displayName": "ITEM DATE",
                "fieldType": "string",
                "text": f"{student_id}{auth_no}\n{date}\n{date}"
            },
            "TERM": {
                "@odata.type": "#Microsoft.Dynamics.CRM.expando",
                "value": term,
                "displayName": "TERM",
                "fieldType": "string",
                "text": term
            }
        }
    else:
        return {
            "@odata.type": "#Microsoft.Dynamics.CRM.expando",
            "DESCRIPTION": {
                "@odata.type": "#Microsoft.Dynamics.CRM.expando",
                "value": f"{student_name}\n{joined_standard_fees}{TUITION_TYPES}\nSTUDENT TOTALS",
                "displayName": "DESCRIPTION",
                "fieldType": "string",
                "text": f"{student_name}\n{joined_standard_fees}{TUITION_TYPES}\nSTUDENT TOTALS",
            },
            "CHARGES": {
                "@odata.type": "#Microsoft.Dynamics.CRM.expando",
                "value": charges,
                "displayName": "CHARGES",
                "fieldType": "string",
                "text": charges
            },
            "ITEM_0025c1675f23ad10d3d1e0df32398367665": {
                "@odata.type": "#Microsoft.Dynamics.CRM.expando",
                "value": f"{student_id}\n{date}\n{date}\n{date}\n{date}\n{date}",
                "displayName": "ITEM DATE",
                "fieldType": "string",
                "text": f"{student_id}\n{date}\n{date}\n{date}\n{date}\n{date}"
            },
            "TERM": {
                "@odata.type": "#Microsoft.Dynamics.CRM.expando",
                "value": term,
                "displayName": "TERM",
                "fieldType": "string",
                "text": term
            }
        }

def generate_seed_data(num_entries):
    return [generate_random_entry(num_entries) for _ in range(num_entries)]

# Generate 5 entries as an example
seed_data = generate_seed_data(5)
print(seed_data)

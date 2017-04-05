import json


cached_contact_data = {}


def search(query):
    contact_data = get_contact_data()
    if contact_data and query:
        return json.dumps(search_by_all_fields(query, contact_data))
    else:
        return ''


def search_by_name(query, contact_data):
    result = []
    for contact in contact_data:
        if query in contact['name']:
            result.append(contact)
    return result


def search_by_all_fields(query, contact_data):
    query = query.lower()
    result = []
    for contact in contact_data:
        if contact_matches_query(query, contact):
            result.append(contact)
    return result


def contact_matches_query(query, contact):
    for val in contact:
        if isinstance(contact[val], list):
            for subval in contact[val]:
                if query in subval.lower():
                    return True
        else:
            if query in contact[val].lower():
                return True
    return False


def get_contact_data():
    global cached_contact_data
    if not cached_contact_data:
        cached_contact_data = load_contact_data()
    contact_data = cached_contact_data
    return contact_data


def load_contact_data():
    contact_data = {}
    with open('data.json') as json_data:
        contact_data = json.load(json_data)
    return contact_data


def get_mock_result():
    return """
        [
        {
            "city": "Gelbressee", 
            "name": "Nero Acosta", 
            "country": "Panama", 
            "company": "Lacus Cras Associates", 
            "job_history": [
                ""
            ], 
            "email": "tempus.non.lacinia@ultricesposuerecubilia.com"
        }, 
        {
            "city": "Westmount", 
            "name": "Ferris Yates", 
            "country": "Peru", 
            "company": "Eu Euismod Ac Corp.", 
            "job_history": [
                ""
            ], 
            "email": "scelerisque.scelerisque.dui@Nullamvitaediam.org"
        }, 
        {
            "city": "Cache Creek", 
            "name": "Germaine Griffin", 
            "country": "Oman", 
            "company": "Diam Sed Industries", 
            "job_history": [
                "Finale", 
                "Cakewalk"
            ], 
            "email": "dolor.Fusce@consectetueradipiscingelit.net"
        }] 
        """
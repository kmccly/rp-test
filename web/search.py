contact_data = ''

def search( query ):
    contact_data = get_contact_data()
    if contact_data and query:
        return contact_data
    else:
        return ''


def get_contact_data():
    global contact_data
    if not contact_data:
        contact_data = get_mock_result()
    return contact_data


def get_mock_result():
    print('loading data...')
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
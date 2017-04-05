def search( query ):
    if query:
        return get_mock_result()
    else:
        return ''


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
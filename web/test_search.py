from unittest import TestCase

import search


class TestSearch(TestCase):

    def test_search_by_name_should_return_empty(self):
        contact_data = [
            {
                "city": "Rennes",
                "name": "Ivan Riley",
                "country": "Burkina Faso",
                "company": "Nonummy Fusce Ltd",
                "job_history": [
                    "Apple Systems",
                    "Google"
                ],
                "email": "tincidunt.orci@convallisdolorQuisque.co.uk"
            },
            {
                "city": "San Miguel",
                "name": "Ignatius Tate",
                "country": "Saudi Arabia",
                "company": "Etiam Ligula Consulting",
                "job_history": [
                    "Apple Systems",
                    "Cakewalk"
                ],
                "email": "vitae@metusInnec.org"
            },
            {
                "city": "Saint-Remy",
                "name": "Nyssa Hammond",
                "country": "Mozambique",
                "company": "Dui Nec Tempus Inc.",
                "job_history": [
                    "Chami",
                    "Cakewalk"
                ],
                "email": "dolor@adipiscingelitEtiam.org"
            }
        ]
        result = search.search_by_name('blah', contact_data)
        assert len(result) == 0

    def test_search_by_name_should_return_one_result(self):
        contact_data = [
            {
                "city": "Rennes",
                "name": "Ivan Riley",
                "country": "Burkina Faso",
                "company": "Nonummy Fusce Ltd",
                "job_history": [
                    "Apple Systems",
                    "Google"
                ],
                "email": "tincidunt.orci@convallisdolorQuisque.co.uk"
            },
            {
                "city": "San Miguel",
                "name": "Ignatius Tate",
                "country": "Saudi Arabia",
                "company": "Etiam Ligula Consulting",
                "job_history": [
                    "Apple Systems",
                    "Cakewalk"
                ],
                "email": "vitae@metusInnec.org"
            },
            {
                "city": "Saint-Remy",
                "name": "Nyssa Hammond",
                "country": "Mozambique",
                "company": "Dui Nec Tempus Inc.",
                "job_history": [
                    "Chami",
                    "Cakewalk"
                ],
                "email": "dolor@adipiscingelitEtiam.org"
            }
        ]
        result = search.search_by_name('Nyssa', contact_data)
        assert len(result) == 1

    def test_search_by_name_should_return_one_result(self):
        contact_data = [
            {
                "city": "Rennes",
                "name": "Ivan Riley",
                "country": "Burkina Faso",
                "company": "Nonummy Fusce Ltd",
                "job_history": [
                    "Apple Systems",
                    "Google"
                ],
                "email": "tincidunt.orci@convallisdolorQuisque.co.uk"
            },
            {
                "city": "San Miguel",
                "name": "Ignatius Tate",
                "country": "Saudi Arabia",
                "company": "Etiam Ligula Consulting",
                "job_history": [
                    "Apple Systems",
                    "Cakewalk"
                ],
                "email": "vitae@metusInnec.org"
            },
            {
                "city": "Saint-Remy",
                "name": "Nyssa Hammond",
                "country": "Mozambique",
                "company": "Dui Nec Tempus Inc.",
                "job_history": [
                    "Chami",
                    "Cakewalk"
                ],
                "email": "dolor@adipiscingelitEtiam.org"
            }
        ]
        result = search.search_by_name('i', contact_data)
        assert len(result) == 2

    def test_search_should_return_empty(self):
        contact_data = [
            {
                "city": "Rennes",
                "name": "Ivan Riley",
                "country": "Burkina Faso",
                "company": "Nonummy Fusce Ltd",
                "job_history": [
                    "Apple Systems",
                    "Google"
                ],
                "email": "tincidunt.orci@convallisdolorQuisque.co.uk"
            },
            {
                "city": "San Miguel",
                "name": "Ignatius Tate",
                "country": "Saudi Arabia",
                "company": "Etiam Ligula Consulting",
                "job_history": [
                    "Apple Systems",
                    "Cakewalk"
                ],
                "email": "vitae@metusInnec.org"
            },
            {
                "city": "Saint-Remy",
                "name": "Nyssa Hammond",
                "country": "Mozambique",
                "company": "Dui Nec Tempus Inc.",
                "job_history": [
                    "Chami",
                    "Cakewalk"
                ],
                "email": "dolor@adipiscingelitEtiam.org"
            },
            {
                "city": "Saint-Remy",
                "name": "Nyssa Hammond",
                "country": "Mozambique",
                "company": "Dui Nec Tempus Inc.",
                "job_history": [
                    "Chami",
                    "Cakewalk"
                ],
                "email": "dolor@adipiscingelitEtiam.org"
            }
        ]
        result = search.search_by_all_fields('_', contact_data)
        assert len(result) == 0

    def test_search_should_return_duplicate(self):
        contact_data = [
            {
                "city": "Rennes",
                "name": "Ivan Riley",
                "country": "Burkina Faso",
                "company": "Nonummy Fusce Ltd",
                "job_history": [
                    "Apple Systems",
                    "Google"
                ],
                "email": "tincidunt.orci@convallisdolorQuisque.co.uk"
            },
            {
                "city": "San Miguel",
                "name": "Ignatius Tate",
                "country": "Saudi Arabia",
                "company": "Etiam Ligula Consulting",
                "job_history": [
                    "Apple Systems",
                    "Cakewalk"
                ],
                "email": "vitae@metusInnec.org"
            },
            {
                "city": "Saint-Remy",
                "name": "Nyssa Hammond",
                "country": "Mozambique",
                "company": "Dui Nec Tempus Inc.",
                "job_history": [
                    "Chami",
                    "Cakewalk"
                ],
                "email": "dolor@adipiscingelitEtiam.org"
            },
            {
                "city": "Saint-Remy",
                "name": "Nyssa Hammond",
                "country": "Mozambique",
                "company": "Dui Nec Tempus Inc.",
                "job_history": [
                    "Chami",
                    "Cakewalk"
                ],
                "email": "dolor@adipiscingelitEtiam.org"
            }
        ]
        result = search.search_by_all_fields('Nyssa Hammond', contact_data)
        assert len(result) == 2

    def test_search_should_return_london_contact_only(self):
        contact_data = [
            {
                "city": "Rennes",
                "name": "Ivan Riley",
                "country": "Burkina Faso",
                "company": "Nonummy Fusce Ltd",
                "job_history": [
                    "Apple Systems",
                    "Google"
                ],
                "email": "tincidunt.orci@convallisdolorQuisque.co.uk"
            },
            {
                "city": "San Miguel",
                "name": "Ignatius Tate",
                "country": "Saudi Arabia",
                "company": "Etiam Ligula Consulting",
                "job_history": [
                    "Apple Systems",
                    "Cakewalk"
                ],
                "email": "vitae@metusInnec.org"
            },
            {
                "city": "Saint-Remy",
                "name": "Nyssa Hammond",
                "country": "Mozambique",
                "company": "Dui Nec Tempus Inc.",
                "job_history": [
                    "Chami",
                    "Cakewalk"
                ],
                "email": "dolor@adipiscingelitEtiam.org"
            },
            {
                "city": "London City",
                "name": "Nyssa Hammond",
                "country": "Mozambique",
                "company": "Dui Nec Tempus Inc.",
                "job_history": [
                    "Chami",
                    "Cakewalk"
                ],
                "email": "dolor@adipiscingelitEtiam.org"
            }
        ]
        result = search.search_by_all_fields('London City', contact_data)
        assert len(result) > 0 and result[0]["name"] == "Nyssa Hammond"
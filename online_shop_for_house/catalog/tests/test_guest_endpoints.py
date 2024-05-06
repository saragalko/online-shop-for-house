import pytest
from rest_framework.test import APITestCase
from django.shortcuts import reverse
from catalog.conftest import EVERYTHING_EQUALS_NOT_NONE

pytestmark = [pytest.mark.django_db]


class TestGuestEndpoints(APITestCase):
    fixtures = ['catalog/tests/fixtures/categories_fixture.json',
                'catalog/tests/fixtures/category_product_fixture.json',
                'catalog/tests/fixtures/discount_fixture.json',
                'catalog/tests/fixtures/seller_fixture.json'
                ]

    def test_categories_list_endpoints(self):
        url = reverse('categories')
        response = self.client.get(url)
        assert response.status_code == 200
        assert isinstance(response.data, list)
        assert response.data == [
            {
                "id": 1,
                "name": EVERYTHING_EQUALS_NOT_NONE,
                "description": "Мебель, гарнитура и все прилогающее"
            },
            {
                "id": 2,
                "name": EVERYTHING_EQUALS_NOT_NONE,
                "description": "От трусов с бабочкой до головного убора нормального"
            },
            {
                "id": 3,
                "name": EVERYTHING_EQUALS_NOT_NONE,
                "description": "Вся самая модная и лучшая одежда для прерасных дам"
            },
            {
                "id": 4,
                "name": EVERYTHING_EQUALS_NOT_NONE,
                "description": "Все для твоих любых домашних животных"
            }
        ]

    def test_category_product_endpoints(self):
        url = reverse('category-products', kwargs={'category_id': 1})
        response = self.client.get(url)
        assert response.status_code == 200
        assert isinstance(response.data, list)
        print(response.data)
        assert response.data == [
            {
                'id': 2,
                'name': EVERYTHING_EQUALS_NOT_NONE,
                'price': '294.55',
                'article': EVERYTHING_EQUALS_NOT_NONE,
                'images': []
            }
        ]

    def test_discount_endpoints(self):
        url = reverse('discounts')
        response = self.client.get(url)
        assert response.status_code == 200
        assert isinstance(response.data, list)
        assert response.data == [
            {
                "id": 1,
                "name": EVERYTHING_EQUALS_NOT_NONE,
                "percent": 5,
                "date_start": "2024-04-01",
                "date_end": EVERYTHING_EQUALS_NOT_NONE
            },
            {
                "id": 2,
                "name": EVERYTHING_EQUALS_NOT_NONE,
                "percent": 20,
                "date_start": "2024-04-14",
                "date_end": EVERYTHING_EQUALS_NOT_NONE
            },
            {
                "id": 3,
                "name": EVERYTHING_EQUALS_NOT_NONE,
                "percent": 40,
                "date_start": "2024-04-12",
                "date_end": EVERYTHING_EQUALS_NOT_NONE
            }
        ]

    def test_seller_endpoints(self):
        url = reverse('sellers')
        response = self.client.get(url)
        assert response.status_code == 200
        assert isinstance(response.data, list)
        assert response.data == [
            {
                "id": 2,
                "name": EVERYTHING_EQUALS_NOT_NONE,
                "description": EVERYTHING_EQUALS_NOT_NONE,
                "contact": EVERYTHING_EQUALS_NOT_NONE
            },
            {
                "id": 3,
                "name": EVERYTHING_EQUALS_NOT_NONE,
                "description": EVERYTHING_EQUALS_NOT_NONE,
                "contact": EVERYTHING_EQUALS_NOT_NONE
            }
        ]

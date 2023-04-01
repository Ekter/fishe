# tests/test_models.py
from django.test import TestCase

from ..models import Probe
from .factories import ProbeFactory


class CompanyTestCase(TestCase):
    def test_str(self):
        """Test for string representation."""
        company = ProbeFactory()
        self.assertEqual(str(company), company.name)

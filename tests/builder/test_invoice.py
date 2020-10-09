import unittest
from datetime import date

from design_patterns.builders.invoice_builder import InvoiceBuilder
from design_patterns.invoice.invoice import InvoiceItem


class test_invoice(unittest.TestCase):

    def test_invoicing(self):
        item = []
        item.extend([InvoiceItem('Item 1', 100)])
        item.extend([InvoiceItem('Item 2', 200)])
        item.extend([InvoiceItem('Item 3', 300)])

        data = {
            'company_name': 'Company for test',
            'document': '10794872000122',
            'items': item,
            'details': 'Details of Invoice',
            'date': date.today()
        }

        invoice = InvoiceBuilder()\
            .company_name(data['company_name'])\
            .document(data['document'])\
            .emission_date(data['date'])\
            .items(data['items']).\
            details(data['details']).build()

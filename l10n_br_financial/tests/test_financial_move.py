# -*- coding: utf-8 -*-
# Copyright 2017 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

class TestFinancialMove(TransactionCase):

    def setUp(self):
        super(TestFinancialMove, self).setUp()
        self.main_company = self.env.ref('base.main_company')
        self.currency_euro = self.env.ref('base.EUR')
        self.financial_move = self.env['financial.move']

    def test_1(self):
        """ DADO a data de vencimento de 27/02/2017
        QUANDO criado um lançamento de contas a receber
        ENTÃO a data de vencimento útil deve ser de 01/03/2017"""
        cr_1 = self.financial_move.create(dict(
            due_date='2017-02-27',
            company_id=self.main_company.id,
            currency_id=self.currency_euro.id,
            amount_document=100.00,
        ))
        self.assertEqual(cr_1.business_due_date, '2017-03-01')

    def test_2(self):
        """DADO uma conta a pagar ou receber
        QUANDO o valor for igual a zero
        ENTÃO apresentar uma mensagem solicitando preenchimento de valor
            maior que zero
        E impedir lançamento"""
        with self.assertRaises(ValidationError):
            cr_2 = self.financial_move.create(
                dict(due_date='2017-02-27',
                     company_id=self.main_company.id,
                     currency_id=self.currency_euro.id,
                     amount_document=0.00,
                     )
            )

            cr_3 = self.financial_move.create(
                dict(due_date='2017-02-27',
                     company_id=self.main_company.id,
                     currency_id=self.currency_euro.id,
                     amount_document=-10.00,
                     )
            )

    def test_3(self):
        """DADO que existe uma parcela de 100 reais em aberto
        QUANDO for recebido/pago 50 reais
        ENTÃO o valor do balanço da parcela deve ser 50 reais
        E o status da parcela deve permanecer em aberto."""
        cr_6 = self.create_receivable_100()
        cr_6.action_confirm()
        pay = self.financial_move.create(
            dict(
                move_type='rr',
                company_id=self.main_company.id,
                currency_id=self.currency_euro.id,
                amount_document=50.00,
                payment_id=cr_6.id
            )
        )
        pay.action_confirm()
        self.assertEqual(50.00, cr_6.balance)
        self.assertEqual('open', cr_6.state)

    def test_4(self):
        """DADO que existe uma parcela de 100 reais em aberto
        QUANDO for recebido/pago 100 reais
        ENTÃO o valor do balanço da parcela deve ser 0
        E o status da parcela deve mudar para pago."""
        cr_4 = self.create_receivable_100()
        cr_4.action_confirm()
        pay = self.financial_move.create(
            dict(
                move_type='rr',
                company_id=self.main_company.id,
                currency_id=self.currency_euro.id,
                amount_document=100.00,
                payment_id=cr_4.id
                )
            )
        pay.action_confirm()
        self.assertEqual(0.00, cr_4.balance)
        self.assertEqual('paid', cr_4.state)

    def test_5(self):
        """DADO que existe uma parcela de 100 reais em aberto
        QUANDO for recebido/pago 150 reais
        ENTÃO o valor do balanço da parcela deve ser 0
        E o status da parcela deve mudar para pago
        E o parceiro deve ficar com um crédito de 50 reais"""
        cr_5 = self.create_receivable_100()
        cr_5.action_confirm()
        pay = self.financial_move.create(
            dict(
                move_type='rr',
                company_id=self.main_company.id,
                currency_id=self.currency_euro.id,
                amount_document=150.00,
                payment_id=cr_5.id
                )
            )
        pay.action_confirm()
        self.assertEqual(0.00, cr_5.balance)
        self.assertEqual(50.00, cr_5.amount_residual)
        self.assertEqual('paid', cr_5.state)

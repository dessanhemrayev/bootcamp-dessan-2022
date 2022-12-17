from odoo.tests.common import Form, TransactionCase


class TestSaleOrderLine(TransactionCase):
    def setUp(self, *args, **kwargs):
        super(TestSaleOrderLine, self).setUp(*args, **kwargs)

        self.Users = self.env['res.users'].with_context(no_reset_password)

        self.customer_des = self.env["res.partner"].create({"name": "Dess"})
        self.product_mac = self.env["product.product"].create({"name": "macbook"})
        self.product_iphone = self.env["product.product"].create({"name": "iphone"})
        self.product_ipod = self.env["product.product"].create({"name": "ipod"})
        self.sale_order_1 = self.env["sale.order"].create(
            {"partner_id": self.customer_des.id}
        )

    def test_add_new_line(self):
        """Add new line to 50 and check the number"""

        # Add line #1
        with Form(self.sale_order_1) as f:
            with f.order_line.new() as line_1:
                line_1.product_id = self.product_mac
                line_1.sequence = 11
            f.save()

        with Form(self.sale_order_1) as f:
            with f.order_line.new() as line_2:
                line_2.product_id = self.product_iphone
                line_1.sequence = 12
            f.save()

        sale_order_line_1 = self.sale_order_1.order_line[0]
        sale_order_line_2 = self.sale_order_1.order_line[1]

        sale_order_line_2.sequence = 1
        sale_order_line_1.sequence = 2

        self.assertEqual(
            sale_order_line_2.line_number, 1, "Line number must be equal to 1"
        )
        self.assertEqual(
            sale_order_line_1.line_number, 2, "Line number must be equal to 2"
        )

    def test_add_many_lines(self):
        with Form(self.sale_order_1) as f:
            with f.order_line.new() as line_1:
                line_1.product_id = self.product_mac
                line_1.sequence = 11
            with f.order_line.new() as line_2:
                line_2.product_id = self.product_iphone
                line_1.sequence = 12
            f.save()
        sale_order_line_1 = self.sale_order_1.order_line[0]
        sale_order_line_2 = self.sale_order_1.order_line[1]

        sale_order_line_2.sequence = 1
        sale_order_line_1.sequence = 2
        self.assertEqual(
            sale_order_line_2.line_number, 1, "Line number must be equal to 1"
        )
        self.assertEqual(
            sale_order_line_1.line_number, 2, "Line number must be equal to 2"
        )

    def test_delete_lines(self):
        with Form(self.sale_order_1) as f:
            with f.order_line.new() as line_1:
                line_1.product_id = self.product_mac
                line_1.sequence = 11
            with f.order_line.new() as line_2:
                line_2.product_id = self.product_iphone
                line_2.sequence = 12
            with f.order_line.new() as line_3:
                line_3.product_id = self.product_ipod
                line_3.sequence = 12
            f.save()
        sale_order_line_1 = self.sale_order_1.order_line[0]
        sale_order_line_2 = self.sale_order_1.order_line[1]
        sale_order_line_3 = self.sale_order_1.order_line[2]

        sale_order_line_2.unlink()
        self.assertEqual(
            sale_order_line_1.line_number, 1, "Line number must be equal to 1"
        )
        self.assertEqual(
            sale_order_line_3.line_number, 2, "Line number must be equal to 2"
        )


acc_pay_ref = "ref"
invoice_origin = "invoice_origin"
report_invoices = "account.account_invoices"
posted_statuses = ['posted']

def order_create_invoices( sale_order, grouped=False, final=False ):
	sale_order._create_invoices(grouped=grouped, final=final)

def payment_post( self ):
    return self.action_post()

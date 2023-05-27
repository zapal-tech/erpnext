# Copyright (c) 2022, Frappe Technologies Pvt. Ltd. and Contributors
# See license.txt

# import frappe
from frappe.tests.utils import FrappeTestCase

from erpnext.stock.serial_batch_bundle import get_batch_nos, get_serial_nos


class TestSerialandBatchBundle(FrappeTestCase):
	def test_inward_serial_batch_bundle(self):
		pass

	def test_outward_serial_batch_bundle(self):
		pass

	def test_old_batch_valuation(self):
		pass

	def test_old_batch_batchwise_valuation(self):
		pass

	def test_old_serial_no_valuation(self):
		pass

	def test_batch_not_belong_to_serial_no(self):
		pass

	def test_serial_no_not_exists(self):
		pass

	def test_serial_no_item(self):
		pass

	def test_serial_no_not_required(self):
		pass

	def test_serial_no_required(self):
		pass

	def test_batch_no_not_required(self):
		pass

	def test_batch_no_required(self):
		pass


def get_batch_from_bundle(bundle):
	batches = get_batch_nos(bundle)

	return list(batches.keys())[0]


def get_serial_nos_from_bundle(bundle):
	serial_nos = get_serial_nos(bundle)
	return sorted(serial_nos) if serial_nos else []


def make_serial_batch_bundle(kwargs):
	from erpnext.stock.serial_batch_bundle import SerialBatchCreation

	type_of_transaction = "Inward" if kwargs.qty > 0 else "Outward"
	if kwargs.get("type_of_transaction"):
		type_of_transaction = kwargs.get("type_of_transaction")

	sb = SerialBatchCreation(
		{
			"item_code": kwargs.item_code,
			"warehouse": kwargs.warehouse,
			"voucher_type": kwargs.voucher_type,
			"voucher_no": kwargs.voucher_no,
			"posting_date": kwargs.posting_date,
			"posting_time": kwargs.posting_time,
			"qty": kwargs.qty,
			"avg_rate": kwargs.rate,
			"batches": kwargs.batches,
			"serial_nos": kwargs.serial_nos,
			"type_of_transaction": type_of_transaction,
			"company": kwargs.company or "_Test Company",
			"do_not_submit": kwargs.do_not_submit,
		}
	)

	if not kwargs.get("do_not_save"):
		return sb.make_serial_and_batch_bundle()

	return sb

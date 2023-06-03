# Copyright (c) 2023, Mohammed Nasser and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document

class StudentRegistration(Document):
	def before_insert(self):
		self.student_full_name = f'{self.student_fname} {self.student_lname or ""}'

	@frappe.whitelist()
	def create_student_user(self, throw_if_missing=False):
		doc = frappe.new_doc('User')
		doc.first_name = self.student_fname
		doc.last_name = self.student_lname
		doc.birth_date = self.student_bday
		doc.mobile_no = self.student_mobile
		doc.email =  self.student_mail
		doc.bio = self.name
		doc.insert()
		import time
		time.sleep(5)
		
		return 'User Created Successfully'
	
	


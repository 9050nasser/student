// Copyright (c) 2023, Mohammed Nasser and contributors
// For license information, please see license.txt

frappe.ui.form.on('Student Registration', {
	refresh: function(frm) {
		frm.add_custom_button('Create User',() =>{
			frm.call({
				doc: frm.doc,
				method: 'create_student_user',
				freeze: true,
				freeze_message: 'Create User',
				callback: function(r) {
					frappe.msgprint(r.message)
					frappe.msgprint("User Created Successfully")

				}
			})
		
	})

	 }
});

frappe.ready(function() {
	frappe.web_form.validate = function() {
	  var data = frappe.web_form.get_values();
	  var birthday = new Date(data.student_bday);
	  var minDate = new Date('2017-01-01');
  
	  if (birthday < minDate) {
		frappe.msgprint('السن اكبر من المسموح');
		return false;
	  }
  
	  return true;
	};
  });
  
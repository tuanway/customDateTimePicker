/**
 * @type {String}
 *
 * @properties={typeid:35,uuid:"5D7C3951-6917-47F1-8DE4-89912E3FD4B9"}
 */
var time = null;

/**
 * @type {String}
 *
 * @properties={typeid:35,uuid:"9B46F492-9297-4702-A597-1185CF5B7C01"}
 */
var date = null;


/**
 * @param oldValue
 * @param newValue
 * @param {JSEvent} event
 *
 * @return {boolean}
 *
 * @private
 *
 * @properties={typeid:24,uuid:"92EE58FA-CEBF-44E7-8F4D-2E31E9BE4BCA"}
 */
function onDataChangeMethodID(oldValue, newValue, event) {
	application.output('date: ' + date + ', time: ' + time)
	return false;
}

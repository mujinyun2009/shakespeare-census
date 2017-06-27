function showAddAnotherPopup(triggeringLink) {
	var href = triggeringLink.href
	var name = triggeringLink.name
	var win = window.open(href, name, "height=500,width=800,resizable=yes,scrollbars=yes");
	win.focus();
	return false;
}

function dismissAddAnotherPopup(win, newId, newRepr) {
    // newId and newRepr are expected to have previously been escaped by
    // django.utils.html.escape.
    newId = html_unescape(newId);
    newRepr = html_unescape(newRepr);
    var name = windowname_to_id(win.name);
    var elem = document.getElementById(name);
    if (elem) {
        if (elem.nodeName == 'SELECT') {
            var o = new Option(newRepr, newId);
            elem.options[elem.options.length] = o;
            o.selected = true;
        }
    }
    win.close();
}

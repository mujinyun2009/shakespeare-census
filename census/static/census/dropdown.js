jQuery(function($) {
$(document).ready(function() {
  var title_select=document.getElementById('id_title');

  title_select.onchange = function(){
    if ($(this).val() == '') {
        $('.edition_section').attr('style', 'display:none');
      }
    else {
      var edition_section=document.getElementById('edition_section');
      edition_section.style.display="inline";
      var title = $(this).val();
      var new_url = "/census/addEdition/" + $(this).val() + "/";
      $('#add_edition').attr('href', new_url);
    }
  };

  var edition_select=document.getElementById('id_edition');
  edition_select.onchange=function() {
    if ($(this).val() == '') {
        $('.issue_section').attr('style', 'display:none');
      }
    else {
        var issue_section=document.getElementById('issue_section');
        issue_section.style.display="inline";
        var edition = $(this).val();
        var new_url = "/census/addIssue/" + $(this).val() + "/";
        $('#add_issue').attr('href', new_url);
      }
  };

  var issue_select=document.getElementById('id_issue');
	issue_select.onchange=function() {
		if ($(this).val() == '') {
			$('.copy_section').attr('style', 'display:none');
		}
		else {
      var copy_section=document.getElementById('copy_section');
      copy_section.style.display="inline";
			$('.copy_submit').attr('style', 'display:inline');
		}
	};
});
});

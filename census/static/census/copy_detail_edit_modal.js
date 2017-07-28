jQuery(function($) {
$(document).ready(function() {
  $(".copy_data").unbind('click');
  $(".copy_data").click(function(ev) {
    ev.preventDefault();
    var url=$(this).data("form");
    $("#copyModal").load(url, function() {
      $("#copyModal").modal('show');
    });
    return false;
  });

  $(".update_copy").unbind('click');

  $(".update_copy").click(function(ev) {
    ev.preventDefault();
    var url=$(this).data("form");
    $("#editModal").load(url, function() {
      $("#editModal").modal('show');
    });
    return false;
  });
});
});

function generateDialog(copy_id) {
  $.ajax({
    url: $('.editForm').attr('action'),
    type: "POST",
    datatype: "json",
    data: $('.editForm').serialize(),
    success: function(data) {
      if(data['stat'] === "ok") {
        alert('Success! Your changes have been saved.');
        $("#editModal").modal('hide');
      } else {
        alert("Error: invalid input! Please correct the errors in your input and submit again!");
        $("#editModal").html(data['form']);
        if(data['stat']==='title error') {
          var option = $('#title').val('Z');
      		option.selected = true;
      		var editions = document.getElementById('edition');
      		editions.options.length = 0;
      		var issues = document.getElementById('issue');
      		issues.options.length = 0;
          var add_edition=document.getElementById('add_edition');
          add_edition.classList.add('hidden');
          var add_issue=document.getElementById('add_issue');
          add_issue.classList.add('hidden');

        } else if (data['stat'] ==='edition error') {
          var option = $('#edition').val('Z');
          option.selected = true;
          var issues = document.getElementById('issue');
      		issues.options.length = 0;
          $('#add_issue').attr('href', "#");
        } else if (data['stat'] === 'issue error') {
          var option = $('#issue').val('Z');
          option.selected = true;
        }
        $("#editModal").modal('show');
      }
      }
    });
  return false;
}

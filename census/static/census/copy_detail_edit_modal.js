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
        alert(data['stat']);
        $("#editModal").modal('show');
      }
      }
    });
  return false;
}

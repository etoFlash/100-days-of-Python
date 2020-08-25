function delete_task(obj) {
    var id_task = $(obj).parent().parent().attr("id");

    $.ajax({
      type: "POST",
      url: "/delete/" + id_task,
      success: $("tr#" + id_task).remove()
    });
}

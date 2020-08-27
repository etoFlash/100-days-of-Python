function delete_task(obj) {
    var id_task = $(obj).parent().parent().attr("id");

    $.ajax({
      type: "POST",
      url: "/delete/" + id_task,
      success: $("tr#" + id_task).remove()
    });
}

function move_task(obj, direction) {
    var id_task = $(obj).parent().parent().attr("id");

    $.post("/move/" + id_task + "/" + direction, function(data) {
      $("#tableTasks").html(data);
    });
}

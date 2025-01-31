$(document).ready(function() {
    $('.task-detail-link').on('click', function() {
        var taskId = $(this).data('task-id');
        var taskName = $(this).data('task-name');
        var taskDetails = $(this).data('task-details');
        var taskDate = $(this).data('task-date');
        var taskPriority = $(this).data('task-priority');

        $('#modal-task-name').text(taskName);
        $('#modal-task-details').text(taskDetails);
        $('#modal-task-date').text(taskDate);
        $('#modal-task-priority').text(taskPriority);

        $('#delete-task-btn').data('task-id', taskId);
    });

    $('#delete-task-btn').on('click', function() {
        var taskId = $(this).data('task-id');

        if (taskId) {
            $.ajax({
                url: '/taskapp/delete_task/' + taskId + '/',
                type: 'POST',
                data: {
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
                },
                success: function(response) {
                    $('#task-list').find('[data-task-id="'+ taskId +'"]').closest('.task-row').remove();
                    $('#taskDetailModal').modal('hide');
                },
                error: function(xhr, errmsg, err) {
                    console.error('削除に失敗しました: ' + errmsg);
                }
            });
        } else {
            console.error('taskId が取得できませんでした');
        }
    });
});

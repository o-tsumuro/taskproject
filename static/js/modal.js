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
    });
});

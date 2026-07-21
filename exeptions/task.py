from exeptions.base import AppException


class TaskNotFoundError(AppException):
    status_code = 404
    detail = "Task not found"


class InvalidTaskTitleError(AppException):
    status_code = 400
    detail = "Title must contain at least 3 characters"


class TaskAlreadyExistsError(AppException):
    status_code = 409
    detail = "Task already exists"


class InvalidTaskIdError(AppException):
    status_code = 400
    detail = "Task id must be greater than zero"


class InvalidPriorityError(AppException):
    status_code = 400
    detail = "Invalid priority"


class TaskUpdateError(AppException):
    status_code = 400
    detail = "Task update failed"


class TaskDeleteError(AppException):
    status_code = 400
    detail = "Task delete failed"
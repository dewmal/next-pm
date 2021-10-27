from datetime import datetime

from project_detail.models import Task


class ProjectService:

    @staticmethod
    def close_task(task: Task):
        steps = task.step_set.all()
        actual_hours = 0
        for step in steps:
            start_time: datetime = step.start_time
            end_time: datetime = step.end_time
            diff = end_time - start_time
            actual_hours += diff.seconds
        task.actual_hours = (actual_hours / 60)/60
        task.save()
        return task

from celery import shared_task

@shared_task
def add():
    return (2000 * 20)

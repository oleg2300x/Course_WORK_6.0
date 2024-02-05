import logging
from django.conf import settings
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from mailing.utils import send_ready_mailings

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    При запуске этот робот проверяет список рассылки каждые 10 секунд и отправляет все готовое к отправке и с соответствующим временем.
    """

    def handle(self, *args, **options):
        print('apscheduler work')
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            send_ready_mailings,
            trigger=CronTrigger(second="*/10"),
            id="send_ready_mailings",
            max_instances=1,
            replace_existing=True,
        )

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")

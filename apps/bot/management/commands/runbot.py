from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Run python3 main.py'

    def handle(self, *args, **options):
        from aiogram import executor
        from apps.bot.handlers import dp

        executor.Executor(dp, skip_updates=True).start_polling()

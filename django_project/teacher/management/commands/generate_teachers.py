from django.core.management.base import BaseCommand
from faker import Faker

from teacher.models import Teacher

fake = Faker()


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "number", default=100, nargs="?", help="Number of teachers to generate"
        )

    def handle(self, *args, **options):
        for i in range(int(options["number"])):
            t = Teacher(
                name=fake.first_name(),
                surname=fake.last_name(),
                birth_data=fake.date(),
                subject=fake.random_element(
                    elements=(
                        "Mathematics",
                        "Literature",
                        "History",
                        "Physics",
                        "Biology",
                    )
                ),
            )
            t.save()
            self.stdout.write(
                self.style.SUCCESS('Successfully added teacher "%s"' % t.name)
            )

from django.db.models import QuerySet

from db.models import CinemaHall


def get_cinema_halls() -> QuerySet[CinemaHall]:
    return CinemaHall.objects.all()


def create_cinema_hall(hall_name: str,
                       hall_raws: int,
                       hall_seats_in_row: int) -> CinemaHall:
    return CinemaHall.objects.create(
        name=hall_name,
        rows=hall_raws,
        seats_in_row=hall_seats_in_row
    )
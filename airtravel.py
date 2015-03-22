"""Model for aircraft flights"""
from utils import *


class Flight:
    """"A flight with a particular passenger aircraft."""
    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError("No airline code in {}".format(number))

        if not number[:2].isupper():
            raise ValueError("Invalid airline code '{}'".format(number))

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("Invalid route number '{}'".format(number))

        self._number = number
        self._aircraft = aircraft

        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [ {letter:None for letter in seats} for _ in rows ]

    def number(self):
        return self._number

    def airline(self):
        return self._number[2:]

    def aircraft_model(self):
        return self._aircraft.model()

    def _parse_seat(self, seat):
        """Parse a seat designator into a valid row and letter.

        Args:
            seat: A seat designator such as '12F'

        Returns:
            A tuple containing an integer and and a string for row and seat.
        """
        rows, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {}".format(letter))

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid seat row {}".format(row_text))

        if row not in rows:
            raise ValueError("Invalid row number {}".format(row))

        return row, letter

    def allocate_seat(self, seat, passenger):
        """Allocate a seat to a passenger.

        Args:
            seat: A seat designator such as '12c' or '21F'.
            passenger: The passenger name.

        Raises:
            ValueError: If the seat is unavailable
        """
        row, letter = self._parse_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} already occupied".format(seat))

        self._seating[row][letter] = passenger

    def relocate_passenger(self, from_seat, to_seat):
        """Relocate a passenger to a different seat.
        :param from_seat: The existing seat designator for the passenger to be moved.
        :param to_seat: The new seat to be moved.
        """
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError("No passenger to relocate in seat {}".format(from_seat))

        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError("Seat {} already occupied".format(to_seat))

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    def num_available_seats(self):
        return sum(sum(1 for s in row.values() if s is None)
                   for row in self._seating
                   if row is not None)

    def _passenger_seats(self):
        """An iterable series of passenger seating allocations."""
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield (passenger, "{}{}".format(row,letter))

    def make_boarding_cards(self, card_printer):
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self.number(), self.aircraft_model())


'''
class Aircraft:

    def __init__(self, registration, model, num_rows, num_sets_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_sets_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return range(1, self._num_rows+1), "ABCDEFGHJK"[:self._num_seats_per_row]
'''


class Aircraft:
    def __init__(self, registration):
        self._registration = registration

    def registration(self):
        return self._registration

    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)


class AirbusA319(Aircraft):
    def model(self):
        return "Airbus A319"

    def seating_plan(self):
        return range(1, 23), "ABCDEF"


class Boeing777(Aircraft):
    def model(self):
        return "Boeing 777"

    def seating_plan(self):
        return range(1, 59), "ABCDEFGHJK"


def make_flight():
    # f = Flight("BA758", Aircraft("G-EUPT", "Airbus A139", num_rows=22, num_sets_per_row=6))
    f = Flight("BA758", AirbusA319("G-EUPT"))
    f.allocate_seat('12A', 'Guido van Rossum')
    f.allocate_seat('15F', 'Bjarne Stroustrup')
    f.allocate_seat('15E', 'Anders Hejlsberg')
    f.allocate_seat('1C', 'John McCarthy')
    f.allocate_seat('1D', 'Richard Hickey')
    return f


def console_card_printer(passenger, seat, flight_number, aircraft):
    output= "| Name: {0}"       \
            " Flight: {1}"      \
            " Seat: {2}"        \
            " Aircraft: {3}"    \
            " |".format(passenger, seat, flight_number, aircraft)
    banner = '+' + '-' * (len(output) - 2) + '+'
    border = '|' + ' ' * (len(output) - 2) + '|'
    lines = [banner, border, output, border, banner]
    card = "\n".join(lines)
    print(card)
    print()


if __name__ == '__main__':
    f = make_flight()

    hrule("Flight number using different methods")
    print(f.number())
    print(Flight.number(f))
    print(f._number)

    hrule("Other Flight info")
    print("Airline code is {}".format(f.airline()))
    print("Aircraft model is {}".format(f.aircraft_model()))
    print("Number of available seats : {}".format(f.num_available_seats()))

    f.relocate_passenger('12A', '15D')

    hrule("Current seating for flight : ")
    pp(f._seating)

    hrule("Print boarding passes")
    f.make_boarding_cards(console_card_printer)

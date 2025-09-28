"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    
    seat_letters = ['A', 'B', 'C', 'D']

    for seat in range(number):
        index = seat % 4
        yield seat_letters[index]

def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """

    # get seat letter generator
    seat_letter_generator = generate_seat_letters(number)

    for seat in range(number):
        row_number = seat // 4
        if row_number >= 12: # 12 corresponds to row 13
            row_number = row_number + 1
        yield "".join([str(row_number + 1), seat_letter_generator.__next__()])


def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    result = {}

    seats = len(passengers)

    seats_generator = generate_seats(seats)

    for passenger in passengers:
        result[passenger] = seats_generator.__next__()
    
    return result

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    for seat in seat_numbers:
        result = "".join([seat, flight_id])
        # pad the result with 0's and send this back
        result = result.ljust(12, "0")
        yield result

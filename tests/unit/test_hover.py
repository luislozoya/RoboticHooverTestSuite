import pytest
from pytest_bdd import scenarios, given, when, then

scenarios("cleaning_service.feature")


@given("the room dimensions are '5,5'")
def room_size():
    return 5, 5


@given("the hoover is initially at '1,2'")
def hoover():
    return 1, 1

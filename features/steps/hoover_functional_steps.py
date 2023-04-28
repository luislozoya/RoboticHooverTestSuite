import allure
import requests
from behave import given, when, then, fixture, use_fixture
from requests import post

from src import payload_manager, requests_manager


@given('a room with dimensions "{room_x}" by "{room_y}"')
def step_impl_given_room_dimensions(context, room_x, room_y):
    context.room_x = int(room_x)
    context.room_y = int(room_y)


@given('a hoover starting at position "{start_x}", "{start_y}"')
def step_impl_given_hoover_position(context, start_x, start_y):
    context.start_x = int(start_x)
    context.start_y = int(start_y)


@given('the following patches of dirt: "{dirt_positions}"')
def step_impl_given_dirt_patches(context, dirt_positions):
    context.dirt_positions = payload_manager.get_dirt_list(dirt_positions)


@when('the hoover moves according to "{instructions}"')
def step_impl_when_hoover_moves(context, instructions):
    context.payload = payload_manager.generate_instructions_payload(context, instructions)
    response = requests_manager.get_response(context)
    context.response_status_code = response.status_code
    context.response_body = response.json()


@then('the final position of the hoover should be "{final_x}", "{final_y}"')
def step_impl_then_hoover_position(context, final_x, final_y):
    assert context.response_status_code == 200, f"Expected {int(200)} but got {context.response_status_code}"
    assert context.response_body["coords"] == [int(final_x), int(final_y)], f"Expected {[int(final_x), int(final_y)]} but got {context.response_body['coords']}"


@then('the number of cleaned patches should be "{cleaned_patches}"')
def step_impl_then_hoover_position(context, cleaned_patches):
    assert context.response_body["patches"] == int(cleaned_patches), f"Expected {int(cleaned_patches)} but got {context.response_body['patches']}"



from behave import given, when, then
from src import payload_manager, requests_manager


@given('a request with wrong parameters "{room_x}" "{room_y}" "{start_x}" "{start_y}" "{dirt_positions}" "{instructions}"')
def a_request_with_wrong_parameters(context, room_x, room_y, start_x, start_y, dirt_positions, instructions):
    payload = payload_manager.generate_payload(context, room_x, room_y, start_x, start_y, dirt_positions, instructions)
    context.payload = payload


@when('I send a request with wrong parameters')
def step_impl_when_i_send_a_request_with_wrong_parameters(context):
    context.response_status_code = requests_manager.get_status_code(context)


@then('the service should return a bad request error')
def step_impl_then_service_should_return_bad_request_error(context):
    assert context.response_status_code == 400, f"Expected 400 but got {context.response_status_code}"


@given('a request with missing payload information "{room_x}" "{room_y}" "{start_x}" "{start_y}" "{instructions}"')
def step_impl_then_service_should_return_an_error(context, room_x, room_y, start_x, start_y, instructions):
    context.payload = payload_manager.generate_incomplete_payload(room_x, room_y, start_x, start_y, instructions)


@when('I send a request with missing payload information')
def step_impl_when_missing_input(context):
    context.response = requests_manager.get_response(context)
    context.response_status_code = requests_manager.get_status_code(context)


@then('the service should return a missing input error')
def step_impl_then_service_should_return_missing_input_error(context):
    response = context.response
    assert response.status_code == 400, f"Expected status code 400 but got {response.status_code}"
    if hasattr(response, "json()"):
        assert response.json() == {"message": "Missing input parameter"}, \
            f"Expected error message 'Missing input parameter' but got {response.json()['message']}"
    else:
        assert False, f"Expected error message 'Missing input parameter'"



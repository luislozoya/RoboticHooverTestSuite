from behave import fixture, use_fixture

from data_provider import config_reader


@fixture
def set_url(context):
    context.url = config_reader.get_url()
    yield context.url


def before_scenario(context, scenario):
    use_fixture(set_url, context)


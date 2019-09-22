import pytest

from stage_3.project import count


@pytest.mark.parametrize('water,milk,beans,cups,message', [
    (300, 65, 100, 1, 'Yes, I can make that amount of coffee'),
    (500, 250, 200, 10, 'No, I can make only 2 cups of coffee'),
    (1550, 299, 300, 3, 'Yes, I can make that amount of coffee'
                        ' (and even 2 more than that)'),
    (0, 0, 0, 1, 'No, I can make only 0 cups of coffee'),
    (0, 0, 0, 0, 'Yes, I can make that amount of coffee'),
    (200, 50, 15, 0, 'Yes, I can make that amount of coffee'
                     ' (and even 1 more than that)'),
])
def test_count(water, milk, beans, cups, message):
    assert count(water, milk, beans, cups) == message

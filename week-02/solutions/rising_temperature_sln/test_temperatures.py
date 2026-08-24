from solution import dailyTemperatures


def test_temperatures():
    assert dailyTemperatures(
        [73, 74, 75, 71, 69, 72, 76, 73]
    ) == [1, 1, 4, 2, 1, 1, 0, 0]

    assert dailyTemperatures(
        [30, 40, 50, 60]
    ) == [1, 1, 1, 0]

    assert dailyTemperatures(
        [30, 60, 90]
    ) == [1, 1, 0]


def test_no_warmer_temperature():
    assert dailyTemperatures([90, 80, 70, 60]) == [0, 0, 0, 0]


def test_single_temperature():
    assert dailyTemperatures([50]) == [0]


def test_same_temperatures():
    assert dailyTemperatures([70, 70, 70]) == [0, 0, 0]
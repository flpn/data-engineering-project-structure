from transformations import clean_data


def test_should_upper_case_names():
    columns = ['age', 'sex']
    
    actual = clean_data.upper_case_names(columns)
    expected = ['AGE', 'SEX']

    assert actual == expected


def test_should_remove_whitespaces_from_names():
    columns = ['FIRST NAME']

    actual = clean_data.remove_whitespaces_from_names(columns)
    expected = ['FIRST_NAME']

    assert actual == expected


def test_should_clean_names():
    columns = ['age', 'LAST NAME']

    actual = clean_data.clean_names(columns)
    expected = ['AGE', 'LAST_NAME']

    assert actual == expected

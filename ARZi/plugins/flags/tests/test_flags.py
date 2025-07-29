from ARZi.plugins.flags import ARZiRegexFlag


def test_valid_regex_match_case_sensitive():
    """
    Test a valid regex match in a case-sensitive manner using ARZiRegexFlag
    """
    flag = ARZiRegexFlag()
    flag.content = r"^[A-Z]\d{3}$"
    flag.data = "case_sensitive"
    provided_flag = "A123"
    assert flag.compare(flag, provided_flag)  # nosec


def test_valid_regex_match_case_insensitive():
    """
    Test a valid regex match in a case-insensitive manner using ARZiRegexFlag
    """
    flag = ARZiRegexFlag()
    flag.content = r"^[a-z]\d{3}$"
    flag.data = "case_insensitive"
    provided_flag = "A123"
    assert flag.compare(flag, provided_flag)  # nosec


def test_invalid_regex_match():
    """
    Test an invalid regex match using ARZiRegexFlag
    """
    flag = ARZiRegexFlag()
    flag.content = r"^[A-Z]\d{3}$"
    flag.data = "case_sensitive"
    provided_flag = "invalid"
    assert not flag.compare(flag, provided_flag)  # nosec

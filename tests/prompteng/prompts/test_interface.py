from prompteng.prompts.interface import _validate_alias 

def test_validate_alias():
    assert _validate_alias("development") is True
    assert _validate_alias("staging") is True
    assert _validate_alias("production") is True
    assert _validate_alias("invalid") is False

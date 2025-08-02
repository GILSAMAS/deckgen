from deckgen.utils.files import read_template



def test_read_template():
    """
    Test reading template files.
    This function checks if the content of the template files matches the expected content.
    It reads the templates from the 'configs/templates' directory using the `read_template` function
    and compares the content with the expected content that is read directly from the files.
    """
    template_names = [
        "question_asking",
        "question_groundeness_critique_prompt",
        "topic_finder"
    ]
    template_contents = {}
    for template_name in template_names:
        with open(f"deckgen/configs/templates/{template_name}.txt", "r") as f:
            expected_content = f.read()
            template_contents[template_name] = expected_content

    for template_name, expected_content in template_contents.items():
        actual_content = read_template(template_name)
        assert actual_content == expected_content
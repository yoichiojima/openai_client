from openai_client.lib import roles


def test_role():
    r = roles.Role()
    return r.get_role("not_exist")

test_role()

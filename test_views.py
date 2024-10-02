import pytest
from django.urls import reverse
from model_bakery import baker


@pytest.mark.django_db
def test_kuhl_user_permissions_list(api_client):
    permission = baker.make("auth.Permission")

    user = baker.make("users.KuhlUser")

    user.user_permissions.set([permission])

    url = reverse("users:permissions-list", kwargs={"pk": user.pk})

    resp = api_client.get(url, format="json")

    assert resp.status_code == 200
    assert len(resp.data["permissions"]) == 1


@pytest.mark.django_db
def test_kuhl_user_permissions_list_no_user(api_client):
    url = reverse("users:permissions-list", kwargs={"pk": 24})

    # with pytest.raises(Http404):
    resp = api_client.get(url, format="json")

    assert resp.status_code == 404

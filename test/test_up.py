from helpers import qualified_url

def test_login(client):
    resp = client.get(qualified_url(''))
    login_links = [ l for l in resp.html.find('a') if l.text == 'Sign In with CAC' ]
    login_resp = client.get(
            login_links[0].attrs['href'],
            cert=(
                "services/authnid/ssl/client-certs/atat.mil.crt",
                "services/authnid/ssl/client-certs/atat.mil.key",
            ),
            verify=False
        )
    assert login_resp.url == 'http://localhost:8000/home'


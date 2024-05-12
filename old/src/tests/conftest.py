@pytest.fixture(scope="session")
def client():
    return AsyncIOMotorClient("mongodb://elsweb:Klneodeon27@elsweb.servehttp.com:27017")

    
import pytest
from app import create_app, db
from app.models import Campaign

@pytest.fixture
def test_client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()

def test_sync_route(test_client):
    response = test_client.post('/sync')
    assert response.status_code == 200
    assert response.json['message'] == 'Campaigns synced'

def test_report_route(test_client):
    test_client.post('/sync')
    response = test_client.get('/report')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 2
    assert all('ctr' in item for item in data)

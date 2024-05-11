import json


def test_main(app, client):
	response = client.get('/')
	assert response.status_code == 200

	data_expectations = "ok"
	assert data_expectations in response.get_data(as_text=True)


def test_games_page(app, client):
	response = client.get('/api/v1/games')
	assert response.status_code == 200

	data_expectations = {'g1': 100, 'g2': 200, 'g3': 300, 'g4': 400}
	# manual query <--> response data
	assert data_expectations == json.loads(response.get_data())

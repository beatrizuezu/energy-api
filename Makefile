clean:
	@find . -iname '*.pyc' -delete
	@find . -iname '*.pyo' -delete
	@find . -iname '*~' -delete
	@find . -iname '*.swp' -delete
	@find . -iname '__pycache__' -delete

setup:
	rye sync


run:
	python manage.py runserver

makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate


loaddata:
	python manage.py loaddata measurement_devices.json
	python manage.py loaddata measurements.json


compose:
	docker-compose up

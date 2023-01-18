install:
	sudo apt-get install docker
	sudo apt-get install python3
	pip install docker-compose

buildAndRun:
	chmod +x ./run_compose.sh
	./run_compose.sh up --build

run:
	./run_compose.sh up

	
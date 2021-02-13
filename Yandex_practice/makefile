HOST=192.168.1.101
TEST_PATH=./

clean-pyc:
    find . -name '*.pyc' -exec rm --force {} +
    find . -name '*.pyo' -exec rm --force {} +
   name '*~' -exec rm --force  {}

clean-build:
    rm --force --recursive build/
    rm --force --recursive dist/
    rm --force --recursive *.egg-info

isort:
    sh -c "isort --skip-glob=.tox --recursive . "

lint:
    flake8 --exclude=.tox

test: clean-pyc
    py.test --verbose --color=yes $(TEST_PATH)

docker-run:
    docker build \
      --file=./Dockerfile \
      --tag=Yandex_practice ./
    docker run \
      --detach=false \
      --name=Yandex_practice \
      --publish=$(HOST):8080 \
      Yandex_practice
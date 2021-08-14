# rip
docker image build --file Dockerfile.dev -t rip:latest .
docker container run -v $PWD/rip:/app --rm -it -p 8000:8000 --name rip rip:latest

docker image build --file Dockerfile.prod -t rip-prod:latest .

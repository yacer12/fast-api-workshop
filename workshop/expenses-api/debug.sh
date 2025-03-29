echo "Starting to build Docker Image"
docker build -t expenses_api .
echo "Finishing Docker Image Build"

echo "Starting to run Docker Container"

docker run --env-file .env \
    -it --rm --name expenses_api \
    -v $(pwd):/code/ \
    -p 9000:9000 expenses_api
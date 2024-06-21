# sboot_docker_user

docker build -t shop_api_user .

docker run --name shop_api_user --rm -v $(pwd)/results_user:/tool/results shop_api_user

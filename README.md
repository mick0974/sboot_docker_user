# sboot_docker_user

sudo docker build -t shop_api_user .

sudo docker run -p 8080:8080 --name shop_api_user --rm -v $(pwd)/results_user:/tool/results shop_api_user

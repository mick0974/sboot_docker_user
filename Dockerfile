FROM ubuntu:22.04

ENV API=shop_api
ENV DEBIAN_FRONTEND=noninteractive

RUN mkdir /api
RUN mkdir /tool

COPY api/ /api/
COPY tool/ /tool/

RUN apt update && \
    apt -y upgrade && \
    apt -y install openjdk-11-jdk mysql-server mitmproxy python3-requests && \
    usermod -d /var/lib/mysql/ mysql && \
    /etc/init.d/mysql start && \
    mysql -e "CREATE DATABASE sboot_shop_api" && \
    mysql -e "CREATE USER michele@localhost IDENTIFIED BY 'mick0974'" && \
    mysql -e "GRANT ALL PRIVILEGES ON sboot_shop_api.* TO michele@localhost" && \
    apt -y autoremove

CMD bash -c "ls && service mysql start && \ 
java -jar /api/shop-api-0.0.1-SNAPSHOT.jar seeds & \ 
sleep 30 && \
cd tool && \
java -jar resttestgen-framework-23.09-all.jar -l DEBUG -a SBootApiEcomMVCHibernate_USER -s OperationSemanticsInferenceStrategy"

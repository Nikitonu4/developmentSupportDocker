# базовый образ jenkins
FROM jenkins/jenkins:2.289.1-lts-jdk11

# заходим под пользователем ROOT(только он может устанавливать плагины)
USER root

EXPOSE 8080 50000

RUN apt-get update

USER jenkins
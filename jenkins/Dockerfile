FROM jenkins/jenkins:2.289.1-lts-jdk11

COPY plugins.txt /usr/share/jenkins/plugins.txt
# запускаем скрипт установки плагинов и скармливаем ему наш файл с плагинами
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/plugins.txt

USER root
RUN apt-get update && apt-get install -y unzip
WORKDIR /gradle
RUN curl -L https://services.gradle.org/distributions/gradle-7.1-bin.zip -o gradle-7.1-bin.zip
RUN unzip gradle-7.1-bin.zip
ENV GRADLE_HOME=/gradle/gradle-7.1
ENV PATH=$PATH:$GRADLE_HOME/bin
USER jenkins
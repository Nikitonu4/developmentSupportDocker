FROM jenkins/jenkins:2.289.1-lts-jdk11

COPY plugins.txt /usr/share/jenkins/plugins.txt
# запускаем скрипт установки плагинов и скармливаем ему наш файл с плагинами
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/plugins.txt

USER jenkins
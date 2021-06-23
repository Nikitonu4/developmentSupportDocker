# базовый образ основан на jenkins(jdk11)
FROM jenkins/jenkins:2.289.1-lts-jdk11

# копируем файл с необходимыми плагинами в контейнер
COPY plugins.txt /usr/share/jenkins/plugins.txt

# запускаем скрипт установки плагинов и скармливаем ему наш файл с плагинами
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/plugins.txt

# ДАЛЬШЕ ОПИСАНЫ ШАГИ ПО УСТАНОВКЕ gradle ДЛЯ ТЕСТА ИНТЕГРАЦИИ

# переключаемся на пользователя root 
USER root

# обновляем пакеты и устанавливаем пакет unzip
RUN apt-get update && apt-get install -y unzip

# задаем рабочую директорию как /gradle 
WORKDIR /gradle

# скачиваем gradle 
RUN curl -L https://services.gradle.org/distributions/gradle-7.1-bin.zip -o gradle-7.1-bin.zip

# распаковываем
RUN unzip gradle-7.1-bin.zip

# задаем переменные окружения 
ENV GRADLE_HOME=/gradle/gradle-7.1
ENV PATH=$PATH:$GRADLE_HOME/bin

# переключаемся обратно на jenkins пользователя
USER jenkins
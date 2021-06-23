
# СТАДИЯ СБОРКИ
# базируется на golang
FROM golang:1.16-alpine3.13 AS build-env

# задаем аргументы и переменные окружения
ARG GOPROXY
ENV GOPROXY ${GOPROXY:-direct}
ARG GITEA_VERSION
ARG TAGS="sqlite sqlite_unlock_notify"
ENV TAGS "bindata timetzdata $TAGS"
ARG CGO_EXTRA_CFLAGS

# устанавливаем инструменты и зависимости
RUN apk --no-cache add build-base git nodejs npm

# настраиваем окружения для сборки
COPY . ${GOPATH}/src/code.gitea.io/gitea
WORKDIR ${GOPATH}/src/code.gitea.io/gitea

# проверяем версию
RUN if [ -n "${GITEA_VERSION}" ]; then git checkout "${GITEA_VERSION}"; fi \
 && make clean-all build

# собираем приложение
RUN go build contrib/environment-to-ini/environment-to-ini.go

# базовый образ alpine 
FROM alpine:3.13

# указываем на необходимость открыть порты 22 и 30000
EXPOSE 22 3000

# устанавливаем необходимые инструменты и зависимости
RUN apk --no-cache add \
    bash \
    ca-certificates \
    curl \
    gettext \
    git \
    linux-pam \
    openssh \
    s6 \
    sqlite \
    su-exec \
    gnupg

# добавляем группу и юзера 
RUN addgroup \
    -S -g 1000 \
    git && \
  adduser \
    -S -H -D \
    -h /data/git \
    -s /bin/bash \
    -u 1000 \
    -G git \
    git && \
  echo "git:*" | chpasswd -e

# задаем переменные окружения
ENV USER git
ENV GITEA_CUSTOM /data/gitea

# создаем точку монтирования для постоянного хранилища
VOLUME ["/data"]

# задаем входную точку
# устаналиваем команду, которая будет запущена при запуске контейнера
ENTRYPOINT ["/usr/bin/entrypoint"]
CMD ["/bin/s6-svscan", "/etc/s6"]

# копируем необходимые файлы в корень контейнера
COPY docker/root /
COPY --from=build-env /go/src/code.gitea.io/gitea/gitea /app/gitea/gitea
COPY --from=build-env /go/src/code.gitea.io/gitea/environment-to-ini /usr/local/bin/environment-to-ini

# создаем символическую ссылку
RUN ln -s /app/gitea/gitea /usr/local/bin/gitea

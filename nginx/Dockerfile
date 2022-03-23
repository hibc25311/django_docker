FROM nginx:latest
LABEL maintainer="awei"


COPY nginx.conf /etc/nginx/nginx.conf
COPY docker-nginx-django_practice_01.conf /etc/nginx/sites-available/

RUN mkdir -p /etc/nginx/sites-enabled/ && \
    ln -s /etc/nginx/sites-available/docker-nginx-django_practice_01.conf /etc/nginx/sites-enabled/

CMD ["nginx", "-g", "daemon off;"]
FROM python:3.8.10

RUN apt-get update
RUN apt-get install -y unixodbc-dev
RUN useradd -m django
COPY ./ /home/django
RUN pip install -r /home/django/requirements.txt
RUN python 
COPY ./entrypoint.sh /entrypoint.sh
RUN chown django:django -R /home/django
RUN chmod uog+x /entrypoint.sh && ln -s /entrypoint.sh /usr/bin/manage
USER django
WORKDIR /home/django
EXPOSE 8000
ENTRYPOINT ["/entrypoint.sh"]
CMD ["runserver"]

FROM python:3.11

WORKDIR /app

COPY requirements.txt app/requirements.txt

RUN pip install -r app/requirements.txt


RUN useradd -m -u 1000 testuser1
USER testuser1

ENV HOME=/home/testuser1 \
	PATH=/home/testuser1/.local/bin:$PATH


WORKDIR $HOME


COPY --chown=testuser1 . $HOME

COPY --chown=testuser1 sentiment-analysis.py $HOME/sentiment-analysis.py

RUN chown -R testuser1 $HOME
RUN chmod 777 -R $HOME
ENTRYPOINT ["python3", "sentiment-analysis.py"]





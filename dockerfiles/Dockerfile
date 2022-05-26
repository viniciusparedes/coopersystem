ARG PYTHON_IMAGE=python
FROM python:3.8.3 as python-stage

# Set PYTHONUNBUFFERED so output is displayed in the Docker log
ENV PYTHONUNBUFFERED=1

# Instala dependências pelo poetry
COPY ./pyproject.toml /app/
WORKDIR /app

# Instala dependências do SO
RUN apt-get clean \
    && apt-get update
RUN apt-get install tzdata

# Seta timezone e localização
RUN echo "America/Sao_Paulo"  > /etc/timezone
RUN dpkg-reconfigure --frontend noninteractive tzdata

# Instala dependências do SO
RUN DEBIAN_FRONTEND=noninteractive apt-get install -yq \
    locales \
    build-essential \
    libpq-dev \
    pkg-config \
    libsasl2-dev \
    libssl-dev \
    libffi-dev \
    wget

# Atualiza pip
RUN pip3 install -U pip

# Instala dependências pelo poetry
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-dev

# Limpa arquivos relativos à instalação de pacotes do SO
RUN apt-get clean -y && \
    apt-get autoclean -y
RUN rm -rf /var/lib/apt/lists/* && \
    sed -i '/pt_BR.UTF-8/s/^# //' /etc/locale.gen && \
    locale-gen pt_BR.UTF-8

ENV LANG pt_BR.UTF-8
ENV LANGUAGE pt_BR
ENV LC_ALL pt_BR.UTF-8

# Copia código da aplicação
COPY src/ /app/
#COPY uwsgi.ini /app/

# Set working directory
WORKDIR /app

# Expõe porta
EXPOSE 1024

#CMD ["uwsgi",  "--ini",  "/app/uwsgi.ini"]
CMD ["python",  "manage.py",  "makemigrations"]
CMD ["python",  "manage.py",  "migrate"]
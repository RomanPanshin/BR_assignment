FROM mcr.microsoft.com/mssql/server:2022-latest

ENV ACCEPT_EULA=Y
ENV SA_PASSWORD=YourStrong!Passw0rd

RUN mkdir -p /usr/src/app

COPY Northwind.sql /usr/src/app/Northwind.sql
COPY AdventureWorks.sql /usr/src/app/AdventureWorks.sql

RUN apt-get update \
    && apt-get install -y curl apt-transport-https gnupg \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list | tee /etc/apt/sources.list.d/msprod.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y mssql-tools unixodbc-dev \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

ENV PATH=$PATH:/opt/mssql-tools/bin

EXPOSE 1433

ENTRYPOINT ["/bin/bash", "/usr/src/app/init-db.sh"]


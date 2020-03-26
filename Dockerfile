FROM ubuntu:16.04

# Add the PostgreSQL PGP key to verify their Debian packages.
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8
# Add PostgreSQL's repository. It contains the most recent stable release of PostgreSQL
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" > /etc/apt/sources.list.d/pgdg.list

# Install ``python-software-properties``, ``software-properties-common`` and PostgreSQL 9.5
RUN apt-get update && apt-get install -y python-software-properties software-properties-common postgresql-9.5 postgresql-client-9.5 postgresql-contrib-9.5
RUN apt-get install -y vim  # just so there is a text editor I'm familiar with in the container

# Run the rest of the commands as the "postgres" user created by the `postgres-9.5` package during installation
USER postgres
# Create the psql role (DB term for user) `cujes`
# Specify the role's password and make it valid forever
# Create the database `cujes` and specify the role `cujes` as its owner
# these are selected to conform to the "real" database (except for the password, for security reasons)
RUN    /etc/init.d/postgresql start &&\
	createuser cujes &&\
	psql --command "ALTER USER \"cujes\" WITH PASSWORD 'pimpekpenis' VALID UNTIL 'infinity';" &&\
    createdb --owner cujes cujes
    #createdb cujes

# Adjust PostgreSQL configuration so that remote connections to the database are possible.
RUN echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/9.5/main/pg_hba.conf
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.5/main/postgresql.conf

# Expose the PostgreSQL port
EXPOSE 5432

# Start the postgres service
CMD ["/usr/lib/postgresql/9.5/bin/postgres", "-D", "/var/lib/postgresql/9.5/main", "-c", "config_file=/etc/postgresql/9.5/main/postgresql.conf"]

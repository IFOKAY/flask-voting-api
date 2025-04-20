#!/bin/bash

# Wait until MariaDB is fully initialized
echo "Waiting for MariaDB to start..."
until mysql -h localhost -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "SHOW DATABASES;" > /dev/null 2>&1; do
  sleep 2
done

# Run SQL scripts to initialize the database and tables
echo "Running SQL scripts..."

# Create the database
mysql -h localhost -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" < /tmp/schema.sql

echo "Database initialized successfully."


# Compilar docker file
docker build .

# crear nuevo proyecto 
docker-compose run --rm app sh -c "django-admin startproject app ."
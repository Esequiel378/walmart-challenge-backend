FROM mongo:3.6.8

# initial data
COPY ./compose/database/mongo-seed/ /mongo-seed
RUN sed -i 's/\r$//g' /mongo-seed/import.sh
RUN chmod +x /mongo-seed/import.sh

FROM mongo:3.6.8 as local

# copy initial data
COPY ./compose/database/data/ /database

# database population script
COPY ./compose/database/mongo-seed/ /mongo-seed
RUN sed -i 's/\r$//g' /mongo-seed/import.sh
RUN chmod +x /mongo-seed/import.sh

FROM mongo:3.6.8 as production

# copy initial data
COPY ./compose/database/data/ /database

# database population script
COPY ./compose/database/mongo-seed/ /mongo-seed
RUN sed -i 's/\r$//g' /mongo-seed/import.sh
RUN chmod +x /mongo-seed/import.sh

ENTRYPOINT ["/mongo-seed/import.sh"]

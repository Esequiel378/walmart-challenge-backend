#!/bin/bash
FILES=$(ls /database/*.json | sort -n -t _ -k 2)

for AFILE in ${FILES[@]}
do
    echo -e "[$(date)] Processing \t$AFILE"
    COLLECTION=`echo $AFILE | sed -n 's/.*\-\(.*\).json/\1/p'`
    mongoimport --host ${DATABASE_HOST} --username ${DATABASE_USERNAME} --password ${DATABASE_PASSWORD} --authenticationDatabase admin --db ${DATABASE_NAME} --collection ${COLLECTION} --mode upsert --file ${AFILE}
    echo -e "[$(date)] Done \t\t$AFILE"
done

echo "[$(date)] No more files to process 🍻"

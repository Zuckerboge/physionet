#!/bin/sh

createdb -U $POSTGRES_USER $DEV_DB -O $POSTGRES_USER
createdb -U $POSTGRES_USER $TEST_DB -O $POSTGRES_USER

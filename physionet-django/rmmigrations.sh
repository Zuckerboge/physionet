for i in physiobank physionetworks physiotoolkit catalog users
do
    rm $i/migrations/0* 2> /dev/null
done

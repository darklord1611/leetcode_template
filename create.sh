
if [ $1 ]; 
then
    mkdir daily/$1
else
    echo "Please provide a name for the directory"
    exit 1
fi


cd daily/$1

touch solution.py

cd -
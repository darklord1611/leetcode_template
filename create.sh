
if [ $1 ]; then
    rm -r daily/$1
fi

mkdir daily/$1


cd daily/$1

touch solution.py

cd -
for i in {1..10} 
do
    g++ main.cpp -o main
    echo "kafjdfklajklg" > test.csv
    ./main > test.csv
done 
# $(...) : 결과 실행 후 값 대입
# ls : 파일 리스트
# wc -l : 개수 세기
variable=$(find . -name '*.sh' | wc -l) 

echo "$variable"

# compile c++ file 
g++ main.cpp -o main  

# save into txt file 
./main > main.txt

# file input by line 
while IFS= read -r line; do
    echo "Text read from file: $line"
done < main.txt

output="" 
for i in {1..10} 
do
    g++ main.cpp -o main
    output= ./main
done 

$output > test.csv
cat test.csv


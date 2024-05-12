# Directory 
SUBDIR="../Submission"

# $1: Lab# $2: Ex# 

ASDF=()
for ((i=1; i<=$2; i++)); do
    echo "$SUBDIR/Lab$1/Answer/ex$1_$2.txt"
    ASDF[$i]=cat $SUBDIR/Lab$1/Answer/ex$1_$i.txt
done

echo "CORRECT ANSWER"
for ((i=1; i<$2; i++)); do
    echo ${ASDF[$i]}
done 

echo "SUBMITTED ANSWER"

for lab in $SUBDIR/Lab$1/*; do
    if [$lab=="$SUBDIR/Lab$1/Answer"]; then
        echo $lab
    fi
    for student in $lab/*; do
        for ((i=1; i<=$2; i++)); do
            path="$student/ex$1_$i"
            g++ $path.cpp -o $path 
            ./$path 
        done
    done
done
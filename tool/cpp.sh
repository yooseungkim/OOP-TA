# Directory -> 제출 최상위 폴더만 추가
HOMEDIR=$(pwd)
SUBDIR="../Submission" 
BLACK="\e[0;30m"
RED="\e[0;31m"
GREEN="\e[0;32m" 
YELLOW="\e[0;33m"
BLUE="\e[0;34m"
MAGENTA="\e[0;35m"
CYAN="\e[0;36m"
GRAY="\e[0;37m"
WHITE="\e[0;38m"


# $1: Lab# $2: Ex# $3: Recompile 

echo $#
if [ $# < 2 ]; then
    echo -e $RED "Error: not enough arguments (score.sh requires lab# and ex#)" $BLACK
    exit 9

LAB_NO=$1
EX_NO=$2
RECOMPILE=${3:-false}

ASDF=()

# READ CORRECT ANSWER
for ((i=1; i<=$2; i++)); do
    PATH="$SUBDIR/Lab$1/Answer/ex$1_$i.txt"
    echo $PATH
done

echo "CORRECT ANSWER"
for ((i=0; i<$2; i++)); do
    echo ${ASDF[$i]}
done 

# READ SUBMITTED ANSWER
echo "SUBMITTED ANSWER"
# FOR EACH LAB SESSION 
for LAB in $SUBDIR/Lab$1/*; do 
    echo $LAB
    # FOR EACH STUDENT
    for STUDENT in $LAB/*; do
        # DO NOT COMPILE ON ANSWER DIRECTORY
        if [[ "$STUDENT" =~ Answer ]]; then continue; fi
        
        echo -e "Checking >> $CYAN $STUDENT $BLACK"
        # COMPILE AND RUN THE SUBMITTED FILE
        for ((i=1; i<=$2; i++)); do
            COMPILE_FILE="$STUDENT/ex$1_$i"
            # IF c++ FILE IS ALREADY COMPILED THEN JUST RUN EXECUTABLE FILE
            if [ $RECOMPILE == true ] || [ ! -e $COMPILE_FILE ]; then
                # g++ $COMPILE_FILE.cpp -o $COMPILE_FILE
                echo "!"
            fi
            # RUN EXECUTABLE FILE
            OUTPUT=./$COMPILE_FILE 
            $OUTPUT > test.csv
        done
    done
done
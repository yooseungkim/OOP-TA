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

# string join function
function join_by { local IFS="$1"; shift; echo "$*"; }

# $1: Lab# $2: Ex# $3: Recompile 

if [[ $#<2 ]]; then
    echo -e $RED "Error: not enough arguments (score.sh requires lab# and ex#)" $BLACK
    exit 9
fi 

LAB_NO=$1
EX_NO=$2
RECOMPILE=${3:-false}
ANSWERS=()
RESULTS=() 
# READ CORRECT ANSWER
for ((i=1; i<=$2; i++)); do
    ANSWER_PATH="$SUBDIR/Lab$1/Answer/ex$1_$i.txt"
    ANSWERS+=("$(cat $ANSWER_PATH)")
done
echo "CORRECT ANSWER"
echo ${ANSWERS[@]}
# READ SUBMITTED ANSWER
echo "SUBMITTED ANSWER"
# FOR EACH LAB SESSION
for LAB in $SUBDIR/Lab$1/*; do 
    if [[ "$LAB" =~ Answer ]]; then continue; fi
    echo -e $MAGENTA Now On : $LAB $BLACK
    # FOR EACH STUDENT
    for STUDENT in $LAB/*; do
        # DO NOT COMPILE ON ANSWER DIRECTORY        
        echo -e "Checking >> $CYAN $STUDENT $BLACK"
        TEMP_RESULT=()
        # COMPILE AND RUN THE SUBMITTED FILE
        for ((i=1; i<=$2; i++)); do
            COMPILE_FILE="$STUDENT/ex$1_$i"
            # IF c++ FILE IS ALREADY COMPILED THEN JUST RUN EXECUTABLE FILE
            if [ $RECOMPILE == true ] || [ ! -e $COMPILE_FILE ]; then
                g++ $COMPILE_FILE.cpp -o $COMPILE_FILE
            fi
            # RUN EXECUTABLE FILE
            OUTPUT=$(./$COMPILE_FILE)

            # Check whether answer is correct or not
            if [ "$OUTPUT" == "${ANSWERS[$i - 1]}" ]; then 
                echo -e $GREEN Correct! $BLACK 
                TEMP_RESULT+=("O")
                TEMP_RESULT+=("$OUTPUT")
                
            else 
                echo -e $YELLOW Expected: ${ANSWERS[$i - 1]} "<->" Submitted: $OUTPUT $BLACK
                TEMP_RESULT+=("X")
                TEMP_RESULT+=("$OUTPUT")
            fi
        done
        join_by ,  "${TEMP_RESULT[@]}"
        RESULTS+=$TEMP_RESULT
        
    done
done
cd $HOMEDIR

echo "1 2 3 4 5" >> score.csv
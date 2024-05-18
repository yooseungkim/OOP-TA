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

#check openpyxl installed
# clear logs 
clear

echo -e $BLUE"Start Scoring Program..."$BLACK

# $1: Lab# $2: Ex# $3: Recompile 

if [[ $# < 2 ]]; then
    echo -e $RED "Error: not enough arguments (score.sh requires lab# and ex#)" $BLACK
    exit 9
fi 

# string join function
function join_by { local IFS="$1"; shift; echo "$*" >> score.txt; }

LAB_NO=$1
EX_NO=$2
declare -i TC_NO=0 
RECOMPILE=${3:-false}
SAVE_TXT=${4:-"score.txt"}
ANSWERS=()
TESTCASES=() 

# INIT SCORE FILE
rm $SAVE_TXT
echo $1 >> $SAVE_TXT
echo $2 >> $SAVE_TXT
# READ CORRECT ANSWER
for ANSWER_PATH in $SUBDIR/Lab$1/Answer/ex$1_$2_*.txt; do
    TC_NO+=1
    ANSWERS+=("$(cat $ANSWER_PATH)")
done

#for (( i=1; i<=$TC_NO; i++ )); do 
#    $TESTCASE_FILE=$SUBDIR/Lab$1/Testcase/ex$1_$2_$i.txt
#    if [ ! -e $TESTCASE_FILE ]; then 
#        echo "NO INPUT FOR THIS PROGRAM" > $TESTCASE_FILE
#    fi 
#    TESTCASES+=($TESTCASE_FILE) 
#done

for TESTCASE_PATH in $SUBDIR/Lab$1/Testcase/ex$1_$2_*.txt; do
    TESTCASES+=("$TESTCASE_PATH")
done

# READ SUBMITTED ANSWER
# FOR EACH LAB SESSION
for LAB in $SUBDIR/Lab$1/*; do 
    if [[ "$LAB" =~ Answer || "$LAB" =~ Testcase ]] ; then continue; fi
    echo -e $MAGENTA Now On : $LAB $BLACK
    # echo $LAB >> $SAVE_TXT 
    # FOR EACH STUDENT
    for STUDENT in $LAB/*; do
        # DO NOT COMPILE ON ANSWER DIRECTORY        
        echo -e "Checking >> $CYAN $STUDENT $BLACK"
        echo $STUDENT >> $SAVE_TXT
        # COMPILE AND RUN THE SUBMITTED FILE
        for ((i=1; i<=$TC_NO; i++)); do
            COMPILE_FILE="$STUDENT/ex$1_$2"
            # IF c++ FILE IS ALREADY COMPILED THEN JUST RUN EXECUTABLE FILE
            if [[ $RECOMPILE == true ]] || [ ! -e $COMPILE_FILE ]; then
                # compile all files with format ex1_1_*.cpp (to use header files) 
                # all source files should be named of the format ex1_1_Car.cpp
                g++ $COMPILE_FILE*.cpp -o $COMPILE_FILE
                if  [ $? -ne 0 ]; then 
                    echo -e $RED"Raised Error"$BLACK
                    echo "X" >> $SAVE_TXT 
                    echo "Raised Error" >> $SAVE_TXT 
                    continue 
                fi 
            fi
            # RUN EXECUTABLE FILE
            OUTPUT=$(cat ${TESTCASES[$i - 1]} | ./$COMPILE_FILE)

            # Check whether answer is correct or not
            if [ "$OUTPUT" == "${ANSWERS[$i - 1]}" ]; then 
                echo -e $GREEN"[$i] Correct!"$BLACK 
                echo "O" >> $SAVE_TXT
                echo $OUTPUT >> $SAVE_TXT
                
            else 
                echo -e $RED[$i]$YELLOW" Expected: "${ANSWERS[$i - 1]} "<-> Submitted: "$OUTPUT$BLACK
                echo "X" >> $SAVE_TXT
                echo $OUTPUT >> $SAVE_TXT
            fi
        done
        # join_by ,  "${TEMP_RESULT[@]}"
        # RESULTS+=("$TEMP_RESULT")
        echo "=====NEXT STUDENT=====" >> $SAVE_TXT
    done
    echo "=====NEXT SESSION=====" >> $SAVE_TXT
done
echo "=====COMPLETE=====" >> $SAVE_TXT

python score.py


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

if [[ $1 == -h ]]; then 
    echo "HELP MESSAGE"
    exit 0 
fi

if [[ $# < 2 ]]; then
    echo -e $RED "Error: not enough arguments (score.sh requires lab# and ex#)" $BLACK
    exit 9
fi 


LAB_NO=$1
EX_NO=$2
RECOMPILE=${3:-"false"}
NO_ANSWER=${4:-"false"}
declare -i TC_NO=0 
SAVE_TXT="../Scores/Lab${LAB_NO}/ex${LAB_NO}_${EX_NO}_score.txt"
ANSWERS=()
TESTCASES=() 
# MAKE DIRECTORY IF IT DOES NOT EXSIT

if [ ! -d ../Scores/Lab${LAB_NO} ]; then   
    mkdir ../Scores/Lab${LAB_NO}
fi

# INIT SCORE FILE
if [ -e $SAVE_TXT ]; then 
    rm $SAVE_TXT
fi
# READ CORRECT ANSWER
for ANSWER_PATH in $SUBDIR/Lab${LAB_NO}/Answer/ex${LAB_NO}_${EX_NO}_*.txt; do
    TC_NO+=1
    if [[ $NO_ANSWER -ne "false" ]]; then 
        echo "Scoring without Answer File"
        break
    fi

    ANSWERS+=("$(cat $ANSWER_PATH)")
    if [ $? -ne 0 ] && [[ $NO_ANSWER -ne "false" ]]; then 
        echo -e $RED"Answer File Does Not Exist"$BLACK
        exit 9
    fi
done

for (( i=1; i<=$TC_NO; i++ )); do 
   TESTCASE_FILE=$SUBDIR/Lab${LAB_NO}/Testcase/ex${LAB_NO}_${EX_NO}_$i.txt
   if [ ! -e $TESTCASE_FILE ]; then 
       echo "NO INPUT FOR THIS PROGRAM" > $TESTCASE_FILE
   fi 
   TESTCASES+=("$TESTCASE_FILE") 
done

# for TESTCASE_PATH in $SUBDIR/Lab$1/Testcase/ex$1_$2_*.txt; do
#     TESTCASES+=("$TESTCASE_PATH")
# done

# READ SUBMITTED ANSWER
# FOR EACH LAB SESSION
for LAB in $SUBDIR/Lab${LAB_NO}/*; do 
    if [[ "$LAB" =~ Answer || "$LAB" =~ Testcase ]] ; then continue; fi
    echo -e $MAGENTA"Now On : "$LAB $BLACK
    # echo $LAB >> $SAVE_TXT 
    # FOR EACH STUDENT
    for STUDENT in $LAB/*; do
        # DO NOT COMPILE ON ANSWER DIRECTORY        
        echo -e "Checking >> $CYAN $STUDENT $BLACK"
        echo $STUDENT >> $SAVE_TXT
        # COMPILE THE SUBMITTED FILE
        COMPILE_FILE=$STUDENT/ex${LAB_NO}_${EX_NO}
        # IF c++ FILE IS ALREADY COMPILED THEN JUST RUN EXECUTABLE FILE
        if [[ $RECOMPILE == true ]] || [ ! -e $COMPILE_FILE ]; then
            # compile all files with format ex1_1_*.cpp (to use header files) 
            # all source files should be named of the format ex1_1_Car.cpp
            g++ $COMPILE_FILE*.cpp -o $COMPILE_FILE
            if  [ $? -ne 0 ]; then 
                echo -e $RED"COMPILE Error"$BLACK
                echo "X" >> $SAVE_TXT 
                echo "Compile Error" >> $SAVE_TXT 
                continue 
            fi 
        fi
        for ((i=1; i<=$TC_NO; i++)); do
            # RUN EXECUTABLE FILE
            OUTPUT=$(cat ${TESTCASES[$i - 1]} | ./$COMPILE_FILE)
            RAN_SUCCESS=$?
            # Check whether answer is correct or not
            if [[ $NO_ANSWER -eq "false" ]]; then 
                if [ "$OUTPUT" == "${ANSWERS[$i - 1]}" ]; then 
                    echo -e $GREEN"[$i] Correct!"$BLACK 
                    echo "O" >> $SAVE_TXT
                    echo $OUTPUT >> $SAVE_TXT
                else 
                    echo -e $RED[$i]$YELLOW" Expected: "${ANSWERS[$i - 1]} "<-> Submitted: "$OUTPUT$BLACK
                    echo "X" >> $SAVE_TXT
                    echo $OUTPUT >> $SAVE_TXT
                fi
            else 
                if [ $RAN_SUCCESS -eq 0 ]; then 
                    echo -e $GREEN[$i] $OUTPUT $BLACK
                    echo "O" >> $SAVE_TXT
                    echo $OUTPUT >> $SAVE_TXT
                else 
                    echo -e $RED[$i] RUN TIME ERROR $BLACK 
                    echo "X" >> $SAVE_TXT
                    echo Run Time Error >> $SAVE_TXT
                fi
            fi
        done
        echo "=====NEXT STUDENT=====" >> $SAVE_TXT
    done
    echo "=====NEXT SESSION=====" >> $SAVE_TXT
    echo ================================================
done
echo "=====COMPLETE=====" >> $SAVE_TXT
# COMPLETE SCORING 
echo -e $MAGENTA"SCORING COMPLETED"$BLACK
# EXPORT CSV FILE - SCORE.PY
echo -e $CYAN"EXPORTING CSV FILE..."$BLACK 
python score.py $LAB_NO $EX_NO

# CHECK WHETHER SCORE.PY HAS SUCCESSFULLY TERMINATED
if [ $? -ne 0 ]; then 
    echo -e $RED"Couldn't Finish Exporting CSV File"$BLACK ... Please Check score.py
else
    echo -e $CYAN"Finished Exporting CSV File"$BLACK 
    echo -e $BLUE"Terminating Scoring Program Successfully"$BLACK
fi

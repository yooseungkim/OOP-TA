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

# $1: Lab# $2: Ex# $3: Recompile 

if [[ $1 == -h ]]; then 
    echo "HELP MESSAGE"
    exit 0 
fi

if [[ $# < 3 ]]; then
    echo -e $RED "Error: not enough arguments (score.sh requires lab#, ex#, tc#)" $BLACK
    exit 1
fi 


LAB_NO=$1
EX_NO=$2
declare -i TC_NO=$3
shift
shift
shift 
RECOMPILE='false' 
NO_ANSWER='false'  
VERBOSE='false' 
# RECOMPILE=${3:-"false"}
# NO_ANSWER=${4:-"false"}

while getopts 'rnvh' flag; do
  case "${flag}" in
    r) RECOMPILE='true' ;;
    n) NO_ANSWER='true' ;;
    v) VERBOSE='true' ;;
    h) 
        echo -e $YELLOW"score.sh help message"$BLACK
        echo -e $MAGENTA"Usage$BLACK: ./score.sh $MAGENTA#(lab) #(ex) #(testcases)$BLACK"
        echo Example: ./score.sh 1 3 3 -r -n
        echo flags: 
        echo -e $MAGENTA'\t'-r$BLACK: recompile the submitted source files 
        echo -e $MAGENTA'\t'-n$BLACK: use when there is no certain answer 
        echo -e $MAGENTA'\t'-h$BLACK: show help message
        exit 1;; 
    *) 
        echo -e $RED"Invalid Flag"$BLACK
        exit 1 ;;
  esac
done


echo -e $BLUE"Starting Scoring Program..."$BLACK

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

# IF -n FLAG, SCORE WITHOUT ANSWER FILE 
if [[ $NO_ANSWER == 'true' ]]; then 
    echo "Scoring without Answer File"
else
    # READ CORRECT ANSWER
    for ANSWER_PATH in $SUBDIR/Lab${LAB_NO}/Answer/ex${LAB_NO}_${EX_NO}_*.txt; do
        # CHECK # TEST CASES
        # APPEND ANSWER INTO ANSWERS ARRAY 
        ANSWERS+=("$(cat $ANSWER_PATH)")
        # IF THERE SHOULD BE ANSWER FILE BUT NO ANSWER FILE, RAISE ERROR 
        if [ $? -ne 0 ]; then 
            echo -e $RED"Answer File Does Not Exist"$BLACK
            exit 1
        fi
    done
fi

# ECHO RECOMPILE OPTION 
if [[ $RECOMPILE == 'true' ]]; then 
    echo "Recompile the Source Files"
else
    echo "Using Existing Executable Files" 
fi 

# CHECK TEST CASES 
for (( i=1; i<=$TC_NO; i++ )); do 
   TESTCASE_FILE=$SUBDIR/Lab${LAB_NO}/Testcase/ex${LAB_NO}_${EX_NO}_$i.txt
    # IF NO TESTCASE FILE, THEN REGARD AS THE PROGRAM DOES NOT NEED INPUT FILES
   if [ ! -e $TESTCASE_FILE ]; then 
       echo "NO INPUT FOR THIS PROGRAM" > $TESTCASE_FILE
   fi 
   TESTCASES+=("$TESTCASE_FILE") 
done

# READ SUBMITTED ANSWER
# FOR EACH LAB SESSION
for LAB in $SUBDIR/Lab${LAB_NO}/*; do 
    # LOOP EXCEPT ANSWER AND TESTCASE FOLDERS
    if [[ "$LAB" =~ Answer || "$LAB" =~ Testcase ]] ; then continue; fi
    echo -e $MAGENTA"Now On : "$LAB $BLACK
    # FOR EACH STUDENT
    for STUDENT in $LAB/*; do        
        echo -e "Checking >> $CYAN $STUDENT $BLACK"
        # SAVE STUDENT ID INTO TXT FILE 
        echo $STUDENT >> $SAVE_TXT
        # COMPILE THE SUBMITTED FILE
        COMPILE_FILE=$STUDENT/ex${LAB_NO}_${EX_NO}
        # IF c++ FILE IS ALREADY COMPILED AND NO -r FLAG, THEN JUST RUN EXECUTABLE FILE 
        if [[ $RECOMPILE == 'true' ]] || [ ! -e $COMPILE_FILE ]; then
            # compile all files with format ex1_1_*.cpp (to use header files) 
            # all source files should be named of the format ex1_1_Car.cpp
            
            # IF NO SOURCE FILE IS SUBMITTED THEN 
            if  [ ! -e "$COMPILE_FILE.cpp" ]; then 
                echo -e $RED"NO SUBMISSION"$BLACK
                for ((i=1; i<=$TC_NO; i++)); do
                    # REGARD AS INCORRECT ANSWER 
                    echo "X" >> $SAVE_TXT 
                    echo "No Submission" >> $SAVE_TXT
                done  
                echo 
                echo "=====NEXT STUDENT=====" >> $SAVE_TXT
                continue 
            fi 
            
            
            g++ $COMPILE_FILE*.cpp -o $COMPILE_FILE

            # IF COMPILE FAILED, THEN RAISE "COMPILE ERROR"
            if  [ $? -ne 0 ]; then 
                echo -e $RED"COMPILE Error"$BLACK       
                for ((i=1; i<=$TC_NO; i++)); do
                    # REGARD AS INCORRECT ANSWER 
                    echo "X" >> $SAVE_TXT 
                    echo "Compile Error" >> $SAVE_TXT
                done  
                echo 
                echo "=====NEXT STUDENT=====" >> $SAVE_TXT
                continue 
            fi 
        fi
        for ((i=1; i<=$TC_NO; i++)); do
            # RUN EXECUTABLE FILE
            OUTPUT=$(cat ${TESTCASES[$i - 1]} | ./$COMPILE_FILE)
            # CHECK EXECUTABLE FILE HAS TERMINATED SUCCESSFULLY
            RAN_SUCCESS=$?
            if [ $RAN_SUCCESS -eq 0 ]; then   
                # IF THERE IS NO GIVEN ANSWER, REGARD AS CORRECT ANSWER IF RAN SUCCESSFULLY          
                if [[ $NO_ANSWER == 'false' ]]; then 
                    # CHECK CORRECT ANSWER 
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
                    echo -e $GREEN[$i] $OUTPUT $BLACK
                    echo "O" >> $SAVE_TXT
                    echo $OUTPUT >> $SAVE_TXT
                fi 
            else 
                echo -e $RED[$i] RUN TIME ERROR $BLACK 
                echo "X" >> $SAVE_TXT
                echo Run Time Error >> $SAVE_TXT
            fi
        done
        echo 
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

# CHECK WHETHER score.py HAS SUCCESSFULLY TERMINATED
if [ $? -ne 0 ]; then 
    echo -e $RED"Couldn't Finish Exporting CSV File"$BLACK ... Please Check score.py
    exit 1
else
    echo -e $CYAN"Finished Exporting CSV File"$BLACK 
    echo -e $BLUE"Terminating Scoring Program Successfully"$BLACK
    exit 0
fi

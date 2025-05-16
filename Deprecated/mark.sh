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

LAB_NO=$1
EX_NO=$2
TC_NO=$3
DEFAULT='true'
SUMMARY='false'
shift
shift
shift 
ANSWER_PATH="$SUBDIR/Lab${LAB_NO}/Answer"
TESTCASE_PATH="$SUBDIR/Lab${LAB_NO}/Testcase" 

clear 

echo -e $BLUE"Starting Integrated Marking Program"$BLACK

while getopts 'ihs' flag; do
  case "${flag}" in
    i)
        echo -e $MAGENTA"Input New Testcases"$BLACK
        DEFAULT='false'
        ;;  
    h) 
        echo -e $YELLOW"mark.sh help message"$BLACK
        echo -e $MAGENTA"Usage$BLACK: ./mark.sh $MAGENTA#(lab) #(ex) #(testcases)$BLACK"
        echo Example: ./mark.sh 1 3 3 -i
        echo flags: 
        echo -e $MAGENTA'\t'-i$BLACK: make new testcases
        echo -e $MAGENTA'\t'-h$BLACK: show help message
        exit 1;; 
    s)
        SUMMARY='true' 
        ;;
    *) 
        echo -e $RED"Invalid Flag"$BLACK
        exit 1 ;;
  esac
done

if [[ $DEFAULT == 'false' ]]; then
    ./input.sh ${LAB_NO} ${EX_NO} ${TC_NO} 
fi 

./score.sh ${LAB_NO} ${EX_NO} ${TC_NO} -r

if [[ $SUMMARY == 'true' ]]; then
    echo -e $CYAN"Starting Summary Program"$BLACK
    python summary.py ${LAB_NO} ${EX_NO}
fi 

if [[ $? -eq 0 ]]; then
    echo -e $BLUE"Marking Program Terminated Successfully"$BLACK
fi

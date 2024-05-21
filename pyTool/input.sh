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
declare -i DEFAULT=0
shift
shift
shift 
ANSWER_PATH="$SUBDIR/Lab${LAB_NO}/Answer"
TESTCASE_PATH="$SUBDIR/Lab${LAB_NO}/Testcase" 

while getopts 'ih' flag; do
  case "${flag}" in
    i)
        if [ -e $ANSWER_PATH ]; then
            echo -e $MAGENTA"Add Testcases to Exsisting Testcases"$BLACK
            DEFAULT=$(find $ANSWER_PATH -name "*." -type f | wc -l)
        else
            echo -e $MAGENTA"No Testcases Found"$BLACK 
        fi;;
    h) 
        echo -e $YELLOW"score.sh help message"$BLACK
        echo -e $MAGENTA"Usage$BLACK: ./input.sh $MAGENTA#(lab) #(ex) #(testcases)$BLACK"
        echo Example: ./input.sh 1 3 3 -i
        echo flags: 
        echo -e $MAGENTA'\t'-i$BLACK: use existing test cases
        echo -e $MAGENTA'\t'-h$BLACK: show help message
        exit 1;; 
    *) 
        echo -e $RED"Invalid Flag"$BLACK
        exit 1 ;;
  esac
done

if [[ $DEFAULT == 0 ]]; then
    echo -e $MAGENTA"Initializing Testcase/Answer Directory"$BLACK
    rm -rf $ANSWER_PATH
    rm -rf $TESTCASE_PATH
    mkdir $ANSWER_PATH
    mkdir $TESTCASE_PATH 
fi 

python input.py $LAB_NO $EX_NO $TC_NO

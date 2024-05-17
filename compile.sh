#!/bin/sh

# shellcheck disable=SC2039
file_list=()

# shellcheck disable=SC2113
function getPaths {
  for file in "$1"/*
  do
    if [ -d "$file" ];
    then
      getPaths "$file"
    elif [ -f "$file" ];
    then
      file_list+=( "$file" )
    fi
  done
}

if [ -z "$1" ]; then
  # shellcheck disable=SC2006
  main_path=`pwd`
else
  main_path=$(dirname "$1")
fi

# create compile dir
COMPILE_PATH="$main_path"/compile
if [ ! -d "$COMPILE_PATH" ]; then
  mkdir "$COMPILE_PATH"
fi
rm "$COMPILE_PATH"/*

getPaths "$main_path"

for file in "${file_list[@]}"
do
  # shellcheck disable=SC2006
  base=`basename "$file"`
  case "${base##*.}" in
    "c")
      gcc -c "$file"
      ;;
    "cpp"|"cc")
      g++ -c "$file"
      ;;
  esac
done

# shellcheck disable=SC2066
# shellcheck disable=SC2006
for file in "$main_path"/*.o
do
    # shellcheck disable=SC2046
    mv "$file" "$COMPILE_PATH"/`basename "$file"`
done

# shellcheck disable=SC2181
# shellcheck disable=SC2006 disable=SC2046
if [ $? -eq 0 ]; then
  g++ `echo "$COMPILE_PATH"/*.o` -o "$COMPILE_PATH"/main

else
  gcc `echo "$COMPILE_PATH"/*.o` -o "$COMPILE_PATH"/main
fi

"$COMPILE_PATH"/main
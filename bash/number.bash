#!/bin/bash

echo -n "Input a number: "
read number

case $number in
50)
echo "Fifty!!" ;;
100)
echo "Double fifty!!" ;;
*)
echo "Neither 100 nor 200" ;;
esac

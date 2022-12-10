
arr=();
curr=0;
while read line; do
    if test "$line" == $''
    then
        arr+=($curr);
        curr=0;
    else
        curr=$((curr+line));
    fi
done < /dev/stdin;

printf '%s\n' ${arr[@]} | sort -nr | head -n1;
printf '%s\n' ${arr[@]} | sort -nr | head -n3 | awk '{tot+=$1} END {print tot}';
#!/bin/bash
for i in *.ogg;
do
	ffmpeg -i "$i" "${i%.*}.mp3";
done

cnt=1

for files in *.mp3;
do
	mv "$files" './sigh_'$cnt'.mp3';
	cnt=$((cnt+1));
done


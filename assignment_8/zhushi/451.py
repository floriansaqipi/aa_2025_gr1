#!/usr/bin/env python3
import sys

def frequencySort(s: str)->str:
   
    char_map = {} # init dict
    char_list = []

    # count chars
    for ch in s:
        if ch not in char_map:
            char_map[ch] = 0
        char_map[ch] += 1 
    
    for ch, count in char_map.items():
        print(f"Char:{ch} -> Count:{count}") 

    for ch, count in char_map.items():
        char_list.append((ch, count)) 
   
    # sort
    n = len(char_list)
    for i in range(0, n-1):
        for j in range(i+1, n):
            if char_list[i][1] < char_list[j][1]:
                char_list[i], char_list[j] = char_list[j], char_list[i]
   
    for ch in char_list:
        print(ch)

    string_builder = ""
    for character in char_list:
        for i in range (character[1]):
            string_builder += character[0]

    return string_builder

if __name__ == "__main__":
    string = "aaabbbbsss"
    print(frequencySort(string))

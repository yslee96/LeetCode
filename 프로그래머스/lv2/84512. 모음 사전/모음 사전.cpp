#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>
using namespace std;
unordered_set<string> words;
char vowels[5] = {'A', 'E', 'I', 'O', 'U'};
void make_words(int size, string cur_str){
    if(size==5)
        return;
    for(int i=0; i<5; i++){
        string new_str = cur_str + vowels[i];
        words.insert(new_str);
        make_words(size+1, new_str);
    }
}

int solution(string word) {
    int answer = 0;
    make_words(0, "");
    vector<string> wordSet(words.begin(), words.end());
    sort(wordSet.begin(), wordSet.end());
    return find(wordSet.begin(), wordSet.end(), word) - wordSet.begin() + 1;
}
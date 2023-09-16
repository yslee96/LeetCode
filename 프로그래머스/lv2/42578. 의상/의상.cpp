#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 1;
    unordered_map<string, int> clothesMap;
    
    for(auto info : clothes){
        clothesMap[info[1]]++;
    }
    
    unordered_map<string,int>::iterator iter;
    for(iter=clothesMap.begin(); iter!=clothesMap.end(); iter++){
        answer = answer * (iter->second+1);
    }
    
    
    return answer-1;
}
class Solution {
public:
    int canBeTypedWords(string text, string brokenLetters) {
        stringstream ss(text);
        string word;
        int count = 0; 

        while (ss >> word) {
            bool broken = false;
            for (char ch : brokenLetters) {
                if (word.find(ch) != string::npos) { 
                    broken = true; 
                    break; 
                }
            }
            if (!broken) count++;
        }
        return count;
    }
};

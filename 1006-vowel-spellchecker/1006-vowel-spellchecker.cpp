class Solution {
public:
    vector<string> spellchecker(vector<string>& wordlist, vector<string>& queries) {
        unordered_set<string> exact(wordlist.begin(), wordlist.end());
        unordered_map<string,string> cap, vowel;

        for(string w : wordlist){
            string low = toLower(w);
            if(!cap.count(low)) cap[low] = w;

            string m = mask(low);
            if(!vowel.count(m)) vowel[m] = w;
        }

        vector<string> ans;
        for(string q : queries){
            if(exact.count(q)) ans.push_back(q);           
            else {
                string low = toLower(q);
                if(cap.count(low)) ans.push_back(cap[low]); 
                else {
                    string m = mask(low);
                    if(vowel.count(m)) ans.push_back(vowel[m]); 
                    else ans.push_back("");                    
                }
            }
        }
        return ans;
    }

    string toLower(string s){
        for(char &c : s) c = tolower(c);
        return s;
    }

    string mask(string s){
        for(char &c : s)
            if(c=='a'||c=='e'||c=='i'||c=='o'||c=='u') c = '#';
        return s;
    }
};

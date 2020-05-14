#include <iostream>
#include<string>
#include <cstdlib>

using namespace std;

int main()
{
    string Test = "got41443882/120/05/12pkts/drops/pktinfisue/crptswith43.83178Gbpsduring1.00387sec";
    cout<<Test<<endl;


    string pkts="";
    string drops="";
    string pktinf = "";
    string crpt = "";
    string gbps ="";
    string time = "";


    size_t gotPosition = Test.find("t");
    size_t pktsPosition = Test.find("pkts");

    string FirstNumber = Test.substr(gotPosition+1, (pktsPosition-gotPosition-1));
    string delimiter = "/";

    size_t pos = 0;
    string token;
    int varSelect = 0;
    while ((pos = FirstNumber.find(delimiter)) != string::npos) {
        token = FirstNumber.substr(0, pos);
        if(varSelect == 0){
            pkts = token;
        }
        else if(varSelect == 1){
            drops = token;
        }
        else if(varSelect == 2){
            pktinf = token;
        }
        FirstNumber.erase(0, pos + delimiter.length());
        varSelect ++;
    }
    crpt = FirstNumber;

    size_t gbpsStart = Test.find("th");
    size_t gbpsStop = Test.rfind("G");
    gbps = Test.substr(gbpsStart+2, (gbpsStop-gbpsStart-2));

    size_t timeStart = Test.find("ng");
    size_t timeStop = Test.rfind("sec");
    time = Test.substr(timeStart+2, (timeStop-timeStart-2));

  
  
  
    // ************************************************
    //Get Your Desired Value from Here !!!!!!!!!!!!!

    cout<<pkts<<" "<<drops<<" "<<pktinf<<" "<<crpt<<" "<<gbps<<" "<<time<<endl;


    return 0;

    }

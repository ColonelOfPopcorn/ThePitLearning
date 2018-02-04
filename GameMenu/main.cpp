#include <iostream>
#include <ctime>
#include <cstdlib>

using namespace std;

bool debug = true;

//Display the initial message the player sees when opening the game. Will eventually be expanded to include menu selections.
void introduction()
{
    std::cout << "Welcome to The Test!" << std::endl;
}

int diceroll(int dicecount, int dicesides){
    if (debug){
        std::cout << "dicecount: " << dicecount << std::endl;
        std::cout << "dicesides: " << dicesides << std::endl;
    }
    for (int i=0; i<dicecount; i++){
            if (debug){
                std::cout << "Roll " << i+1 << std::endl;
            }
            srand(time(NULL));
            int result = rand()%dicesides + 1;
            std::cout << "Dice " << i+1 << " result: " << result << std::endl;
    }
}

int dicequery(){
    std::cout << "how many dice would you like to roll?" << std::endl;
    string input;
    getline(std::cin, input);
}

//A toggle menu to turn Debug on or off. Modifies the global Debug variable.
int debugmenu(){
    //checks first if Debug is already on. If so, it gives the user the option to turn it off or leave it on
    if (debug == true){
        std::cout << "Debug mode is currently ON. Would you like to turn it OFF? y/n" << std::endl;
        //this will keep the prompts repeating until a valid selection is made
        int menuloop = 0;
        while (menuloop == 0){
            string response;
            //std::cin >> ws;
            getline(std::cin, response);
            if(response == "Y" || response == "Yes" || response == "y" || response == "yes"){
                debug = false;
                std::cout << "Debug has been turned off." << std::endl;
                menuloop = 1;
            }else if (response == "N" || response == "No" || response == "n" || response == "no"){
                menuloop = 1;
            }else{
            std::cout << "Invalid Selection." << std::endl;
            std::cout << "Debug mode is currently ON. Would you like to turn it OFF? y/n" << std::endl;
            }
        }
        return 0;
    }
    //checks if Debug is off. If it's not on, it should be off, but we still check in case something has gone wrong
    if (debug == false){
        std::cout << "Debug mode is currently OFF. Would you like to turn it ON? y/n" << std::endl;
        int menuloop = 0;
        while (menuloop == 0){
            string response;
            std::cin >> ws;
            getline(std::cin, response);
            if (response == "Y" || response == "Yes" || response == "y" || response == "yes"){
                debug = true;
                std::cout << "Debug has been turned on." << std::endl;
                menuloop = 1;
            }else if (response == "N" || response == "No" || response == "n" || response == "no"){
                menuloop = 1;
            }else{
            std::cout << "Invalid Selection." << std::endl;
            std::cout << "Debug mode is currently OFF. Would you like to turn it ON? y/n" << std::endl;
            }
        }
        return 0;
    }
    //a bit of extra debug; if this message ever shows up, then neither IF statement triggered
    std::cout << "prematurely exiting debug menu" << std::endl;
}

void clientinput()
{
    std::cout << "What would you like to do?" << std::endl;
    if (debug)
        {
        std::cout << "Debug mode is ON" << std::endl;
        }
    string input;
    getline(std::cin, input);
    if (debug)
    {
        std:cout << "<DEBUG>You entered: '" << input << "'" << std::endl;
    }
    if (input=="/debug"){
        debugmenu();
    }else if (input == "/roll"){
        std::cout << "static 1d20 roll" << std::endl;
        diceroll(1, 20);
    }else{
        std::cout << "Invalid command." << std::endl;
    }
    /*int menuloop = 0;
        while (menuloop = 0){
            string response;
            std::cin >> ws;
            getline(std::cin, response);
            switch (string(response)) {
        case "/debug":
            std::cout<<"Enter Debug"<<std::endl;
            break;
        case "/roll":
            std::cout<<"Roll Menu placeholder"<<std::endl;
            break;
        case "Option 3":
            std::cout<<"It pressed number 3"<<std::endl;
            break;
        default:
            std::cout<<"Input:"<< response <<std::endl;
            break;
        }
        }*/
}
int main()
{
    introduction();
    while (true){
            clientinput();
    }
    return 0;
}

#include "Morse.h"

class Translator
{
private:
    Morse mor;
    void action(char*);
public:
    Translator(int pin);
    Translator();
    ~Translator();
    void translate(char);
    void translateword(char*);
};

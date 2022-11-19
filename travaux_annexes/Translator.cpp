#include "Translator.h"

Translator::Translator(int pin)
{
    mor = Morse(pin);
}

Translator::Translator()
{
    mor = Morse();
}

Translator::~Translator()
{
}

void Translator::translate(char letter)
{
    switch (letter)
    {
    case 'a':
        action(".-");
        break;
    case 'b':
        action("-...");
        break;
    case 'c':
        action("-.-.");
        break;
    case 'd':
        action("-..");
        break;
    case 'e':
        action(".");
        break;
    case 'f':
        action("..-.");
        break;
    case 'g':
        action("--.");
        break;
    case 'h':
        action("....");
        break;
    case 'i':
        action("..");
        break;
    case 'j':
        action(".---");
        break;
    case 'k':
        action("-.-");
        break;
    case 'l':
        action(".-..");
        break;
    case 'm':
        action("--");
        break;
    case 'n':
        action("-.");
        break;
    case 'o':
        action("---");
        break;
    case 'p':
        action(".--.");
        break;
    case 'q':
        action("--.-");
        break;
    case 'r':
        action(".-.");
        break;
    case 's':
        action("...");
        break;
    case 't':
        action("-");
        break;
    case 'u':
        action("..-");
        break;
    case 'v':
        action("...-");
        break;
    case 'w':
        action(".--");
        break;
    case 'x':
        action("-..-");
        break;
    case 'y':
        action("-.--");
        break;
    case 'z':
        action("--..");
        break;
    case '0':
        action("-----");
        break;
    case '1':
        action(".----");
        break;
    case '2':
        action("..---");
        break;
    case '3':
        action("...--");
        break;
    case '4':
        action("....-");
        break;
    case '5':
        action(".....");
        break;
    case '6':
        action("-....");
        break;
    case '7':
        action("--...");
        break;
    case '8':
        action("---..");
        break;
    case '9':
        action("----.");
        break;
    case ' ':
        action(" ");
        break;
    default:
        break;
    }
}

void Translator::action(char *morse)
{
    int i = 0;
    while (morse[i] != '\0')
    {
        if (morse[i] == '.')
        {
            mor.dot();
        }
        else if (morse[i] == '-')
        {
            mor.dash();
        }
        else if (morse[i] == ' ')
        {
            mor.space();
        }
        i++;
    }
    mor.space();
}

void Translator::translateword(char *word)
{
    int i = 1;
    while (word[i] != '\0')
    {
        if (word[i] == '0')
        {
            mor.space();
        }
        else
        {
            translate(word[i]);
        }
        i++;
    }
}
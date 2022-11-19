class Morse
{
private:
    int _pin;
    void (*queue_function[100])();
    // void* queue_function;
    int* queue_time;
public:
    Morse(int pin);
    Morse();
    ~Morse();
    int TIME_DOT = 250;
    void dot();
    void dash();
    void space();
};

#define LEN_LIST 222

class Morse
{
private:
    int len_list;
    short unsigned int _pin;
    void (*queue_function[LEN_LIST])(short unsigned int);
    short unsigned int *queue_pin[LEN_LIST];
    unsigned int *queue_time[LEN_LIST];
    void addaction(void (*function)(short unsigned int), short unsigned int *pin, int time);
    unsigned int last_time_queue;
public:
    Morse(int pin);
    Morse();
    ~Morse();
    int TIME_DOT = 250;
    void dot();
    void dash();
    void little_space();
    void space();
    void makeaction();
};

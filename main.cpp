#include<iostream>
#include<fstream>
#include<sstream>
#include<string>
#include<vector>
using namespace std;

struct TurbineReading {
    string datetime;
    double rotor_speed, generator_speed, generator_temperature, wind_speed, power_output, relative_wind_direction, supply_voltage, blade_pitch_deg, yaw_offset;
    int turbine_status;
};

int main() {
    ifstream file("mock_turbine_dataset.csv");

    if (!file.is_open()) {
        cout << "Could not open file!" << endl;
        return 1;
    }

    string line;
    getline(file, line);
    cout << "Header: " << line << endl;

    while (getline(file, line)) {
    stringstream ss(line);
    string field;
        while (getline(ss, field, ',')) {
            cout << field << endl;
        }
    }
return 0;     
}

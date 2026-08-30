#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
using namespace std;

struct TurbineRecord {
    string logTime;
    double windspeed;
    double rpm;
    double powerOut;
    double t1;
    int turbineStatus;
    int gridStatus;
};

bool hasBit(int status, int bit) {
    return (status & bit) != 0;
}

int main() {
    ifstream file("swt_august_2022_final.csv");

    if (!file.is_open()) {
        cout << "Error... Could not open file" << endl;
        return 1;
    }

    string line;
    getline(file, line); // skip header

    vector<TurbineRecord> records;

    while (getline(file, line)) {
        stringstream ss(line);
        string field;
        vector<string> row;

        while (getline(ss, field, ';')) {
            row.push_back(field);
        }

        TurbineRecord rec;
        rec.logTime = row[0];
        rec.windspeed = stod(row[1]);
        rec.rpm = stod(row[2]);
        rec.powerOut = stod(row[7]);
        rec.t1 = stod(row[9]);
        rec.turbineStatus = stoi(row[14]);
        rec.gridStatus = stoi(row[15]);

        records.push_back(rec);
    }

    file.close();

    cout << "Loaded " << records.size() << " records." << endl;
    return 0;
}

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
    double t3;
    int turbineStatus;
    int gridStatus;
};

bool hasBit(int status, int bit) {
    return (status & bit) != 0;
}

bool isValid(TurbineRecord rec) {
    if (rec.windspeed < 0 || rec.windspeed > 25) {
        return false;
    }
    if (rec.rpm < 0) {
        return false;
    }
    if (rec.powerOut < 0) {
        return false;
    }
    if (rec.t1 < -10 || rec.t1 > 60) {
        return false;
    }
    return true;
}

bool checkWindPowerMismatch(TurbineRecord rec) {
    bool alreadyIdle = (rec.turbineStatus == 1 || rec.turbineStatus == 3 ||
                         rec.turbineStatus == 33 || rec.turbineStatus == 35);

    if (rec.windspeed >= 4 && rec.powerOut < 50 && !alreadyIdle) {
        return true; // fault detected
    }
    return false;
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
        rec.t3 = stod(row[11]);
        rec.turbineStatus = stoi(row[14]);
        rec.gridStatus = stoi(row[15]);

        if (isValid(rec)) {
            records.push_back(rec);
        }
    }

    file.close();

    cout << "Loaded " << records.size() << " records." << endl;
    return 0;
}

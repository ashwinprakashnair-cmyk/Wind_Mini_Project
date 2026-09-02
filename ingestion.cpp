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

bool tryStod(const string& s, double& out) {
    try { out = stod(s); return true; }
    catch (...) { return false; }
}

bool tryStoi(const string& s, int& out) {
    try { out = stoi(s); return true; }
    catch (...) { return false; }
}

int main() {
    ifstream file("swt_august_2022_final.csv");
    if (!file.is_open()) {
        cout << "Error... Could not open file" << endl;
        return 1;
    }

    string line;
    getline(file, line); // skip header

    int skippedCount = 0;
    vector<TurbineRecord> records;

    while (getline(file, line)) {
        stringstream ss(line);
        string field;
        vector<string> row;

        while (getline(ss, field, ';')) {
            row.push_back(field);
        }

        if (row.size() < 16) {
            skippedCount++;
            continue;
        }

        TurbineRecord rec;
        rec.logTime = row[0];

        bool ok = true;
        ok = ok && tryStod(row[1], rec.windspeed);
        ok = ok && tryStod(row[2], rec.rpm);
        ok = ok && tryStod(row[7], rec.powerOut);
        ok = ok && tryStod(row[9], rec.t1);
        ok = ok && tryStod(row[11], rec.t3);
        ok = ok && tryStoi(row[14], rec.turbineStatus);
        ok = ok && tryStoi(row[15], rec.gridStatus);

        if (!ok) {
            skippedCount++;
            continue;
        }

        if (isValid(rec)) {
            records.push_back(rec);
        } else {
            skippedCount++;
        }
    }

    file.close();
    cout << "Loaded " << records.size() << " records, skipped " << skippedCount << " rows." << endl;
    return 0;
}

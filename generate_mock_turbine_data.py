"""
generate_mock_turbine_data.py

Generates a synthetic (mock) wind-turbine SCADA dataset, MODELED ON the real
Aventa AV-7 (6kW) IET-OST Research Wind Turbine dataset (Barber, Hammer &
Marykovskiy, 2025, Zenodo, https://doi.org/10.5281/zenodo.16276333).

This is NOT real recorded data. Value ranges per turbine_status were derived
from patterns observed in the real dataset (see project notes). The purpose
is to demonstrate full turbine_status coverage (all 14 documented states)
for testing search/sort/segmentation logic in the C++ mini-project, since
real-world data samples rarely contain more than a handful of rows for the
rare transitional states (0-7, 11, 12).

Output: mock_turbine_dataset.csv
Columns match the real dataset schema exactly:
datetime, rotor_speed, generator_speed, generator_temperature, wind_speed,
power_output, relative_wind_direction, supply_voltage, blade_pitch_deg,
turbine_status, yaw_offset
"""

import csv
import random
from datetime import datetime, timedelta

random.seed(42)  # reproducible output

# ---------------------------------------------------------------------
# Status code definitions (from the official metadata dictionary) and
# the natural order a turbine cycles through in a normal start-up ->
# generate -> shutdown day, plus an alarm/fault interruption.
# ---------------------------------------------------------------------
STATUS_SEQUENCE = [
    (0,  "Initialize system",              20),
    (1,  "Feathered position search 1",    15),
    (2,  "Feathered position search 2",    15),
    (3,  "Feathered position 1",           10),
    (4,  "Function test 1",                20),
    (5,  "Function test 2",                20),
    (6,  "Feathered position 2",           10),
    (7,  "Standby position 1",             60),
    (8,  "Standby position 2",             60),
    (9,  "Standby position 3",             60),
    (10, "Power operation",              3600),   # main generation block (1 hr)
    (13, "Alarm - fault condition",        300),   # fault interrupts generation
    (12, "Shut down",                        5),   # very brief, per metadata (<25rpm)
    (9,  "Standby position 3",             120),   # returns to standby after fault
    (10, "Power operation",              1800),   # resumes generation
    (11, "High wind shutdown",             400),   # high wind event
    (12, "Shut down",                        5),
    (8,  "Standby position 2",             200),   # ends the day in standby
]

# Approximate value ranges per status, grounded in real observed stats:
#   status 8/9  -> rotor ~2-19 RPM, gen ~50-250 RPM, power ~0, wind low-moderate
#   status 10   -> rotor ~7-70 RPM, gen scales with rotor, power scales with wind
#   status 13   -> rotor ~7-25 RPM (still spinning on inertia), power ~0
#   status 11   -> high wind, blades feathering, power drops despite high wind
#   status 0-7,12 -> transitional/near-zero, brief
RANGES = {
    0:  dict(rotor=(0, 1),     gen=(0, 5),     temp=(5, 8),   wind=(0, 3),  power=(0, 0),      pitch=(35, 38)),
    1:  dict(rotor=(0, 2),     gen=(0, 10),    temp=(5, 8),   wind=(0, 3),  power=(0, 0),      pitch=(30, 40)),
    2:  dict(rotor=(0, 3),     gen=(0, 15),    temp=(5, 8),   wind=(0, 3),  power=(0, 0),      pitch=(25, 35)),
    3:  dict(rotor=(0, 2),     gen=(0, 10),    temp=(5, 8),   wind=(0, 3),  power=(0, 0),      pitch=(35, 38)),
    4:  dict(rotor=(1, 5),     gen=(5, 30),    temp=(6, 9),   wind=(0, 3),  power=(0, 0.1),    pitch=(20, 30)),
    5:  dict(rotor=(1, 6),     gen=(5, 35),    temp=(6, 9),   wind=(0, 3),  power=(0, 0.1),    pitch=(20, 30)),
    6:  dict(rotor=(0, 2),     gen=(0, 10),    temp=(6, 9),   wind=(0, 3),  power=(0, 0),      pitch=(35, 38)),
    7:  dict(rotor=(2, 12),    gen=(50, 180),  temp=(6, 10),  wind=(1, 4),  power=(0, 0.05),   pitch=(14, 20)),
    8:  dict(rotor=(6, 17),    gen=(80, 250),  temp=(6, 10),  wind=(1, 4),  power=(0, 0.1),    pitch=(14, 18)),
    9:  dict(rotor=(2, 19),    gen=(50, 260),  temp=(6, 10),  wind=(1, 5),  power=(0, 0.1),    pitch=(14, 18)),
    10: dict(rotor=(7, 70),    gen=(260, 900), temp=(20, 32), wind=(3, 12), power=(0.5, 6.2),  pitch=(0, 14)),
    11: dict(rotor=(20, 40),   gen=(300, 600), temp=(22, 30), wind=(12, 20),power=(1.0, 3.0),  pitch=(60, 85)),
    12: dict(rotor=(15, 25),   gen=(100, 300), temp=(18, 25), wind=(3, 10), power=(0, 0.3),    pitch=(30, 37)),
    13: dict(rotor=(7, 25),    gen=(80, 300),  temp=(15, 28), wind=(2, 9),  power=(0, 0),      pitch=(20, 40)),
}


def random_in(rng):
    return round(random.uniform(rng[0], rng[1]), 2)


def generate_dataset(start_time, output_path):
    rows = []
    current_time = start_time

    for status, label, duration_sec in STATUS_SEQUENCE:
        r = RANGES[status]
        for _ in range(duration_sec):
            rotor = random_in(r["rotor"])
            gen = random_in(r["gen"])
            temp = random_in(r["temp"])
            wind = random_in(r["wind"])
            power = random_in(r["power"])
            pitch = random_in(r["pitch"])
            wind_dir = random.randint(-30, 30)
            supply_v = round(random.uniform(27.5, 27.9), 1)
            yaw = 0

            rows.append([
                current_time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3] + "+05:30",
                rotor, gen, temp, wind, power, wind_dir, supply_v, pitch, status, yaw
            ])
            current_time += timedelta(seconds=1)

    header = ["datetime", "rotor_speed", "generator_speed", "generator_temperature",
              "wind_speed", "power_output", "relative_wind_direction",
              "supply_voltage", "blade_pitch_deg", "turbine_status", "yaw_offset"]

    with open(output_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)

    return len(rows)


if __name__ == "__main__":
    start = datetime(2025, 1, 15, 6, 0, 0)
    count = generate_dataset(start, "mock_turbine_dataset.csv")
    print(f"Generated {count} rows -> mock_turbine_dataset.csv")

    # quick summary of status distribution
    from collections import Counter
    with open("mock_turbine_dataset.csv") as f:
        reader = csv.DictReader(f)
        statuses = [int(row["turbine_status"]) for row in reader]
    print("\nStatus distribution:")
    for code, cnt in sorted(Counter(statuses).items()):
        print(f"  Status {code}: {cnt} rows")

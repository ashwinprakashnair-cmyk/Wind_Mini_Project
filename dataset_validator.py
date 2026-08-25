import numpy as np
import pandas as pd

# 1. Ingest Dataset
df = pd.read_csv("v2_final_cleaned.csv")

# 2. Derive Constant for Theoretical Wind Power
# Theoretical Formula: P_theoretical = 0.5 * rho * A * v^3
# Empirical constant k = 0.5 * rho * A calculated from the dataset's cp_estimated channel:
k = 0.08005259137721873

# Compute Theoretical Power & Calculated Cp
df["p_theoretical"] = k * (df["wind_speed"] ** 3)
df["cp_calculated"] = df["power_output"] / df["p_theoretical"]

# 3. Overall Metric Calculations
total_records = len(df)
mean_actual_power = df["power_output"].mean()
mean_theoretical_power = df["p_theoretical"].mean()
p_rated = df[df["operating_regime"] == "rated_capped"]["power_output"].max()

capacity_factor = mean_actual_power / p_rated
overall_efficiency = mean_actual_power / mean_theoretical_power
below_rated_cp_mean = df[df["operating_regime"] == "below_rated"][
    "cp_calculated"
].mean()
below_rated_cp_max = df[df["operating_regime"] == "below_rated"][
    "cp_calculated"
].max()

# 4. Mechanical Kinematics Verification
# Check relation: Generator Speed / Rotor Speed == gear_ratio_calc
df["gear_ratio_actual"] = df["generator_speed"] / df["rotor_speed"]
gear_discrepancies = np.sum(
    np.abs(df["gear_ratio_calc"] - df["gear_ratio_actual"]) > 0.01
)

# 5. Physics & Operational Anomaly Checks
betz_violations = df[df["cp_calculated"] > 0.593]  # Betz Limit = 16/27 ~ 0.593
cutin_violations = df[(df["wind_speed"] < 3.0) & (df["power_output"] > 0)]
cutout_violations = df[(df["wind_speed"] > 25.0) & (df["power_output"] > 0)]
overpower_violations = df[df["power_output"] > p_rated]
zero_power_anomalies = df[(df["wind_speed"] >= 3.0) & (df["power_output"] == 0)]

# Combine total anomalous rows
total_anomalies = len(
    df[
        (df["cp_calculated"] > 0.593)
        | ((df["wind_speed"] < 3.0) & (df["power_output"] > 0))
        | ((df["wind_speed"] > 25.0) & (df["power_output"] > 0))
        | (df["power_output"] > p_rated)
        | ((df["wind_speed"] >= 3.0) & (df["power_output"] == 0))
    ]
)

# 6. Accuracy Score Computation
dataset_accuracy = ((total_records - total_anomalies) / total_records) * 100

# 7. Display Results
print("=" * 50)
print("     WIND TURBINE SCADA VERIFICATION REPORT     ")
print("=" * 50)
print(f"Total Records Analyzed : {total_records}")
print(
    f"Wind Speed Range       : {df['wind_speed'].min():.2f} m/s - {df['wind_speed'].max():.2f} m/s"
)
print(f"Rated Capacity (P_rated): {p_rated:.2f} kW")
print(f"Mean Active Power Output: {mean_actual_power:.4f} kW")
print(f"Mean Theoretical Power : {mean_theoretical_power:.4f} kW")
print("-" * 50)
print(f"Capacity Factor (CF)   : {capacity_factor * 100:.2f}%")
print(f"Overall Efficiency     : {overall_efficiency * 100:.2f}%")
print(f"Mean Cp (Below Rated)  : {below_rated_cp_mean:.4f}")
print(f"Max Cp (Below Rated)   : {below_rated_cp_max:.4f}")
print("-" * 50)
print("PHYSICS & ANOMALY BREAKDOWN:")
print(f"  - Betz Violations (Cp > 0.593)  : {len(betz_violations)}")
print(f"  - Ghost Power (v < 3 m/s)       : {len(cutin_violations)}")
print(f"  - Storm Violations (v > 25 m/s) : {len(cutout_violations)}")
print(f"  - Overpower Excursions          : {len(overpower_violations)}")
print(f"  - Gearbox Kinematic Errors      : {gear_discrepancies}")
print(f"  - Zero Power at v >= 3 m/s      : {len(zero_power_anomalies)}")
print("-" * 50)
print(f"FINAL DATASET ACCURACY SCORE      : {dataset_accuracy:.4f}%")
print("=" * 50)

# Display specific details for the 1 flagged anomaly (spin-up lag)
if len(zero_power_anomalies) > 0:
    print("\nFlagged Anomaly Detail:")
    print(
        zero_power_anomalies[
            [
                "datetime",
                "wind_speed",
                "power_output",
                "operating_regime",
                "blade_pitch_deg",
            ]
        ]
    )

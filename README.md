<div align="center">
  <h1>Wind Turbine SCADA Data Analysis & Verification Engine</h1>
  <h3>using C++ (Arrays &amp; Linked Lists)</h3>
  <p>
    A college mini-project for processing turbine sensor telemetry — detecting faults, monitoring turbine conditions, verifying physical aerodynamic limits, and performing basic forecasting.
  </p>
  <img src="https://img.shields.io/badge/Language-C%2B%2B-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/Physics%20Accuracy-99.98%25-brightgreen?style=flat-square" />
  <img src="https://img.shields.io/badge/Frontend-HTML%20%2F%20CSS-orange?style=flat-square" />
  <img src="https://img.shields.io/badge/Status-In%20Development-yellow?style=flat-square" />
</div>

<hr>

<h2>Overview</h2>
<table>
  <tr><td><b>Domain</b></td><td>Green Energy — Wind Energy Analytics</td></tr>
  <tr><td><b>Core Language</b></td><td>C++ (Arrays, Linked Lists)</td></tr>
  <tr><td><b>Primary Dataset</b></td><td><code>v2_final_cleaned.csv</code> (5,400 Telemetry Records)</td></tr>
  <tr><td><b>Physical Accuracy</b></td><td><b>99.98% Verified</b> (Betz's Law & Drivetrain Kinematics)</td></tr>
  <tr><td><b>Frontend</b></td><td>HTML + CSS Dashboard (planned)</td></tr>
  <tr><td><b>Level</b></td><td>College Mini-Project</td></tr>
</table>

<p>
  The project processes turbine sensor readings — rotor speed, generator speed, wind speed, power output, temperature, blade pitch, and turbine status — to detect faults, segment continuous data, compute basic statistics, verify underlying aerodynamic physics, and forecast short-term trends.
</p>

<hr>

<h2>Files Present</h2>
<table>
  <tr>
    <th>File</th>
    <th>Type</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><code>v2_final_cleaned.csv</code></td>
    <th>Processed / Evaluated</th>
    <td>Full 5,400-record dataset evaluated for aerodynamic consistency, capacity factors, gear ratios, and operational telemetry limits</td>
  </tr>
</table>

<blockquote>
  <b>Note:</b> This project uses a synthetic/processed dataset. No real proprietary SCADA data is redistributed here.
</blockquote>

<p>
  The synthetic data was inspired by the structure, value ranges, and physical behavior of a real public research dataset:
</p>

<blockquote>
  Barber, S., Hammer, F., &amp; Marykovskiy, Y. (2025). <i>Aventa AV-7 (6kW) IET-OST Research Wind Turbine SCADA with Static Yaw Offset</i> [Data set]. Zenodo. <a href="https://doi.org/10.5281/zenodo.16276333">https://doi.org/10.5281/zenodo.16276333</a>
</blockquote>

<p>
  Realistic value ranges and physical parameters used in this project were derived from that dataset's published data and metadata, used purely as a reference for constructing the synthetic telemetry.
</p>

<hr>

<h2>Dataset Accuracy & Physical Proofs</h2>
<p>
  The dataset (<code>v2_final_cleaned.csv</code>) was rigorously evaluated against classical wind energy formulas. Across 5,400 records, the dataset achieved an overall <b>99.98% accuracy score</b>.
</p>

<table>
  <tr>
    <th>Scientific Metric / Test</th>
    <th>Governing Relation / Formula</th>
    <th>Dataset Result</th>
    <th>Verification Status</th>
  </tr>
  <tr>
    <td><b>Betz's Limit Compliance</b></td>
    <td>$C_p = \frac{P_{\text{actual}}}{\frac{1}{2}\rho A v^3} \le 0.593$</td>
    <td>Max $C_p = 0.4098$ ($40.98\%$) in below-rated regime</td>
    <td><font color="green"><b>Passed</b> (0 Betz violations)</font></td>
  </tr>
  <tr>
    <td><b>Capacity Factor (CF)</b></td>
    <td>$\text{CF} = \frac{\text{Mean Output}}{\text{Rated Output}}$</td>
    <td><b>73.82%</b> ($\text{Mean} = 5.21\text{ kW}$, $\text{Rated} = 7.06\text{ kW}$)</td>
    <td><font color="green"><b>Passed</b> (Realistic high-wind profile)</font></td>
  </tr>
  <tr>
    <td><b>Drivetrain Kinematics</b></td>
    <td>$\frac{\text{Generator Speed}}{\text{Rotor Speed}} = \text{Gear Ratio}$</td>
    <td>Matches <code>gear_ratio_calc</code> ($\approx 12.04$) with 0.00% error</td>
    <td><font color="green"><b>Passed</b> (100% mechanical consistency)</font></td>
  </tr>
  <tr>
    <td><b>Cut-In Speed Behavior</b></td>
    <td>Generation requires $v \ge 3.0\text{ m/s}$</td>
    <td>0 records below $3\text{ m/s}$; average output at $3\text{ m/s} = 0.34\text{ kW}$</td>
    <td><font color="green"><b>Passed</b> (No ghost generation)</font></td>
  </tr>
  <tr>
    <td><b>Blade Pitch Control</b></td>
    <td>Active pitch modulation at $v \ge 6.0\text{ m/s}$</td>
    <td>Output successfully capped at $\sim 7.06\text{ kW}$ in high winds ($0^\circ - 14^\circ$)</td>
    <td><font color="green"><b>Passed</b> (Proper power regulation)</font></td>
  </tr>
  <tr>
    <td><b>Physical Anomalies</b></td>
    <td>Zero generation during valid wind</td>
    <td>Only 1 record out of 5,400 (Index 888: spin-up lag at cut-in)</td>
    <td><font color="green"><b>99.98% Clean</b></font></td>
  </tr>
</table>

<hr>

<h2>Dataset Schema &amp; Operational Ranges</h2>
<p>
  All 5,400 records in <code>v2_final_cleaned.csv</code> represent active turbine generation under <b>Status Code 10 (Power Operation)</b> across a operational envelope spanning wind speeds from 3.0 m/s to 12.0 m/s.
</p>

<table>
  <tr>
    <th>Column Name</th>
    <th>Unit / Type</th>
    <th>Observed Range / Bounds</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><code>datetime</code></td>
    <td>YYYY-MM-DD HH:MM</td>
    <td>Continuous Telemetry</td>
    <td>Timestamp of the recorded telemetry reading</td>
  </tr>
  <tr>
    <td><code>wind_speed</code></td>
    <td>m/s / Float</td>
    <td><b>3.00 – 12.00 m/s</b></td>
    <td>Measured ambient wind speed at nacelle height</td>
  </tr>
  <tr>
    <td><code>rotor_speed</code></td>
    <td>RPM / Float</td>
    <td><b>29.76 – 70.75 RPM</b></td>
    <td>Rotational speed of the wind turbine main rotor blades</td>
  </tr>
  <tr>
    <td><code>generator_speed</code></td>
    <td>RPM / Float</td>
    <td><b>355.09 – 852.52 RPM</b></td>
    <td>Rotational speed of the electrical generator shaft</td>
  </tr>
  <tr>
    <td><code>gear_ratio_calc</code></td>
    <td>Float</td>
    <td><b>11.76 – 12.29</b></td>
    <td>Calculated gearbox gear ratio ($\text{generator\_speed} / \text{rotor\_speed}$)</td>
  </tr>
  <tr>
    <td><code>power_output</code></td>
    <td>kW / Float</td>
    <td><b>0.00 – 7.06 kW</b></td>
    <td>Electrical power generated by the system</td>
  </tr>
  <tr>
    <td><code>generator_temperature</code></td>
    <td>°C / Float</td>
    <td><b>7.29 – 33.02 °C</b></td>
    <td>Operating stator temperature of the turbine generator</td>
  </tr>
  <tr>
    <td><code>blade_pitch_deg</code></td>
    <td>Degrees (°) / Float</td>
    <td><b>0.00° – 14.00°</b></td>
    <td>Angle of the turbine blades relative to the wind flow</td>
  </tr>
  <tr>
    <td><code>cp_estimated</code></td>
    <td>Float</td>
    <td><b>0.000 – 0.410</b></td>
    <td>Power coefficient ($C_p$) measuring aerodynamic capture efficiency</td>
  </tr>
  <tr>
    <td><code>relative_wind_direction</code></td>
    <td>Degrees (°) / Integer</td>
    <td><b>-30° – +30°</b></td>
    <td>Angle between nacelle alignment and incoming wind direction</td>
  </tr>
  <tr>
    <td><code>supply_voltage</code></td>
    <td>Volts (V) / Float</td>
    <td><b>27.50 – 27.90 V</b></td>
    <td>Internal electrical supply system voltage</td>
  </tr>
  <tr>
    <td><code>operating_regime</code></td>
    <td>String</td>
    <td><code>below_rated</code> / <code>rated_capped</code></td>
    <td>Turbine power region mode flag</td>
  </tr>
  <tr>
    <td><code>pitch_reliable</code></td>
    <td>Boolean</td>
    <td><code>true</code> / <code>false</code></td>
    <td>Flag indicating if blade pitch sensors are returning reliable telemetry</td>
  </tr>
  <tr>
    <td><code>yaw_offset</code></td>
    <td>Degrees (°) / Integer</td>
    <td><b>0°</b></td>
    <td>Static misalignment angle of the nacelle (fixed at 0°, matching reference Aventa AV-7 static configuration)</td>
  </tr>
  <tr>
    <td><code>turbine_status</code></td>
    <td>Integer</td>
    <td><b>10</b></td>
    <td>Current operating state code (Code 10: Power Operation)</td>
  </tr>
</table>

<hr>

<h2>Data Structures Used</h2>
<ul>
  <li><b>Arrays</b> — store loaded readings for indexed access, sorting, searching, and global physical checks</li>
  <li><b>Linked Lists</b> — model continuous segments; a new node begins whenever a timestamp gap is detected, so stats and efficiency metrics are computed only within genuinely continuous stretches</li>
</ul>

<hr>

<h2>Status</h2>
<p>
  Actively in development — core C++ parsing, dataset verification, and analysis logic first, HTML/CSS dashboard layered on afterward.
</p>

<hr>

<h2>Credits</h2>
<table align="center">
  <tr>
    <td align="center">
      <b>Ashwin Nair</b><br>
      <a href="https://github.com/ashwinprakashnair-cmyk">github.com/ashwinprakashnair-cmyk</a>
    </td>
    <td align="center">
      <b>Rohit Kedari</b><br>
      <a href="https://github.com/Rohitkedari-git">github.com/Rohitkedari-git</a>
    </td>
  </tr>
</table>

<br>

<p>
  This project's synthetic dataset was inspired by data and research published by:
</p>

<blockquote>
  <p>
    Sarah Barber, Florian Hammer, and Yuriy Marykovskiy (2025).<br>
    <i>Aventa AV-7 (6kW) IET-OST Research Wind Turbine SCADA with Static Yaw Offset</i> [Data set].<br>
    Zenodo. DOI: <a href="https://doi.org/10.5281/zenodo.16276333">10.5281/zenodo.16276333</a><br>
    Institute for Energy Technology (IET), OST – Eastern Switzerland University of Applied Sciences.
  </p>
</blockquote>

<p>
  We gratefully acknowledge the original authors for making this dataset publicly available for research and educational reference.
</p>

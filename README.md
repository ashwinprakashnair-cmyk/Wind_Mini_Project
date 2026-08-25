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
  <tr><td><b>Physical Accuracy</b></td><td><b>99.98% Verified</b> (Betz's Law & Gear Ratio Kinematics)</td></tr>
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
    <td>Full 5,400-record dataset evaluated for aerodynamic consistency, capacity factors, and gear ratios</td>
  </tr>
  <tr>
    <td><code>mock_turbine_dataset.csv</code></td>
    <td>Synthetic Reference</td>
    <td>Generated baseline data covering all 14 turbine operating states</td>
  </tr>
</table>

<blockquote>
  <b>Note:</b> This project uses a synthetic/processed dataset. No real proprietary SCADA data is redistributed here.
</blockquote>

<p>
  The synthetic data was inspired by the structure, value ranges, and turbine status codes of a real public research dataset:
</p>

<blockquote>
  Barber, S., Hammer, F., &amp; Marykovskiy, Y. (2025). <i>Aventa AV-7 (6kW) IET-OST Research Wind Turbine SCADA with Static Yaw Offset</i> [Data set]. Zenodo. <a href="https://doi.org/10.5281/zenodo.16276333">https://doi.org/10.5281/zenodo.16276333</a>
</blockquote>

<p>
  Realistic value ranges and turbine status code definitions used in this project were derived from that dataset's published data and metadata, used purely as a reference for building the synthetic dataset.
</p>

<hr>

<h2>Dataset Accuracy & Physical Proofs</h2>
<p>
  The primary dataset (<code>v2_final_cleaned.csv</code>) was rigorously evaluated against classical wind energy formulas. Across 5,400 records, the dataset achieved an overall <b>99.98% accuracy score</b>.
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
    <td>Active pitch pitching at $v \ge 6.0\text{ m/s}$</td>
    <td>Output successfully capped at $\sim 7.06\text{ kW}$ in high winds</td>
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

<h2>Dataset Schema &amp; Parameters</h2>
<table>
  <tr>
    <th>Column Name</th>
    <th>Unit / Type</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><code>datetime</code></td>
    <td>YYYY-MM-DD HH:MM</td>
    <td>Timestamp of the recorded telemetry reading</td>
  </tr>
  <tr>
    <td><code>rotor_speed</code></td>
    <td>RPM / Float</td>
    <td>Rotational speed of the wind turbine main rotor blades</td>
  </tr>
  <tr>
    <td><code>generator_speed</code></td>
    <td>RPM / Float</td>
    <td>Rotational speed of the electrical generator shaft</td>
  </tr>
  <tr>
    <td><code>gear_ratio_calc</code></td>
    <td>Float</td>
    <td>Calculated gearbox gear ratio ($\text{generator\_speed} / \text{rotor\_speed}$)</td>
  </tr>
  <tr>
    <td><code>generator_temperature</code></td>
    <td>°C / Float</td>
    <td>Operating temperature of the turbine generator</td>
  </tr>
  <tr>
    <td><code>wind_speed</code></td>
    <td>m/s / Float</td>
    <td>Measured ambient wind speed at nacelle height</td>
  </tr>
  <tr>
    <td><code>power_output</code></td>
    <td>kW / Float</td>
    <td>Electrical power generated by the system</td>
  </tr>
  <tr>
    <td><code>operating_regime</code></td>
    <td>String</td>
    <td>Turbine power region (<code>below_rated</code> vs <code>rated_capped</code>)</td>
  </tr>
  <tr>
    <td><code>pitch_reliable</code></td>
    <td>Boolean</td>
    <td>Flag indicating if blade pitch sensors are returning reliable data</td>
  </tr>
  <tr>
    <td><code>cp_estimated</code></td>
    <td>Float</td>
    <td>Power coefficient ($C_p$) measuring theoretical wind capture efficiency</td>
  </tr>
  <tr>
    <td><code>relative_wind_direction</code></td>
    <td>Degrees (°) / Float</td>
    <td>Angle between nacelle alignment and incoming wind direction</td>
  </tr>
  <tr>
    <td><code>supply_voltage</code></td>
    <td>Volts (V) / Float</td>
    <td>Internal electrical supply system voltage</td>
  </tr>
  <tr>
    <td><code>blade_pitch_deg</code></td>
    <td>Degrees (°) / Float</td>
    <td>Angle of the turbine blades relative to the wind flow</td>
  </tr>
  <tr>
    <td><code>turbine_status</code></td>
    <td>Integer (0–13)</td>
    <td>Current operating state code (see status mapping table below)</td>
  </tr>
  <tr>
    <td><code>yaw_offset</code></td>
    <td>Degrees (°) / Float</td>
    <td>Static or dynamic misalignment angle of the turbine nacelle (fixed at 0° in this synthetic dataset, matching the static yaw offset configuration of the reference Aventa AV-7 dataset)</td>
  </tr>
</table>

<hr>

<h2>Turbine Status Codes</h2>
<table>
  <tr><th>Code</th><th>Meaning</th></tr>
  <tr><td align="center">0</td><td>Initialize system</td></tr>
  <tr><td align="center">1</td><td>Feathered position search 1</td></tr>
  <tr><td align="center">2</td><td>Feathered position search 2</td></tr>
  <tr><td align="center">3</td><td>Feathered position 1</td></tr>
  <tr><td align="center">4</td><td>Function test 1</td></tr>
  <tr><td align="center">5</td><td>Function test 2</td></tr>
  <tr><td align="center">6</td><td>Feathered position 2</td></tr>
  <tr><td align="center">7</td><td>Standby position 1</td></tr>
  <tr><td align="center">8</td><td>Standby position 2</td></tr>
  <tr><td align="center">9</td><td>Standby position 3</td></tr>
  <tr><td align="center">10</td><td>Power operation</td></tr>
  <tr><td align="center">11</td><td>High wind shutdown</td></tr>
  <tr><td align="center">12</td><td>Shut down</td></tr>
  <tr><td align="center">13</td><td>Alarm / fault condition</td></tr>
</table>

<hr>

<h2>Synthetic Data Generation Ranges</h2>
<p>
  Each status code drives a distinct sensor behavior profile. The synthetic generator samples values within the following per-status ranges, chosen to reflect realistic turbine behavior at each operating state:
</p>

<table>
  <tr>
    <th>Code</th><th>Status</th><th>Rotor Speed (RPM)</th><th>Generator Speed (RPM)</th><th>Gen. Temp (°C)</th><th>Wind Speed (m/s)</th><th>Power Output (kW)</th><th>Blade Pitch (°)</th>
  </tr>
  <tr><td align="center">0</td><td>Initialize system</td><td>0–1</td><td>0–5</td><td>5–8</td><td>0–3</td><td>0</td><td>35–38</td></tr>
  <tr><td align="center">1</td><td>Feathered position search 1</td><td>0–2</td><td>0–10</td><td>5–8</td><td>0–3</td><td>0</td><td>30–40</td></tr>
  <tr><td align="center">2</td><td>Feathered position search 2</td><td>0–3</td><td>0–15</td><td>5–8</td><td>0–3</td><td>0</td><td>25–35</td></tr>
  <tr><td align="center">3</td><td>Feathered position 1</td><td>0–2</td><td>0–10</td><td>5–8</td><td>0–3</td><td>0</td><td>35–38</td></tr>
  <tr><td align="center">4</td><td>Function test 1</td><td>1–5</td><td>5–30</td><td>6–9</td><td>0–3</td><td>0–0.1</td><td>20–30</td></tr>
  <tr><td align="center">5</td><td>Function test 2</td><td>1–6</td><td>5–35</td><td>6–9</td><td>0–3</td><td>0–0.1</td><td>20–30</td></tr>
  <tr><td align="center">6</td><td>Feathered position 2</td><td>0–2</td><td>0–10</td><td>6–9</td><td>0–3</td><td>0</td><td>35–38</td></tr>
  <tr><td align="center">7</td><td>Standby position 1</td><td>2–12</td><td>50–180</td><td>6–10</td><td>1–4</td><td>0–0.05</td><td>14–20</td></tr>
  <tr><td align="center">8</td><td>Standby position 2</td><td>6–17</td><td>80–250</td><td>6–10</td><td>1–4</td><td>0–0.1</td><td>14–18</td></tr>
  <tr><td align="center">9</td><td>Standby position 3</td><td>2–19</td><td>50–260</td><td>6–10</td><td>1–5</td><td>0–0.1</td><td>14–18</td></tr>
  <tr><td align="center">10</td><td>Power operation</td><td>7–70</td><td>260–900</td><td>20–32</td><td>3–12</td><td>0.5–6.2</td><td>0–14</td></tr>
  <tr><td align="center">11</td><td>High wind shutdown</td><td>20–40</td><td>300–600</td><td>22–30</td><td>12–20</td><td>1.0–3.0</td><td>60–85</td></tr>
  <tr><td align="center">12</td><td>Shut down</td><td>15–25</td><td>100–300</td><td>18–25</td><td>3–10</td><td>0–0.3</td><td>30–37</td></tr>
  <tr><td align="center">13</td><td>Alarm / fault condition</td><td>7–25</td><td>80–300</td><td>15–28</td><td>2–9</td><td>0</td><td>20–40</td></tr>
</table>

<p>
  The remaining parameters are generated independently of status code:
</p>

<table>
  <tr><th>Column</th><th>Generation Method</th></tr>
  <tr><td><code>relative_wind_direction</code></td><td>Random integer, -30° to 30°</td></tr>
  <tr><td><code>supply_voltage</code></td><td>Random float, 27.5–27.9 V</td></tr>
  <tr>
  <td><code>yaw_offset</code></td>
  <td>Fixed at 0° — matches the static yaw offset configuration of the reference Aventa AV-7 dataset</td>
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

<div align="center">
  <h1>Urban Small Wind Turbine SCADA Data Analysis</h1>
  <h3>using C++ (Arrays & Linked Lists)</h3>
  <p>
    A college mini-project for processing real turbine sensor telemetry — detecting faults, monitoring turbine conditions, verifying physical electrical/aerodynamic behavior, and performing basic forecasting.
  </p>
  <img src="https://img.shields.io/badge/Language-C%2B%2B-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/Data-Real%20SCADA-brightgreen?style=flat-square" />
  <img src="https://img.shields.io/badge/Frontend-HTML%20%2F%20CSS-orange?style=flat-square" />
  <img src="https://img.shields.io/badge/Status-In%20Development-yellow?style=flat-square" />
</div>

<hr>

<h2>Overview</h2>
<table>
  <tr><td><b>Domain</b></td><td>Green Energy — Small Wind Turbine Analytics</td></tr>
  <tr><td><b>Core Language</b></td><td>C++ (Arrays, Linked Lists)</td></tr>
  <tr><td><b>Primary Dataset</b></td><td><code>swt_august_2022_final.csv</code> (35,903 Real Telemetry Records, 1-minute resolution)</td></tr>
  <tr><td><b>Data Type</b></td><td>Real-world SCADA data (not synthetic)</td></tr>
  <tr><td><b>Frontend</b></td><td>HTML + CSS Dashboard (planned)</td></tr>
  <tr><td><b>Level</b></td><td>College Mini-Project</td></tr>
</table>

<p>
  The project processes real turbine sensor readings — wind speed, RPM, DC/AC voltages, current, power output, temperatures, and bitmask status codes — to detect faults, segment continuous data, compute basic statistics, verify underlying electrical/aerodynamic physics, and forecast short-term trends.
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
    <td><code>swt_august_2022_final.csv</code></td>
    <th>Real / Cleaned / Trimmed</th>
    <td>35,903-record subset (August 2022, 1 month) of real Skystream 3.7 SCADA telemetry, trimmed to the 17 columns needed for this project and cleaned of 4 confirmed-corrupt rows</td>
  </tr>
</table>

<blockquote>
  <b>Note:</b> This project uses real, published SCADA data — not a synthetic approximation. The full source dataset spans January–December 2022 (369,731 records); August was selected as a representative one-month subset with the widest variety of operational status codes (19 distinct combinations: 10 Turbine status + 3 Grid status + 6 System status values — more than any other month).
</blockquote>

<p>
  Source dataset:
</p>

<blockquote>
  Bassi, W., Rodrigues, A. L., &amp; Sauer, I. L. (2023). <i>Operation SCADA Data of an Urban Small Wind Turbine in São Paulo, Brazil</i> [Data set]. Zenodo. <a href="https://doi.org/10.5281/zenodo.7348454">https://doi.org/10.5281/zenodo.7348454</a>. Licensed under <a href="https://creativecommons.org/licenses/by/4.0/">CC-BY-4.0</a>. Recorded from a Southwest Windpower / XZERES <b>Skystream 3.7</b> installed at the Institute of Energy and Environment, University of São Paulo.
</blockquote>

<p>
  Turbine specifications (rated power, rotor diameter, cut-in speed) used for physical validation below are the manufacturer's published Skystream 3.7 specs, cross-checked against the dataset's own <code>Power max</code> column (constant 2400W across 99.99% of raw records).
</p>

<hr>

<h2>Dataset Accuracy &amp; Physical Validation</h2>
<p>
  The dataset (<code>swt_august_2022_final.csv</code>) was checked against classical wind/electrical power formulas using the Skystream 3.7's published specs: <b>rated power 2.4 kW</b>, <b>rotor diameter 3.72 m</b> (swept area 10.87 m²), <b>cut-in wind speed ≈ 3.0–3.5 m/s</b>.
</p>

<table>
  <tr>
    <th>Scientific Metric / Test</th>
    <th>Governing Relation / Formula</th>
    <th>Dataset Result</th>
    <th>Verification Status</th>
  </tr>
  <tr>
    <td><b>Electrical Power Law</b></td>
    <td>Power out ≈ (Voltage L1 + Voltage L2) × Current out</td>
    <td>Implied voltage = 220.65 V ± 4.7 V (for rows with ≥ 200 W output) — stable and physically consistent. Ratio is unstable below 200 W due to division by small currents, not a data defect.</td>
    <td><font color="green"><b>Passed</b> (verified at meaningful output)</font></td>
  </tr>
  <tr>
    <td><b>Inverter Efficiency</b></td>
    <td>Power reg / Power out</td>
    <td>Mean = 1.0054 (± 0.016) for ≥ 200 W rows — near-lossless conversion, consistent with a well-tuned grid-tied inverter</td>
    <td><font color="green"><b>Passed</b></font></td>
  </tr>
  <tr>
    <td><b>Betz's Limit Compliance</b></td>
    <td>Cp = P_actual / (½ρAv³) ≤ 0.593</td>
    <td>4 of 17,762 non-zero-wind records (0.023%) marginally exceed Betz limit (Cp up to 0.692), all at low integer wind-speed readings (3–4 m/s) where the dataset's integer-only wind speed resolution amplifies error via the v³ term</td>
    <td><font color="orange"><b>99.98% Passed</b> (explained by wind-speed measurement resolution, not a physics violation)</font></td>
  </tr>
  <tr>
    <td><b>Cut-In Speed Behavior</b></td>
    <td>Generation requires v ≥ 3.0 m/s</td>
    <td>179 records show trace output below 3 m/s (max 16 W); all occur near the 3 m/s boundary and are consistent with rotor inertia carrying over between 1-minute samples.</td>
    <td><font color="green"><b>Passed</b> (physically explainable)</font></td>
  </tr>
  <tr>
    <td><b>Idle Coasting Behavior</b></td>
    <td>RPM &gt; 0 while Windspeed = 0</td>
    <td>510 records, all with RPM 5–17 (near-idle) and Power out = 0 — consistent with the rotor freewheeling to a stop in still air rather than a sensor fault</td>
    <td><font color="green"><b>Passed</b> (physically explainable)</font></td>
  </tr>
  <tr>
    <td><b>Rated Power Ceiling</b></td>
    <td>Output should not sustain above 2,400 W nameplate</td>
    <td>Max recorded: 1,927 W in August (below rated — August was a lower-wind month); full-year data shows only 11 of 369,731 rows briefly exceed 2,400 W, up to 3,713 W — realistic short-duration overshoot, not systemic capping</td>
    <td><font color="green"><b>Passed</b></font></td>
  </tr>
  <tr>
    <td><b>Known Data Corruption (pre-cleaning)</b></td>
    <td>Physically impossible sensor values</td>
    <td>4 rows removed from the raw 35,907-row August extract: 2 with corrupted Turbine status (value 33063, an implausible bitmask) and 2 with Power max = 0 (sensor init/calibration artifacts)</td>
    <td><font color="green"><b>Cleaned</b> (0.011% of rows removed)</font></td>
  </tr>
</table>

<hr>

<h2>Plain-Language Glossary</h2>
<p>For anyone in the room unfamiliar with the terms above:</p>
<ul>
  <li><b>Betz's Limit</b> — a hard physics ceiling: no wind turbine can ever convert more than 59.3% of the wind's energy into electricity, regardless of design.</li>
  <li><b>Cp (power coefficient)</b> — the turbine's real-time efficiency score: actual power produced ÷ max power theoretically available in that wind.</li>
  <li><b>Swept area</b> — the circular area the spinning blades cover (π × radius²); bigger blades capture more wind.</li>
  <li><b>Cut-in speed</b> — the minimum wind speed before the turbine generates any power at all.</li>
  <li><b>Freewheeling / coasting</b> — the rotor still spinning briefly from leftover momentum after wind drops, like a bike wheel spinning after you stop pedaling.</li>
  <li><b>L1 / L2 (phases)</b> — the two AC lines that together deliver grid power in this split-phase setup.</li>
  <li><b>Inverter</b> — the device that converts the turbine's raw DC output into clean AC power usable by the grid.</li>
  <li><b>Inverter efficiency ratio</b> — Power reg ÷ Power out; close to 1 means almost no energy is lost during conversion.</li>
  <li><b>Bitmask</b> — a way of packing multiple independent flags into one number using powers of 2 (1, 2, 4, 8, 16...), added together when several conditions are true at once. E.g. 33 = 32 + 1 = two conditions happening simultaneously.</li>
  <li><b>Correlation</b> — a number from -1 to 1 showing how tightly two variables move together; 0.997 means near-total lockstep, not coincidence.</li>
</ul>

<hr>

<h2>Dataset Schema &amp; Operational Ranges</h2>
<p>
  All 35,903 records in <code>swt_august_2022_final.csv</code> are real 1-minute SCADA readings from August 2022.
</p>

<table>
  <tr>
    <th>Column Name</th>
    <th>Unit / Type</th>
    <th>Observed Range</th>
    <th>Description</th>
  </tr>
  <tr><td><code>Log Time</code></td><td>YYYY:MM:DD:HH:MM:SS,ms</td><td>2022-08-01 to 2022-08-31</td><td>Timestamp of the recorded telemetry reading</td></tr>
  <tr><td><code>Windspeed (ref)</code></td><td>m/s / Integer</td><td><b>0 – 10</b></td><td>Estimated reference wind speed, calculated from rotor rotation (integer resolution)</td></tr>
  <tr><td><code>RPM</code></td><td>RPM / Integer</td><td><b>0 – 327</b></td><td>Rotational speed of the wind turbine blades</td></tr>
  <tr><td><code>Voltage In</code></td><td>V / Float</td><td><b>0.0 – 289.6</b></td><td>DC voltage generated by the turbine rotor; correlates 0.997 with RPM (physical, not anomalous)</td></tr>
  <tr><td><code>Voltage L1</code></td><td>V / Float</td><td><b>125.4 – 135.1</b></td><td>Grid AC voltage, phase L1</td></tr>
  <tr><td><code>Voltage L2</code></td><td>V / Float</td><td><b>126.9 – 138.4</b></td><td>Grid AC voltage, phase L2</td></tr>
  <tr><td><code>Current out</code></td><td>A / Float</td><td><b>0.02 – 8.47</b></td><td>Total AC output current delivered to the grid</td></tr>
  <tr><td><code>Power out</code></td><td>W / Integer</td><td><b>0 – 1,927</b></td><td>Total AC active power delivered to the grid</td></tr>
  <tr><td><code>Power reg</code></td><td>W / Integer</td><td><b>0 – 1,910</b></td><td>Gross power from the generator before inverter losses</td></tr>
  <tr><td><code>T1</code></td><td>°C / Float</td><td><b>10.3 – 37.6</b></td><td>Inverter heatsink temperature 1</td></tr>
  <tr><td><code>T2</code></td><td>°C / Float</td><td><b>10.1 – 37.8</b></td><td>Inverter heatsink temperature 2</td></tr>
  <tr><td><code>T3</code></td><td>°C / Float</td><td><b>8.1 – 35.0</b></td><td>Ambient temperature inside the nacelle housing</td></tr>
  <tr><td><code>Event count</code></td><td>Integer</td><td><b>13,228 – 13,500</b></td><td>Cumulative count of SCADA system events (genuinely incrementing, unlike a static placeholder)</td></tr>
  <tr><td><code>Last event code</code></td><td>Integer</td><td><b>6 – 111</b></td><td>Numeric identifier of the most recent logged event code</td></tr>
  <tr><td><code>Turbine status</code></td><td>Bitmask / Integer</td><td>10 distinct values observed</td><td>Bitmask of active turbine operational/mechanical states</td></tr>
  <tr><td><code>Grid status</code></td><td>Bitmask / Integer</td><td>3 distinct values observed: 0, 4096, 5120</td><td>Bitmask of grid connection health and fault conditions</td></tr>
  <tr><td><code>System status</code></td><td>Bitmask / Integer</td><td>6 distinct values observed</td><td>Bitmask of high-level system operational states</td></tr>
</table>

<hr>

<h2>Status Code Reference (Bitwise Logic)</h2>
<p>
  Status columns are bitmasks — each individual bit (1, 2, 4, 8, 16, 32...) represents one independent condition, and codes combine additively when multiple conditions occur at once
  (e.g. <code>Turbine status = 33</code> = Anemometer mode (32) + Low Windspeed (1)).
</p>

<h3>Full bit reference (individual flags)</h3>

<table>
<tr><th colspan="2">Turbine Status</th><th colspan="2">Grid Status</th><th colspan="2">System Status</th></tr>
<tr><th>Bit</th><th>Meaning</th><th>Bit</th><th>Meaning</th><th>Bit</th><th>Meaning</th></tr>
<tr><td>0</td><td>Normal Run / Power Generation</td><td>0</td><td>Normal (no faults)</td><td>0</td><td>Normal (no errors)</td></tr>
<tr><td>1</td><td>Low Windspeed</td><td>1</td><td>L1 Low Voltage</td><td>1</td><td>HS Backoff</td></tr>
<tr><td>2</td><td>Braking</td><td>2</td><td>L1 High Voltage</td><td>2</td><td>SIP TX Too Long</td></tr>
<tr><td>4</td><td>Overspeed</td><td>4</td><td>L2 Low Voltage</td><td>4</td><td>Improper Reset</td></tr>
<tr><td>8</td><td>No Stall (normal high-efficiency operation)</td><td>8</td><td>L2 High Voltage</td><td>8</td><td>Battery Timeout</td></tr>
<tr><td>16</td><td>High Wind Test</td><td>16</td><td>Offset Limit</td><td>16</td><td>Drive Off</td></tr>
<tr><td>32</td><td>Anemometer mode</td><td>32</td><td>Phase Error</td><td>32</td><td>Slave Shutdown</td></tr>
<tr><td>64</td><td>Ramp</td><td>64</td><td>Frequency Low</td><td>64</td><td>Temp Shutdown</td></tr>
<tr><td>128</td><td>TSR Incr</td><td>128</td><td>Frequency High</td><td>128</td><td>High Temp</td></tr>
<tr><td>256</td><td>Power High</td><td>256</td><td>DPLL Unlock</td><td>256</td><td>Run (Normal Operation)</td></tr>
<tr><td>512</td><td>TSR Limit</td><td>512</td><td>Grid Disconnect</td><td>512</td><td>Disabled</td></tr>
<tr><td>1024</td><td>Quiet</td><td>1024</td><td>Anti-Islanding</td><td>1024</td><td>Waiting</td></tr>
<tr><td>2048</td><td>Incr Delay</td><td>2048</td><td><i>not published</i></td><td>2048</td><td>Temp Backoff</td></tr>
<tr><td>4096</td><td>RPM Control</td><td>4096</td><td><b>"Grid Standby / No Export"</b> <i>— unofficial name, see note below</i></td><td>4096</td><td>Bad Setpoints</td></tr>
<tr><td>8192</td><td>Vin High</td><td>8192</td><td><i>not published</i></td><td>8192</td><td>Bad CRC</td></tr>
</table>

<blockquote>
<b>Documentation gap (honest disclosure):</b> The source Zenodo documentation defines Grid status bits only up to 1024 (Anti-Islanding). Our August subset contains 1,542 records with <code>Grid status = 4096</code> and 1 record with <code>Grid status = 5120</code> (= 4096 + 1024). Bit 4096 is <b>not defined anywhere</b> in the published reference sheet.
<br><br>
Rather than leave it unusable, we investigated it against the rest of the telemetry in our own data and are assigning it the working name <b>"Grid Standby / No Export"</b> — <u>this name is our own inference, not an official manufacturer term</u>. The basis for it:
<ul>
  <li>99.3% of all rows with this bit set occur while <code>Turbine status</code> already indicates Low Windspeed and/or Braking (codes 1, 3, 33, 35) — i.e. the turbine is already idle, not actively generating</li>
  <li><code>Voltage L1</code> and <code>Voltage L2</code> during these rows (avg 131.3 V / 132.5 V) are statistically indistinguishable from normal-operation rows (avg 131.1 V / 132.3 V) — no voltage anomaly is present</li>
  <li><code>Power out</code> is 0 W in effectively all of these rows</li>
</ul>
No fault signature (voltage excursion, frequency deviation, etc.) accompanies this bit — it behaves like an informational "not exporting power" flag tied to the turbine's own idle state, not a grid malfunction. We therefore treat it as a separate, low-severity <i>informational</i> category in our fault classifier, rather than lumping it in with genuine grid faults (which would inflate downtime/fault statistics with a condition that isn't actually a malfunction).
</blockquote>

<h3>Combinations actually found in this dataset (decoded)</h3>

<table>
<tr><th>Column</th><th>Value</th><th>Rows</th><th>Decoded meaning</th></tr>
<tr><td rowspan="10">Turbine status</td><td>0</td><td>11,607</td><td>Normal Run / Power Generation</td></tr>
<tr><td>1</td><td>20,058</td><td>Low Windspeed</td></tr>
<tr><td>3</td><td>400</td><td>Braking + Low Windspeed</td></tr>
<tr><td>8</td><td>3,765</td><td>No Stall</td></tr>
<tr><td>9</td><td>2</td><td>No Stall + Low Windspeed</td></tr>
<tr><td>32</td><td>1</td><td>Anemometer mode</td></tr>
<tr><td>33</td><td>31</td><td>Anemometer mode + Low Windspeed</td></tr>
<tr><td>35</td><td>20</td><td>Anemometer mode + Braking + Low Windspeed</td></tr>
<tr><td>288</td><td>1</td><td>Power High + Anemometer mode</td></tr>
<tr><td>289</td><td>18</td><td>Power High + Anemometer mode + Low Windspeed</td></tr>
<tr><td rowspan="3">Grid status</td><td>0</td><td>34,360</td><td>Normal (no faults)</td></tr>
<tr><td>4096</td><td>1,542</td><td>"Grid Standby / No Export" <i>(unofficial, inferred — see note above)</i></td></tr>
<tr><td>5120</td><td>1</td><td>Anti-Islanding + "Grid Standby / No Export" (unofficial)</td></tr>
<tr><td rowspan="6">System status</td><td>0</td><td>19,292</td><td>Normal (no errors)</td></tr>
<tr><td>8</td><td>891</td><td>Battery Timeout</td></tr>
<tr><td>256</td><td>15,226</td><td>Run (Normal Operation)</td></tr>
<tr><td>264</td><td>74</td><td>Run (Normal Operation) + Battery Timeout</td></tr>
<tr><td>1024</td><td>260</td><td>Waiting</td></tr>
<tr><td>1032</td><td>160</td><td>Waiting + Battery Timeout</td></tr>
</table>

<p>
  <i>Full bit reference published with the source dataset at <a href="https://doi.org/10.5281/zenodo.7348454">Zenodo (DOI 10.5281/zenodo.7348454)</a>.</i>
</p>

<hr>

<h2>Data Structures Used</h2>
<ul>
  <li><b>Arrays</b> — store loaded readings for indexed access, sorting, searching, and global physical checks</li>
  <li><b>Linked Lists</b> — model continuous segments and fault event chains, organized as an <b>array of linked-list heads</b> (one list per category: Low Windspeed, Grid Fault, Battery/System, and Grid Standby/Informational) so each category can be queried, sorted by duration, and traversed independently of the main telemetry array and of each other — the informational "Grid Standby" bucket is kept separate from real Grid Faults so it doesn't distort downtime/fault statistics</li>
</ul>

<hr>

<h2>Fault Detection Rules &amp; Threshold Derivation</h2>
<p>
  Each detection rule's threshold was derived empirically by testing candidate values against the actual dataset, rather than assumed — following the same evidence-based approach used in the Physical Validation section above. The goal for each threshold was a sensitivity that flags genuine anomalies without excessive false positives. A naive first attempt at Rule 2, for example, used a fixed T1 temperature cutoff and initially flagged 2,217 rows — an unusable false-positive rate driven by ordinary ambient heat rather than real faults — before being corrected to a T1-vs-ambient delta comparison.
</p>

<table>
  <tr>
    <th>Rule</th>
    <th>Condition</th>
    <th>Threshold</th>
    <th>Candidates Flagged</th>
    <th>Rationale</th>
  </tr>
  <tr>
    <td><b>1. Wind-Power Mismatch</b></td>
    <td>Windspeed ≥ 4 m/s, Power out &lt; 50W, turbine not already in an idle/braking state</td>
    <td>Fixed</td>
    <td>41</td>
    <td>Flags cases where meaningful wind is present but the turbine isn't generating expected power, while excluding rows already explained by a Low-Windspeed or Braking <code>Turbine status</code> (avoiding false positives from legitimately idle conditions)</td>
  </tr>
  <tr>
    <td><b>2. Temp-Without-Load</b></td>
    <td>Power out &lt; 10W, (T1 − T3) delta</td>
    <td>&gt; 5°C</td>
    <td>28</td>
    <td>Uses T1 (inverter heatsink) minus T3 (nacelle ambient) instead of an absolute T1 threshold, so the check isolates inverter-specific heating from ordinary outdoor/seasonal temperature. Normal delta across the dataset averages 2.1–2.7°C with a max of ~7.1°C, so &gt;5°C indicates a genuine deviation</td>
  </tr>
  <tr>
    <td><b>3. Tip-Speed Ratio Anomaly</b></td>
    <td>Windspeed ≥ 3 m/s, RPM ÷ Windspeed ratio outside band</td>
    <td>20 – 55</td>
    <td>9</td>
    <td>Substitutes for a literal gear-ratio check (the dataset has only one RPM sensor, not separate rotor/generator shaft speeds). The ratio is stable across wind speeds once windspeed ≥ 3 m/s (mean ≈ 36.4, std ≈ 4.6); below 3 m/s the ratio is naturally noisy due to low-speed measurement resolution and is excluded from this check</td>
  </tr>
  <tr>
    <td><b>4. Rapid Change Detection</b></td>
    <td>Absolute change in Power out between consecutive 1-minute readings</td>
    <td>&gt; 500W</td>
    <td>638</td>
    <td>Deliberately kept sensitive. The higher candidate count relative to the other rules is expected and by design — it is intended to be consumed by the Flood Detection system below, which groups closely-timed repeated triggers (e.g. sustained gusty wind causing many consecutive swings) into a single event rather than treating each 1-minute reading as an independent fault</td>
  </tr>
</table>

<hr>

<h2>Flood Detection &amp; Alarm Clustering</h2>
<p>
  Individual fault readings are grouped into clusters when they recur close together in time for the <i>same</i> rule, rather than being reported as independent events. This is the primary analytical objective of the project, distinguishing it from a basic threshold-checking script.
</p>
<p>
  The design follows principles from the <b>ANSI/ISA-18.2</b> industrial alarm management standard (the real standard used in process control rooms, adopted by OSHA as good engineering practice), specifically:
</p>
<ul>
  <li><b>Alarm flood definition</b> — ISA-18.2 defines a flood as more than 10 alarms within a 10-minute window; this project uses the same time-window concept to decide whether consecutive same-rule triggers belong to one ongoing cluster or are separate events</li>
  <li><b>State-based alarm suppression</b> — ISA-18.2 recommends suppressing alarms already explained by a known operating condition (e.g. not alarming on low flow caused by an already-tripped pump). This project already implements an instance of this principle via the "Grid Standby / No Export" informational category described above, which is deliberately excluded from real Grid Fault statistics</li>
  <li><b>Alarm priority tiers</b> — ISA-18.2 recommends no more than three or four alarm priorities, with high-priority alarms kept to a small minority. This project uses a three-tier severity scheme (Info / Warning / Critical)</li>
</ul>
<p>
  Each cluster records: the timestamp of its first (anchor) event, the timestamp of its most recent event, the total number of readings grouped into it, and the peak severity observed within the cluster. This gives a reader a single, actionable entry to review — e.g. <i>"Rapid Change cluster, 12 readings, 2022:08:14 14:20–14:35, peak severity CRITICAL"</i> — instead of 12 near-duplicate log lines for what is most likely one continuous physical event (such as a gust).
</p>

<hr>

<h2>Scope &amp; Limitations (Honest Disclosure)</h2>
<p>
  This project intentionally does <b>not</b> attempt statistical or machine-learning-based fault prediction, anomaly scoring, or automated root-cause inference. These are legitimate and widely-used approaches in real SCADA condition-monitoring research (e.g. neural-network and regression-based normal-behavior modeling), but they require labeled historical fault data, model training/validation, and a level of statistical rigor outside the scope of a C++ data-structures mini-project.
</p>
<p>
  Specifically:
</p>
<ul>
  <li>The Flood Detection system groups <b>repeated occurrences of the same rule</b> within a short time window, on the reasonable physical assumption that these usually reflect one ongoing condition (e.g. sustained gusty wind) rather than many independent faults. It does <b>not</b> claim to identify a definitive root cause.</li>
  <li>The system does <b>not</b> infer causal relationships between different fault types — e.g. it will not claim that a Wind-Power Mismatch event caused a later Rapid Change event, even if they occur close together in time. Any such correlation is, at most, noted as "co-occurring," never as causal.</li>
  <li>The Forecasting feature (described separately) is a naive short-term linear trend projection over the most recent readings only. It does not account for weather forecasts, seasonal patterns, or any external factors, and is not intended to be a reliable prediction of future turbine behavior — it exists only to flag developing trends worth a closer look.</li>
</ul>
<p>
  This scope was chosen deliberately: every feature in this project is one the authors can fully explain and defend line-by-line, rather than reaching for techniques (e.g. ML-based anomaly detection) that would be difficult to justify or validate within this project's timeline and academic level.
</p>

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
  This project uses real SCADA data published by:
</p>

<blockquote>
  <p>
    Bassi, W., Rodrigues, A. L., &amp; Sauer, I. L. (2023).<br>
    <i>Operation SCADA Data of an Urban Small Wind Turbine in São Paulo, Brazil</i> [Data set].<br>
    Zenodo. DOI: <a href="https://doi.org/10.5281/zenodo.7348454">10.5281/zenodo.7348454</a><br>
    Institute of Energy and Environment (IEE), University of São Paulo (USP), Brazil.<br>
    Licensed under <a href="https://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International (CC-BY-4.0)</a>.
  </p>
</blockquote>

<p>
  We gratefully acknowledge the original authors for making this real-world dataset publicly available for research and educational reference.
</p>

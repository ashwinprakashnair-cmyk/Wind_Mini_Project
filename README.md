<div align="center">
Wind Turbine SCADA Data Analysis
using C++ (Arrays & Linked Lists)
<p> A college mini-project for analyzing wind turbine sensor data — detecting faults, monitoring turbine conditions, and performing basic forecasting. </p> <img src="https://img.shields.io/badge/Language-C%2B%2B-blue?style=flat-square" /> <img src="https://img.shields.io/badge/Frontend-HTML%20%2F%20CSS-orange?style=flat-square" /> <img src="https://img.shields.io/badge/Status-In%20Development-yellow?style=flat-square" /> <img src="https://img.shields.io/badge/Data-Synthetic-lightgrey?style=flat-square" /> </div> <br>
Overview
<table> <tr><td><b>Domain</b></td><td>Green Energy — Wind Energy</td></tr> <tr><td><b>Core Language</b></td><td>C++ (Arrays, Linked Lists)</td></tr> <tr><td><b>Frontend</b></td><td>HTML + CSS Dashboard (planned)</td></tr> <tr><td><b>Level</b></td><td>College Mini-Project</td></tr> </table>

The project processes turbine sensor readings — rotor speed, generator speed, wind speed, power output, temperature, blade pitch, and turbine status — to detect faults, segment continuous data, compute basic statistics, and forecast short-term trends.

<br>
Dataset
File	Type	Description
mock_turbine_dataset.csv	Synthetic	Generated data covering all 14 turbine operating states
generate_mock_turbine_data.py	Script	Generator used to build the synthetic dataset

Note: This project uses a synthetic dataset. No real recorded SCADA data is redistributed here.

The synthetic data was inspired by the structure, value ranges, and turbine status codes of a real public research dataset:

<blockquote> Barber, S., Hammer, F., &amp; Marykovskiy, Y. (2025). <i>Aventa AV-7 (6kW) IET-OST Research Wind Turbine SCADA with Static Yaw Offset</i> [Data set]. Zenodo. <a href="https://doi.org/10.5281/zenodo.16276333">https://doi.org/10.5281/zenodo.16276333</a> </blockquote>

Realistic value ranges and turbine status code definitions used in this project were derived from that dataset's published data and metadata, used purely as a reference for building the synthetic dataset.

<br>
Turbine Status Codes
Code	Meaning	Code	Meaning
0	Initialize system	7	Standby position 1
1	Feathered position search 1	8	Standby position 2
2	Feathered position search 2	9	Standby position 3
3	Feathered position 1	10	Power operation
4	Function test 1	11	High wind shutdown
5	Function test 2	12	Shut down
6	Feathered position 2	13	Alarm / fault condition
<br>
Data Structures Used
Arrays — store loaded readings for indexed access, sorting, and searching
Linked Lists — model continuous segments; a new node begins whenever a timestamp gap is detected, so stats are computed only within genuinely continuous stretches
<br>
Status

Actively in development — core C++ parsing and analysis logic first, HTML/CSS dashboard layered on afterward.

<br>
Credits
<table align="center"> <tr> <td align="center"><b>Ashwin Nair</b></td> <td align="center"><b>Rohit Kedari</b></td> </tr> </table> <br> <p align="center"> This project's synthetic dataset was inspired by data and research published by: </p> <blockquote> <p> Sarah Barber, Florian Hammer, and Yuriy Marykovskiy (2025).<br> <i>Aventa AV-7 (6kW) IET-OST Research Wind Turbine SCADA with Static Yaw Offset</i> [Data set].<br> Zenodo. DOI: <a href="https://doi.org/10.5281/zenodo.16276333">10.5281/zenodo.16276333</a><br> Institute for Energy Technology (IET), OST – Eastern Switzerland University of Applied Sciences. </p> </blockquote> <p align="center"> We gratefully acknowledge the original authors for making this dataset publicly available for research and educational reference. </p>

# recent_earthquake_indonesia

This Python package provides an easy-to-use interface for extracting data from the Indonesian Agency for Meteorology, Climatology and Geophysics (https://www.bmkg.go.id/en.html) and displaying information about the most recent earthquake in Indonesia.

## Installation

To install the package, run the following command:

```
pip install recentearthquake-indonesia
```

## Usage

To extract the latest earthquake data, run the following command:

```
python extract.py
```

This will print the following information about the latest earthquake:

* Date and time
* Magnitude
* Depth
* Geolocation (latitude and longitude)
* Center
* Felt

## Example

The following is an example of the output of the `extract.py` script:

```
Recent Earthquake in Indonesia
Date and Time: 2023-08-25 18:23:00 (UTC+07:00)
Magnitude: 6.0
Depth: 10 km
Geolocation: Latitude= -7.52, Longitude= 112.67
Center: Lombok, West Nusa Tenggara
Felt: Not felt
```

## Contributing

Contributions are welcome! Please open a pull request on GitHub if you have any improvements or bug fixes.

## License

This package is licensed under the GNU General Public License v3 (GPLv3).

You are free to:

Use the software for any purpose.
Study the software and modify it to make it better.
Share the software with others.
The GPLv3 license requires you to:

* Make the source code of your modifications available to others.
* If you distribute the software, you must also distribute the source code.

You can find more information about the GPLv3 license at https://www.gnu.org/licenses/gpl-3.0.en.html.

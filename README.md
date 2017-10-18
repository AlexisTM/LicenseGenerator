# LicenseParser

Create the license.txt file for your project

## Usage

Create a configuration file `project.yaml`

```
license_name1:
  ros_core_libraries:
    title: ROS core libraries
    file: list/OSRF.txt
  Python:
    file: list/python.txt
license_name2:
  python:
    title: Python executable and core libraries
    file: list/python.txt
```

Execute the generator:

```bash
python LicenseGenerator.py path/to/project.yaml
```

The license files `license_name1.licenses.txt` and `license_name2.licenses.txt` are generated in the `project.yaml folder`.

The `license_name1.licenses.txt` will be:

```txt
/** ROS core libraries **/

.....(content of list/OSRF.txt)


/** Python **/

.....(content of list/python.txt)
```


## Contribute

Feel free to make a PR. The needed features are:

* Install it as an executable in the python script path
* Add it in Pypi

The optional features:
* Customize the layout
* Customize output filename
* Provide default licenses (LGPL, LGPLv2, LGPLv3, GPLv2, GPLv3, MIT, CC, BSD-3, ...)
* Provide errors for license files not found (try except, report the name of the license)

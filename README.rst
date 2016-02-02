Nexys 3 UFC Script Module
#########################

Warning
*******
Does not contain all mappings, just the basic ones that I saw need for (Switches, Buttons, LEDs) more will be added as needed. Feel free to make a pull request adding some or adding an issue to request some.

Installation
------------
.. code-block::

    $pip install git+https://github.com/badisa/Nexys-3-Script.git

Usage
-----
Outputs a ufc file with the name passed to the script

.. code-block::

    $ufc_generator.py -name Lab0A -i A SD0 -i B SD1 -o F LD0 -o F_2 LD1


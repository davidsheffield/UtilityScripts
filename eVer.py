#!/usr/bin/env python

################################
#
# eVer
#
#  Convert units to electron volt equivalents
#
#  author: David G. Sheffield
#
################################

import argparse
import math
import sys


# Constants
khbar    = 6.582119514e-16 # eV s
kc       = 299792458.0     # m / s
kin_to_m = 0.0254          # m / in
kft_to_m = 0.3048          # m / ft
kyd_to_m = 0.9144          # m / yd


def getArguments():
    parser = argparse.ArgumentParser(
        description='Convert units to electron volt equivalents.')
    # Command line flags
    parser.add_argument('value')
    parser.add_argument('-l', '--length', action='store', dest='length',
                        metavar='UNIT', help='Convert length with unit.')
    return parser.parse_args()


def prefixify(value, inverse):
    unit = 'eV'
    power = -3.0 * math.floor(math.log10(value) / 3.0)

    check_power = power
    if not inverse:
        check_power = -power

    if check_power == -3.0:
        unit = 'meV'
    elif check_power == -6.0:
        unit = 'ueV'
    elif check_power == -9.0:
        unit = 'neV'
    elif check_power == -12.0:
        unit = 'peV'
    elif check_power == -15.0:
        unit = 'feV'
    elif check_power <= -18.0:
        unit = 'aeV'
        if inverse:
            power = -18.0
        else:
            power = 18.0
    elif check_power == 3.0:
        unit = 'keV'
    elif check_power == 6.0:
        unit = 'MeV'
    elif check_power == 9.0:
        unit = 'GeV'
    elif check_power == 12.0:
        unit = 'TeV'
    elif check_power == 15.0:
        unit = 'PeV'
    elif check_power >= 18.0:
        unit = 'EeV'
        if inverse:
            power = 18.0
        else:
            power = -18.0

    value *= math.pow(10, power)
    return value, unit


def convertLength(value, unit):
    if unit in ['m', 'meter']:
        unit = 'm'
        value_m = float(value)
    elif unit == 'dm':
        value_m = float(value) / 10.0
    elif unit == 'cm':
        value_m = float(value) / 100.0
    elif unit == 'mm':
        value_m = float(value) / 1.0e-3
    elif unit == 'um':
        value_m = float(value) * 1.0e-6
    elif unit == 'nm':
        value_m = float(value) * 1.0e-9
    elif unit == 'pm':
        value_m = float(value) * 1.0e-12
    elif unit == 'fm':
        value_m = float(value) * 1.0e-15
    elif unit == 'am':
        value_m = float(value) * 1.0e-18
    elif unit == 'dam':
        value_m = float(value) * 10.0
    elif unit == 'hm':
        value_m = float(value) * 100.0
    elif unit == 'km':
        value_m = float(value) * 1.0e3
    elif unit == 'Mm':
        value_m = float(value) * 1.0e6
    elif unit == 'Gm':
        value_m = float(value) * 1.0e9
    elif unit == 'Tm':
        value_m = float(value) * 1.0e12
    elif unit == 'Pm':
        value_m = float(value) * 1.0e15
    elif unit == 'Em':
        value_m = float(value) * 1.0e18
    elif unit in ['in', 'inch']:
        unit = 'in'
        value_m = float(value) * kin_to_m
    elif unit in ['ft', 'foot', 'feet']:
        unit = 'ft'
        value_m = float(value) * kft_to_m
    elif unit in ['yd', 'yard']:
        unit = 'yd'
        value_m = float(value) * kyd_to_m
    elif unit == 'thou':
        value_m = float(value) / 1000.0 * kin_to_m
    elif unit == 'tenth':
        value_m = float(value) / 10000.0 * kin_to_m
    else:
        print('{0} is not a recognized unit.'.format(unit))
        sys.exit(1)

    value_eV = value_m / (khbar * kc)
    value_XeV, unit_eV = prefixify(value_eV, True)
    print("Length: {0} {1} = {2} /{3}".format(float(value), unit, value_XeV, unit_eV))
    energy_XeV, unit_eV = prefixify(1.0 / value_eV, False)
    print("Energy scale: {0} {1}".format(energy_XeV, unit_eV))


def main():
    args = getArguments() # Setup flags and get arguments
    if args.length:
        convertLength(args.value, args.length)
    else:
        print('Must specify dimension to convert.')


if __name__ == '__main__':
    main()

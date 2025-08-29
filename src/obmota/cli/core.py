# -*- coding: utf-8 -*-

import click

from obmota.TripData import TripData

@click.group(invoke_without_command=False)
def cli():
    """
        \b
        __  __    ___  ____  __  __    ___ _____  _      __  __
        \ \/ /   / _ \| __ )|  \/  |  / _ \_   _|/ \     \ \/ /
         \/ /   | | | |  _ \| |\/| | | | | || | / _ \     \/ / 
         / /\   | |_| | |_) | |  | | | |_| || |/ ___ \    / /\ 
        /_/\_\   \___/|____/|_|  |_|  \___/ |_/_/   \_\  /_/\_\\
        
        \b
        obmota is a utility package for encoding/decoding OBM OTA
        Packages according to Euro 7/VII definitions.
        
        Invoke with a command from the list below.
    """
    pass


@cli.group()
# @click.option('-d', '--decode', help="Returns a human-readable version of the trip data string")
def tripdata():
    """
        Ingest a trip data string (64 bytes) for manipulation.
        
        It is meant to be called with any command listed below.
    """
    pass


@tripdata.command()
@click.argument('td', required=True, type=str)
def decode(td):
    """
        Returns a human-readable version of the trip data string
        without verifying the hashing.
        
        TD = the string to be parsed (64 bytes expected)
    """
    trip_data = TripData(td)
    click.echo(trip_data)


if __name__ == '__main__':
    cli()
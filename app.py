#!/usr/bin/env python
import click

@click.command()
@click.option("--name")
def hello(name):
    click.echo(f'Hello there {name}!')

if __name__ == '__main__':
    #pylint: disable=no-value-for-parameter
    hello()
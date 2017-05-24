import click

@click.command()
@click.argument('dollars')
def cli(dollars):
	dollars = int(dollars)
	INR = int(64.77 * dollars)
	click.echo("{} $ == {} INR".format(dollars, INR))
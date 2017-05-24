from setuptools import setup
setup(
	name="dtr",
	version='0.1',
	py_modules=['hello'],
	install_requires=['Click',],
	entry_points='''
		[console_scripts]
		dtr=hello:cli
	''',
)


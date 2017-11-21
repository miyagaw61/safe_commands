from setuptools import setup, find_packages

console_scripts = [
        'remove=safe_commands.safe_commands:console_remove',
        'move=safe_commands.safe_commands:console_move',
        'copy=safe_commands.safe_commands:console_copy',
        ]

setup(
    name='safe_commands',
    version='0.0.1',
    packages=find_packages(),
    description='safe_commands',
    author='Taisei Miyagawa @miyagaw61',
    author_email='miyagaw61@gmail.com',
    install_requires=['enert==0.0.2', 'better_exceptions'],
    dependency_links=['git+https://github.com/miyagaw61/enert.git#egg=enert-0.0.2'],
    entry_points = {'console_scripts': console_scripts},
    url='https://github.com/miyagaw61',
    license='MIT'
)

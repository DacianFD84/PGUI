from setuptools import setup, find_packages

setup(
    name='PlaywrightGUI',  # Numele aplicației tale
    version='1.0.0',  # Versiunea aplicației
    packages=find_packages(),  # Găsește toate pachetele din directorul curent
    install_requires=[
        'PyQt6==6.4.0',  # Adaugă dependințele tale
        'playwright==1.28.0',
    ],
    include_package_data=True,  # Include fișierele suplimentare
    package_data={
        '': ['*.py'],  # Include toate fișierele Python din proiect
    },
    entry_points={
        'console_scripts': [
            'playwrightgui = main:main',  # Schimbă la funcția principală
        ],
    },
)

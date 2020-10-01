import setuptools

setuptools.setup(
	name='cc_oaktree',
	version='3.0',
	author="yoochan",
	author_email="yota.news@gmail.com",
    url="https://github.com/yota-code/oaktree",
    description="tree handling library compatible with xml/html and braket",
    packages=setuptools.find_packages(where="package"),
	package_dir = {
		'': 'package'
	},
    classifiers=[
        "Programming Language :: Python :: 3",
		"Development Status :: 4 - Beta",
        "License :: OSI Approved :: BSD License",
		"License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

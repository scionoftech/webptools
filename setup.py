import setuptools

with open('README.md') as f:
    long_description = f.read()

setuptools.setup(
    name="webptools",
    version="0.0.5",
    scripts=['webptools/webplib.py'],
    author="Sai Kumar Yava",
    author_email="saikumar.geek@gmail.com",
    description="webptools is a Webp image conversion package for python",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/scionoftech/webptools",
    packages=['webptools', 'lib', 'lib/libwebp_linux', 'lib/libwebp_osx',
              'lib/libwebp_win64'],
    package_data={'': ['lib/*']},
    include_package_data=True,
    keywords=['webp', 'converter', 'image'],
    install_requires=["uuid"],
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
    ],

)
# packages=setuptools.find_packages(include=['lib', 'lib.*', 'frames']),
# package_data = {'': ['*.py', 'lib/*']},
# include_package_data = True,
# data_files = [('lib/*')],

from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='iiyo',
  version='1.0.2',
  description='iiyo is Sinhala Prastha Pirulu Theravili, Thun theravili Sinhalen, Sinhala Random Name genarate ',
  long_description_content_type="text/markdown",
  package_data={'iiyo': ['*.last', '*.txt']},
  url='https://github.com/dotLK/iiyo',  
  author='https://github.com/dotLK',
  author_email='',
  license='MIT', 
  classifiers=classifiers,
  keywords='iiyo,Sinhala Prastha Pirulu, Theravili , Thun theravili sinhalen,random_name_generator,name-generator', 
  packages=find_packages(),
  install_requires=[''] 
)

from setuptools import setup
import os

def recursive_get_sub_packages(path):
    res = []
    for folder in os.listdir(path):
        rec_path = f'{path}{folder}/'
        if os.path.isdir(rec_path) and folder != '__pycache__' and not folder.startswith('.') :
            res.append(rec_path.replace('/', '.').strip('.'))
            res.extend(recursive_get_sub_packages(rec_path))
    return res

setup(
      name='japanese_learner',
      version='0.1.1',
      description='Help to learn Japanese letter',
      url='https://github.com/matthieuDev/japanese_learner/',
      author='MatthieuDev',
      author_email='matthieu.devaux@alumni.epfl.ch',
      license='MIT',
      packages=['japanese_learner'] + recursive_get_sub_packages('japanese_learner/'),
      install_requires= ['matplotlib', 'numpy', 'tensorflow', 'epitran'],
      zip_safe=False,
      include_package_data=True,
      package_data={'japanese_learner': ['**/*.json', '**/*.csv', '**/*.html',  '**/*.md']},
)
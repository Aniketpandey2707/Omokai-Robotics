from setuptools import setup

package_name = 'mission_executor'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Aniket Pandey',
    maintainer_email='pandeyaniket2707@gmail.com',
    description='Mission Executor for Omokai Robotics Assignment',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'main = mission_executor.main:main',
        ],
    },
)
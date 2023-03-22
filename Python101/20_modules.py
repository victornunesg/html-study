# ----------------------------
# MODULES
# ----------------------------

# importing modules
import platform

# you can also give an alias/name for the module:
# import platform as pl

# and you can import a specific method
# from platform import python_version, system
# print(python_version())
# print(system())

print('\nModules')
# Instead of just copy and paste codes that do specific things, you can use modules importing them
# https://docs.python.org/3/py-modindex.html

# using dir statement to check all the methods in datetime module
print(dir(platform))
# calling a method from the module 'platform'
print(platform.python_version())

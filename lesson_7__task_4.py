""" Урок 7, завдання 4
Ознайомтеся за допомогою документації з класами OrderedDict, defaultdict та ChainMap модуля collections.
"""

"""
class collections.OrderedDict([items])

Return an instance of a dict subclass that has methods specialized for rearranging dictionary order.
"""


"""
class collections.defaultdict(default_factory=None, /[, ...])

Return a new dictionary-like object. defaultdict is a subclass of the built-in dict class. It overrides one method 
and adds one writable instance variable. The remaining functionality is the same as for the dict class and is not 
documented here.
The first argument provides the initial value for the default_factory attribute; it defaults to None. All remaining 
arguments are treated the same as if they were passed to the dict constructor, including keyword arguments.
"""


"""
A ChainMap class is provided for quickly linking a number of mappings so they can be treated as a single unit. 
It is often much faster than creating a new dictionary and running multiple update() calls.
The class can be used to simulate nested scopes and is useful in templating.

class collections.ChainMap(*maps)

A ChainMap groups multiple dicts or other mappings together to create a single, updateable view. If no maps are 
specified, a single empty dictionary is provided so that a new chain always has at least one mapping.
The underlying mappings are stored in a list. That list is public and can be accessed or updated using the maps 
attribute. There is no other state.
Lookups search the underlying mappings successively until a key is found. In contrast, writes, updates, and 
deletions only operate on the first mapping.
A ChainMap incorporates the underlying mappings by reference. So, if one of the underlying mappings gets updated, 
those changes will be reflected in ChainMap.
"""

import math
from typing import *

__all__ = [
  'type_check',
  'type_instantiate',
  'least_common_multiple',
  'Has_Next_Iterator',
  'has_next',
]


def type_check(value, ty) -> bool:
  """
    shitty isinstance that also works with 'typing' objects
  """

  if getattr(ty, '__origin__', None) is Union:
    for sub_ty in ty._subs_tree()[1:]:
      if type_check(value, sub_ty):
        return True
    return False
  if getattr(ty, '__origin__', None) is Dict:
    if not type_check(value, dict):
      return False

    key_ty, val_ty = ty._subs_tree()[1:]

    for key, val in value.items():
      if not type_check(key, key_ty):
        return False
      if not type_check(val, val_ty):
        return False

    return True
  if getattr(ty, '__origin__', None) is Set:
    if not type_check(value, set):
      return False

    elem_ty = ty._subs_tree()[1]

    for elem in value:
      if not type_check(elem, elem_ty):
        return False

    return True
  if getattr(ty, '__origin__', None) is List:
    if not type_check(value, list):
      return False

    elem_ty = ty._subs_tree()[1]

    for elem in value:
      if not type_check(elem, elem_ty):
        return False

    return True
  if getattr(ty, '__origin__', None) is Tuple:
    if not type_check(value, tuple):
      return False

    elem_ty = ty._subs_tree()[1]

    for elem in value:
      if not type_check(elem, elem_ty):
        return False

    return True
  else:
    return isinstance(value, ty)


def type_instantiate(ty, *args, **kwargs):
  """
    create instance of type
  """

  if getattr(ty, '__origin__', None) is Dict:
    ctor = dict
  elif getattr(ty, '__origin__', None) is List:
     ctor = list
  elif getattr(ty, '__origin__', None) is Set:
    ctor = set
  elif getattr(ty, '__origin__', None) is Tuple:
    ctor = tuple
  else:
    ctor = ty

  obj = ctor(*args, **kwargs)
  assert type_check(obj, ty)
  return obj


def least_common_multiple(a: int, b: int) -> int:
  # https://en.wikipedia.org/wiki/Least_common_multiple#Reduction_by_the_greatest_common_divisor
  return abs(a * b) // math.gcd(a, b)


E = TypeVar('E')


class Has_Next_Iterator(Iterator[E]):
  """
    Iterator that wraps another iterator and adds
    a has_next() method that checks if the iterator is empty
  """

  _SENTINEL  = object()

  def __init__(self, it: Iterator[E]):
    self._iter = iter(it)
    self._peek = self._SENTINEL

  def __iter__(self):
    return self

  def __next__(self):
    if self._peek is self._SENTINEL:
      return next(self._iter)
    else:
      out = self._peek
      self._peek = self._SENTINEL
      return out

  def has_next(self):
    if self._peek is self._SENTINEL:
      try:
        self._peek = next(self._iter)
      except StopIteration:
        return False

    return True

  def __bool__(self):
    return self.has_next()


def has_next(fn):
  """
    Wraps the generator iterator returned by a function in a Has_Next_Iterator
  """

  def wrapper(*args, **kwargs):
    gen = fn(*args, **kwargs)
    return Has_Next_Iterator(gen)

  return wrapper



import math
from typing import *

__all__ = [
  'type_check',
  'type_instantiate',
  'least_common_multiple',
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


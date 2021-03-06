from typing import Any
from typing import Generic
from typing import overload
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Tuple
from typing import Type
from typing import List
import pynamodb.attributes

_T = TypeVar('_T')

# TODO: derive from pynamodb.attributes.Attribute directly when pynamodb>=5
if TYPE_CHECKING:
    _A = TypeVar('_A', bound=pynamodb.attributes.Attribute[Any])

    class Attribute(Generic[_T], pynamodb.attributes.Attribute[_T]):
        @overload
        def __get__(self: _A, instance: None, owner: Any) -> _A:
            ...

        @overload
        def __get__(self, instance: Any, owner: Any) -> _T:
            ...

        def __get__(self, instance: Any, owner: Any) -> Any:
            ...
else:
    class Attribute(Generic[_T], pynamodb.attributes.Attribute):
        pass

T = TypeVar('T', bound = Tuple[Any, ...])
_DEFAULT_FIELD_DELIMITER = '#'

class UnicodeDelimitedTupleAttribute(Attribute[T]):
    """
    Stores a tuple of strings as a string. The tuple's members will be joined with a delimiter.
    >>> from typing import NamedTuple
    >>>
    >>> from pynamodb.models import Model
    >>>
    >>> class LatLng(NamedTuple):
    >>>   lat: int
    >>>   lng: int
    >>>
    >>> class Employee(Model):
    >>>   location = UnicodeDelimitedTupleAttribute(LatLng)
    """
    attr_type = pynamodb.constants.STRING
    def __init__(self, tuple_type: Type[T], delimiter:str = _DEFAULT_FIELD_DELIMITER, **kwargs: Any)->None:
        """
        :param tuple_type: The type of the tuple -- may be a named or plain tuple
        :param delimiter: The delimiter to separate the tuple elements
        """
        super().__init__(**kwargs)
        self.tuple_type : Type[T] = tuple_type
        self.delimiter = delimiter
    def deserialize(self, value: str) -> T:
        fields = getattr(self.tuple_type, '_fields', None)
        field_types = getattr(self.tuple_type, '_field_types', None)
        if fields and field_types:
            values = value.split(self.delimiter, maxsplit=len(fields))
            params = {}
            for f,v in zip(fields, values):
                _type = field_types[f]
                subtypes = getattr(_type, '__args__', None)
                if subtypes:
                    for _t in subtypes:
                        try:
                            params[f] = _t(v)
                            break
                        except ValueError:
                            continue
                else:
                    params[f] = _type(v)
            return self.tuple_type(**params)
        else:
            return self.tuple_type(value.split(self.delimiter))
    
    def serialize(self, value:T)->str:
        if not isinstance(value, self.tuple_type):
            raise TypeError(f"value has invalid type '{type(value)}'; expected '{self.tuple_type}'")
        values: List[T] = list(value)
        while values and values[-1] is None:
            del values[-1]
        strings = [str(e) for e in values]
        if any(self.delimiter in s for s in strings):
            raise ValueError(f"Tuple elements may not contain delimiter '{self.delimiter}'")
        return self.delimiter.join(strings)
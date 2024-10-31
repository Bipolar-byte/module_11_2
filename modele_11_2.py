import inspect
import sys


def introspection_info(obj):
    obj_type = type(obj).__name__
    obj_module = getattr(obj, "__module__", None)

    module_path = sys.modules[obj_module].__file__ if obj_module in sys.modules else None

    obj_attrs = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    obj_methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]

    is_user_defined = inspect.isclass(type(obj)) and obj_module != "builtins"

    nesting_level = obj_module.count(".") if obj_module else 0

    return {
        "type": obj_type,
        "attributes": obj_attrs,
        "methods": obj_methods,
        "module": obj_module,
        "module_path": module_path,
        "user_defined": is_user_defined,
        "nesting_level": nesting_level
    }


number_info = introspection_info(42)
print(number_info)


class Testclass:
    def __init__(self, name):
        self.name = name
        self.value = 100

    def greet(self):
        return


my_object = Testclass("Alice")
my_object_info = introspection_info(my_object)
print(my_object_info)

__all__ = ['Base', 'MyClass', 'Other']


class Base:
    """
    A public base class
    """


class _Mixin(Base):
    """
    A private class between two public classes
    """


class MyClass(_Mixin):
    """
    A public class whose only base class is private
    """


class Other(Base):
    """
    A public class with a public base class
    """

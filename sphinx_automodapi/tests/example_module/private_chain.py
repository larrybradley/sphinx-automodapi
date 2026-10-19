__all__ = ['Base', 'Combined', 'MyClass', 'Other', 'Solo']


class Base:
    """
    A public base class
    """


class _Mixin(Base):
    """
    A private class between two public classes
    """


class _Helper:
    """
    A private mixin class without public ancestors
    """


class MyClass(_Mixin):
    """
    A public class whose only base class is private
    """


class Other(Base):
    """
    A public class with a public base class
    """


class Combined(_Helper, Base):
    """
    A public class with a private mixin and a public base class
    """


class Solo(_Helper):
    """
    A public class whose only base class is a private mixin
    """

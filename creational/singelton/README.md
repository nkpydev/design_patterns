# Singleton Pattern

## Purpose:
Ensures that a class has only one instance and provides a global point of access to it.

## When to use?
- Logger Objects
- Configuration Management
- Thread pool Managers
- Database Connections

## How does it work?
This implementation uses, **metaclasses** to intercept instance creation and ensures only one object is created for the class.

## Example Output:
```cmd
Creating new instance for class: Singleton
Singleton value: first
Returning existing instance for Singleton
Singleton value: first
obj1 is obj2? True
```
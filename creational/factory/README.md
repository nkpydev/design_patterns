# Factory Pattern

## Purpose:
Defines an interface for creating objects, but lets subclasses decide which class to instanciate.

## When to use:
- When object creation logic is complex.
- To decouple object instantiation from usage.
- To promote **Open/Closed Principle**

## How it works?
A 'Factory' class exposes a 'create' method which returns instances of common interface.

## Example Output:
```cmd
Dog says: Woff!
Cat says: Meow!
```
# Builder Pattern

## Purpose
Separates the construction of a complex object from its representation so that the same construction process can create different representations.

## When to use
- When an object has many optional parts or configuration
- When construction involves many steps

## How it works ?
Use a `Builder` class to create an object step by step and return the final object using a `build()` method.

## Example Output
```cmd
Car with V8 engine, 4 wheels, color Red
```
# Mutable vs Immutable Objects

A **mutable object** can be changed after it's created, and an **immutable object** can't.

In Javascript, **everything (except for strings) is mutable by default**:

```
const array = [4, 9];

array[0] = 1;
// array is now [1, 9]
```

**Freezing an object** makes it immutable, though:

```
const array = [4, 9];

// Make it immutable
Object.freeze(array);

array[0] = 1;
// array is still [4, 9]
```

Strings can be mutable or immutable depending on the language.

Strings are immutable in Javascript:

```
const testString = 'mutable?';

testString[7] = '!';
// String is still 'mutable?'
// (but no error is raised!)
```

But in some other languages, like Swift, strings can be mutable:

```
var testString = "mutable?"

if let range = testString.range(of: "?") {
testString.replaceSubrange(range, with: "!")
// testString is now "mutable!"
}
```

Swift
Mutable objects are nice because you can make changes **in-place**, without allocating a new object. But be careful—whenever you make an in-place change to an object, all references to that object will now reflect the change.

# Binary numbers

The number system we usually use (the one you probably learned in elementary school) is called base 10, because each digit has ten possible values (1, 2, 3, 4, 5, 6, 7, 8, 9, and 0).

But computers don't have digits with ten possible values. They have bits with two possible values (0 and 1). So they use base 2 numbers.

Base 10 is also called decimal. Base 2 is also called binary.

Binary, or "base-two" numbers

Just as the places in base 10 are sequential powers of 10, the places in binary (base 2) are sequential powers of 2:

2^0= 1
2^1=2
2^2=4
2^3=8
etc.

## Negative Numbers and Two's Complement

Negative numbers are typically represented in binary using two's complement encoding. In two's complement, the leftmost digit is negative, and the rest of the digits are positive.

Let's look at what happens when we interpret that 101 as two's complement:
-101 = -4+0+1 = -3

```
Fun computer systems trivia fact: two's complement isn't the only way negative numbers could be encoded. Other encodings tossed around in the 1960s included one's complement and sign and magnitude encodings. Of the three encodings, two's complement is the one still used today for a few reasons:

There is only one way to represent zero.
Basic operations like addition, subtraction, and multiplication are the same regardless of whether the numbers involved are positive or negative.
Since two's complement had both of these properties (and the others didn't), it stuck around and is still used today.
```

## Counting from -5 to 5 in two's complement

Here are the base-10 numbers -5−5 through 55 in two's complement, along with how we'd interpret each bit:

| Decimal | Binary | Interpretation |
| ------- | ------ | -------------- |
| -5      | 1011   | -8 + 0 + 2 + 1 |
| -4      | 1100   | -8 + 4 + 0 + 0 |
| -3      | 1101   | -8 + 4 + 0 + 1 |
| -2      | 1110   | -8 + 4 + 2 + 0 |
| -1      | 1111   | -8 + 4 + 2 + 1 |
| 0       | 0000   | 0 + 0 + 0 + 0  |
| 1       | 0001   | 0 + 0 + 0 + 1  |
| 2       | 0010   | 0 + 0 + 2 + 0  |
| 3       | 0011   | 0 + 0 + 2 + 1  |
| 4       | 0100   | 0 + 4 + 0 + 0  |
| 5       | 0101   | 0 + 4 + 0 + 1  |

So, should 1011 be read as "eleven" (in binary) or "negative five" (in two's complement)?

It could be either one! Many languages have two types of numbers: signed and unsigned. Signed numbers are represented in two's complement, and unsigned numbers use plain old base 2.

So, if an interviewer asks you to convert base-2 into decimal, ask: "is that in two's complement or not?"

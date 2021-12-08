## Remember

- Preprocessor directives, namespace, main(), output and input, cascading, return statement.
- `\n` and `\t` in printing.
- Taking strings as input through `cin` or `getline()`.
- Behaviour of `cin`, `cin.get()`, `cin.getline()`, `getline()` and `cout`.

## Data Types

- Size of different data types.
  - Number of bits each data type takes also depends on compiler and can change based on a system being 32-bit or 64-bit.

## Declaration VS Defination

- Declaration mean allocating the memory and symbol table entry.
- Defination mean assigning the value.
- They are mostly done together.

- Literal is a direct value. eg. "Hello" is a String literal, 23 is a int literal etc.
- For integer type of variables we can assign a literal in decimal number system, octal or hexa and these type of ints, can be used in short, long, long long and even for char data type.
  - By default it's a base 10 integer, if prefixed with 0 it's Octal, if prefixed with 0x with Hexdecimal
  - In cout all the system are converted to decimal and printed
  - In character all are converted to decimal and their ASCII values are printed
- To write float as 12.98 then by default the value is double. Better to have F or f at the end for float literals.
- Similarly with integar it's int if you wanna assign long then use L suffix, and LL for long long.
- NOTE: If we assign a float value to a char then float value is converted into character and this is done implicitly that's why it is called type coercion.
- To use the number in scientific notation use e followed by the raised power. eg. 12e2 will be depicted as 1200, 12e-1 as 1.2 etc.

## Overflow

- Say we have a char x and as we know the range of char is from -128 to 127 so we might get an error or warning upon storing 130 depending on compiler. So from char x = 127 if we do x++ in next line since the capacity of char is only till 127 max so it will come back to -128. Think of it as a round pattern with numbers from -128 to 127. If you do next or increment after last number 127 or 360 degree you come back to -128 or 0th degree. Similarly if we are at x = -128 and we do x-- then we come back to 127.

- Cycling is done when the we try to exceed any data type's limit (overflow).

## NOTE

- % works only on int and char type data and not for float.
- Arithematic Operators follow PEMDAS.
- There are 4 kinds of pre/post increment and decrement operators.

  1. Pre Increment (++x) Unary operator, much faster than x = x+1 a binary operator.
  2. Post Increment (x++)
  3. Pre Decrement (--x)
  4. Post Decrement (x--)

- Bitwise operations occur on the bits of data and not on the entire data as single unit. Bit-Wise Operators which are available :

  - & (bitwise AND) Takes two numbers as operands and does AND on every bit of two numbers. The result of AND is 1 only if both bits are 1.

  - | (bitwise OR) Takes two numbers as operands and does OR on every bit of two numbers. The result of OR is 1 any of the two bits is 1.

  - ^ (bitwise XOR) Takes two numbers as operands and does XOR on every bit of two numbers. The result of XOR is 1 if the two bits are different.

  - << (left shift) Takes two numbers, left shifts the bits of the first operand, the second operand decides the number of places to shift. If a number x is left shift by i positions then result is x \* 2^i.Sign bit is not affected and stays same.

  - > > (right shift) Takes two numbers, right shifts the bits of the first operand, > > the second operand decides the number of places to shift. > > If a number x is right shift by i then x will get divided by 2^i. Sign bit is not affected and stays same.

  - ~ (bitwise NOT) Takes one number and inverts all bits of it

- typedef used to define our own data type or giving alias to some other data type. So it is easier for us to keep track, prevent errors and make code more readable.
  eg. typedef int i; //Now we can use i instead of int
  Above example gives alias to data type int used as i. Because we might not know what's the use of 2 int variables declared out of nowhere so it is better to have 2 int variables which are declared as i m1,m2 to give us an idea these something to do with marks.

- Most of the time typedef is used in competetive programming to make things fast. eg. typedef long long l

- Explicit type conversion => (newtype)var OR newtype(var)

  - This doesn't change type of original variable but it creates a soft copy with new type which we can either store somewhere or use to print.
    eg. int x = 65;
    cout<< char(x); //A
    cout<< (char)x; //A

- NOTE: Operators are just functions.

## Declaring Constants

- Enum is used to define a group of related constants under one name.
- #define mon 0 //This is a preprocessor. As it is starting with # so no need of ; at the end.
- int const mon = 0; //const keyword is used to make the path constant i.e. only read access. NOTE path not storage.
Object orientation is a strategy/style of writing programs/software. Other methodologies include structured programming, procedural programming, modular programming, aspect oriented programming.

OOP is more related to designing of a software, and deals with internal designing or organization of code. Programming or app development becomes highly systematic and allows us to follow the procedures of engineering to design a software using OOP.

Principles of Object Oriented Programming

1. Abstraction: Object Oriented approach gives a systematic method to develop software, apps and solutions in an organised way just how other engineers develop buildings, blue prints or any other things in a systematic manner.This allows the user to not know how the entire program works, just giving user enough idea about how to perform functions he/she wants to perform. Just like a TV or Car, internal mechanism is not available what user can interact with is more than enough to accomplish all the tasks users might need to perform. We write stuff inside class.

2. Encapsulation: Another thing we get due to class is encapsulation or data hiding.To avoid mishandling of variables we use data encapsulation. Functions used to access variables and modify them are public, but direct modification of variables is avoided by making variables inside a class as private.

3. Inheritance: Say we have written a class A, and after some days we want another class B which has all the features as class A along with some other features too which I will add. Then we can borrow/inherit all the features of A, add our own features to get class B.

4. Polymorphism: C++ polymorphism means that a call to a member function will cause a different function to be executed depending on the type of object that invokes the function.

Class vs Object

It is said that everything in the world is an object and there is some class for it most probably. Class means to classify and we can take any object in the world and it has to belong to some class, even if it doesn't begins to any class then it means that it belongs to class of objects which do not fit into any other existing classes.

Class is like a blueprint and object is the thing created from that blueprint.

Class is a definition how something should be if it is made from the class, in a sense it is a blueprint. Object is the instance. Say Car is a class and BMW is an instance of it. Blueprint is made once but from that multiple houses are made which are identical in a housing board colony. That means that blueprint is a class telling how every house, an object should be and identical houses or objects are created from that. Data and function together make up a class. We can create class for kind of object we want as per our needs and then create some instances of those classes we made to proceed as per our coding requirement.

NOTE: Using dot operator(.) we can access the properties of a normal object. If we want to access the properties of a pointer object we use arrow operator(->).

We can create an object either in stact or in heap just like any other primitive data type.

The concept of getter and setter functions are introduced because of data hiding/ encapsulation. getter is to get the data and setter is to set the data. Get functions are called accessor functions and set functions are called mutators and known as property functions. For a data member if there exists get and set both then that means it is read and writeable. If a data member has only get and no set then it means that data member is just read only. It depends on programmer to define read and write.

CONSTRUCTOR : Function which is automatically called when the object is created off of a class.

On creation of object, a function was there in the compiler which constructed the object.
Every class will have a constructor. Compiler provided built-in constuctor is called as default constructor.

There are 3 different types of user defined constructor :

1. Non-parameterized constructor
2. Parameterized constructor
3. Copy Constuctor
   If we don't write any of the 3 constuctors above then the 4th kind default constructor is provided by compiler.

Contructor don't have any return type not even void and have name same as class name.

PROBLEM WITH COPY CONSTUCTOR : Copy constructer do shallow copy (naam ka copy bus). So whenever we have to deal with pointers we have to do deep copy (true copy). For deep copy we use heap memory (new and delete).

So our class should have the following methods irrespective of need to create a perfect class :

1. Constructors
   1.1 Non parameterized constructor
   1.2 Parameterized constructor
   1.3 Copy constructor
2. Setter or mutators
3. Accessors or Getters
4. Actual functions useful for class called Facilitators
5. Inspector function -> Checks based on some properties, mostly a bool
6. Destructor function

In a class we just write the function names and do not define the functions inside it without ellaborating.
Functions are ellaborated outside the class by using scope resolution operators.

Every method of a class is automatically provided with a pointer named `this` that holds the address of the current object in which the method is called.
this-> pointer is used to remove the ambiguity between parameters of functions and data members of a class.
this-> is used to refer to the data member of current object we are writing this in.

A struct is another user defined data type. Data members can't be private or protected in a structure as opposed to a class. Structure has everything by default as public and class has everything by default as private.
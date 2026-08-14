Yes. The important thing is to understand that **`@decorator_name` is not magic**. Python performs a specific operation when it sees it.

Let's go deep, step by step.

### 1. Start with a normal function

```python
def printer():
    print("Welcome")


printer()
```

When Python executes:

```python
def printer():
    print("Welcome")
```

Python creates a **function object** in memory.

Conceptually:

```text
printer ──────────────► function object
                       ┌─────────────────┐
                       │ code            │
                       │ name: printer   │
                       │ globals         │
                       │ ...             │
                       └─────────────────┘
```

The name `printer` is simply a variable/reference pointing to that function object.

---

# 2. Now create a decorator

```python
def dec_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")

    return wrapper
```

Notice something important:

`dec_decorator` itself **doesn't decorate anything yet**.

It is simply a function that expects another function.

For example:

```python
dec_decorator(printer)
```

Here:

```text
printer
   │
   ▼
function object
   │
   │ passed as argument
   ▼
dec_decorator(func)
```

Inside `dec_decorator`:

```python
func
```

now refers to the original `printer` function.

Then Python creates:

```python
def wrapper():
    print("Before")
    func()
    print("After")
```

and returns that `wrapper` function.

So:

```python
new_function = dec_decorator(printer)
```

means:

```text
printer ─────────► original printer function


new_function ────► wrapper function
                         │
                         │ remembers
                         ▼
                    original printer
```

That "remembers" part becomes very important later: **closure**.

---

# 3. Now let's introduce `@`

Suppose you write:

```python
@dec_decorator
def printer():
    print("Welcome")
```

At first glance, it looks like:

```text
@dec_decorator
    ↓
some special decoration mechanism
```

But that's not what you should think.

Instead, Python essentially transforms the definition into:

```python
def printer():
    print("Welcome")

printer = dec_decorator(printer)
```

That is the fundamental idea.

So:

```python
@dec_decorator
def printer():
    print("Welcome")
```

becomes conceptually:

```python
def printer():
    print("Welcome")

printer = dec_decorator(printer)
```

---

# 4. But WHEN does this happen?

This is where understanding Python execution becomes useful.

Consider:

```python
print("1")

@dec_decorator
def printer():
    print("Welcome")

print("2")
```

Python executes the file **from top to bottom**.

When Python reaches:

```python
@dec_decorator
def printer():
    print("Welcome")
```

it does roughly this:

### Step 1

Python creates the original function:

```python
def printer():
    print("Welcome")
```

So now:

```text
printer ───────► original function
```

### Step 2

Python evaluates the decorator:

```python
dec_decorator
```

This gives Python the decorator function.

### Step 3

Python calls the decorator and passes the newly created function:

```python
dec_decorator(printer)
```

So:

```text
                printer
                   │
                   ▼
             original function
                   │
                   │ passed into
                   ▼
             dec_decorator()
                   │
                   ▼
             wrapper function
```

### Step 4

The returned value is assigned back to `printer`:

```python
printer = dec_decorator(printer)
```

This is the crucial part.

Before decoration:

```text
printer ───────► original function
```

After decoration:

```text
printer ───────► wrapper function
                         │
                         ▼
                  original function
```

So the name `printer` **no longer directly points to the original function**.

It now points to the wrapper.

---

# 5. That's why this works

Suppose:

```python
@dec_decorator
def printer():
    print("Welcome")
```

and:

```python
def dec_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")

    return wrapper
```

After decoration, you can mentally rewrite the entire thing as:

```python
def printer():
    print("Welcome")


def wrapper():
    print("Before")
    printer()
    print("After")


printer = wrapper
```

There is one subtle problem with this simplified representation, though.

The actual `wrapper` needs access to the **original** `printer`, even after the name `printer` is replaced.

That's where **closures** come in.

---

# 6. The closure is the deeper part

Look at this:

```python
def dec_decorator(func):

    def wrapper():
        print("Before")
        func()
        print("After")

    return wrapper
```

When `dec_decorator(printer)` runs:

```python
func
```

refers to the original `printer`.

Then `wrapper` is created.

Even though `func` is a local variable of `dec_decorator`, `wrapper` can still access it.

Why?

Because `wrapper` **closes over** `func`.

So after:

```python
printer = dec_decorator(printer)
```

we effectively have:

```text
printer
   │
   ▼
wrapper function
   │
   │ closure
   ▼
func ─────────► original printer function
```

Therefore when you do:

```python
printer()
```

you're actually doing:

```python
wrapper()
```

The wrapper executes:

```python
print("Before")
```

then:

```python
func()
```

and `func` still points to the original `printer`.

So:

```text
printer()
   │
   ▼
wrapper()
   │
   ├── print("Before")
   │
   ├── func()
   │      │
   │      ▼
   │   original printer()
   │      │
   │      ▼
   │   print("Welcome")
   │
   └── print("After")
```

Output:

```text
Before
Welcome
After
```

---

# 7. The most important mental model

When you see:

```python
@dec_decorator
def printer():
    print("Welcome")
```

Don't think:

> "`@` modifies the function."

Instead think:

> **Python creates the function first, passes that function to the decorator, receives another function back, and assigns that returned function to the original function name.**

Conceptually:

```python
def printer():
    print("Welcome")

printer = dec_decorator(printer)
```

That's the core mechanism.

---

# 8. Why does calling `printer()` execute the wrapper?

This is probably the biggest "aha!" moment.

Initially:

```python
printer → original printer
```

After:

```python
printer = dec_decorator(printer)
```

the situation changes:

```python
printer → wrapper
```

Therefore:

```python
printer()
```

means:

```python
wrapper()
```

It does **not** directly call the original function.

Inside the wrapper, however:

```python
func()
```

calls the original function.

So there are actually **two different function objects** involved:

```text
                    decorator
                       │
                       ▼
              ┌─────────────────┐
              │    wrapper      │
              │                 │
printer() ───►│ print("Before") │
              │                 │
              │ func() ─────────┼────► original printer
              │                 │
              │ print("After")  │
              └─────────────────┘
```

---

# 9. What if I write `@modified_function_name`?

Suppose you have:

```python
@modified_function_name
def my_function():
    print("Hello")
```

Python expects `modified_function_name` to be something callable — normally a decorator function.

Conceptually:

```python
def my_function():
    print("Hello")

my_function = modified_function_name(my_function)
```

So the name after `@` is evaluated and used as the **decorator callable**.

For example:

```python
def modify(func):
    def wrapper():
        print("Something extra")
        func()

    return wrapper


@modify
def hello():
    print("Hello")
```

is conceptually:

```python
def hello():
    print("Hello")

hello = modify(hello)
```

---

# 10. What about multiple decorators?

This is where things get even more interesting.

Suppose:

```python
@decorator_one
@decorator_two
def hello():
    print("Hello")
```

It is equivalent to:

```python
def hello():
    print("Hello")

hello = decorator_two(hello)
hello = decorator_one(hello)
```

Notice the order.

The **bottom decorator is applied first**.

You can visualize it as:

```text
original hello
      │
      ▼
decorator_two
      │
      ▼
result
      │
      ▼
decorator_one
      │
      ▼
final hello
```

Therefore when you call:

```python
hello()
```

you enter `decorator_one`'s wrapper first.

---

# 11. One very important distinction

There are two moments you need to keep separate:

### Decoration time

This happens when Python executes the function definition:

```python
@dec_decorator
def printer():
    ...
```

At this point:

```python
printer = dec_decorator(printer)
```

happens.

### Calling time

Later, when you write:

```python
printer()
```

you're calling the **returned wrapper**, not the original function directly.

So:

```text
          DECORATION TIME
                 │
                 ▼
      original function created
                 │
                 ▼
       decorator(original)
                 │
                 ▼
          wrapper returned
                 │
                 ▼
       name points to wrapper
                 │
                 │
                 ▼
           CALLING TIME
                 │
                 ▼
             printer()
                 │
                 ▼
              wrapper()
                 │
                 ▼
           original func()
```

That distinction is the foundation of understanding decorators deeply.

---

### The one line you should remember

Whenever you see:

```python
@some_decorator
def some_function():
    ...
```

read it mentally as:

```python
def some_function():
    ...

some_function = some_decorator(some_function)
```

And then ask yourself:

**"What function does `some_decorator()` return?"**

That returned function is what `some_function()` will actually execute.

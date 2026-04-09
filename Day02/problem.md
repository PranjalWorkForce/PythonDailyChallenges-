

### ✅ Corrected Code

```python
num1 = int(input("Enter the number: "))
num2 = int(input("Enter the number: "))

print(num1 + num2)

# OR
sum = num1 + num2
print(sum)
```

---

### 🔍 Explanation

#### 1. Taking Input

```python
num1 = int(input("Enter the number: "))
```

* `input()` takes user input as a **string** (text).
* `int()` converts that string into an **integer (number)**.
* So if you type `5`, it becomes the number `5` instead of `"5"`.

Same for:

```python
num2 = int(input("Enter the number: "))
```

---

#### 2. Adding Numbers

```python
print(num1 + num2)
```

* Adds `num1` and `num2`.
* Directly prints the result.

---

#### 3. Alternative Way

```python
sum = num1 + num2
print(sum)
```

* First stores the result in a variable called `sum`.
* Then prints it.

---

### ⚠️ Your Mistakes

* Missing closing parentheses `)` in `input()`
* Missing `:` or spacing in the prompt string
* `// OR` is not valid in Python (use `# OR` for comments)

---

### 🧠 Key Idea

* `input()` → gets text
* `int()` → converts to number
* `+` → adds numbers
* `print()` → shows output

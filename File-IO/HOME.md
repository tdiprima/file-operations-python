## Get user's home directory

You can get the user's home directory in Python using the `os` module or the `pathlib` module. Here's how:

### Using `os`:

```python
import os

home_directory = os.path.expanduser("~")
print(home_directory)
```

### Using `pathlib`:

```python
from pathlib import Path

home_directory = Path.home()
print(home_directory)
```

Both methods will give you the path to the current user's home directory. Use whichever fits your style! 😊

---

## Concatenate

You can concatenate the home directory with the rest of a directory string using `os.path.join` or `pathlib`. Here's how:

### Using `os.path.join`:

```python
import os

home_directory = os.path.expanduser("~")
full_path = os.path.join(home_directory, "some", "nested", "directory")
print(full_path)
```

### Using `pathlib`:

```python
from pathlib import Path

home_directory = Path.home()
full_path = home_directory / "some" / "nested" / "directory"
print(full_path)
```

Both methods ensure proper handling of directory separators across different operating systems. Pick the one you like! 😊

<br>

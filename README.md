# python-ripgrep

A Python wrapper for ripgrep, providing fast and efficient text searching capabilities.

## Description

python-ripgrep is a Python package that wraps the functionality of ripgrep, a line-oriented search tool that recursively searches directories for a regex pattern. This package allows you to harness the power and speed of ripgrep directly from your Python code.

## Features

- Fast text searching using ripgrep's algorithms
- Recursive directory searching
- Regular expression support
- Customizable search parameters

## Installation

You can install python-ripgrep using pip:

```
pip install python-ripgrep
```

## Usage

Here's a basic example of how to use python-ripgrep:

```python
from python_ripgrep import search

# Perform a simple search, returning a
# list of string results grouped by file.
results = search(
    patterns=["pattern"],
    paths=["path/to/search"],
    globs=["*.py"],
)

# Process the results
for result in results:
    print(result)
```

## API Reference

The main components of python-ripgrep are:

- `search`: The primary function for performing searches
- `files`: A function for listing files that would be searched (--files equivalent)
- `PySortMode` and `PySortModeKind`: Enums for specifying sort modes

For detailed API documentation, please refer to the source code comments.

## Implementation Details

### Direct Rust Integration

Unlike many other ripgrep bindings for Python, python-ripgrep doesn't shell out to the ripgrep command-line tool. Instead, it reimplements core ripgrep logic in Rust and provides a direct interface to Python. This approach offers several advantages:

1. **Performance**: By avoiding the overhead of creating a new process and parsing stdout, this implementation can be more efficient, especially for large-scale searches or when called frequently.

2. **Fine-grained control**: The library can expose more detailed control over the search process and return structured data directly to Python.

3. **Better integration**: It allows for tighter integration with Python code, making it easier to incorporate into larger Python applications.

### Current Limitations

As of now, the library implements a subset of ripgrep's functionality. The main search options currently supported are:

1. `patterns`: The search patterns to use
2. `paths`: The paths to search in
3. `globs`: File patterns to include or exclude
4. `sort`: Sort mode for search results
5. `max_count`: Maximum number of matches to show

## Implemented Flags

The following is a checklist of ripgrep flags that have been implemented in this Python wrapper:

- [x] `patterns`: Search patterns
- [x] `paths`: Paths to search (default: current directory)
- [x] `globs`: File patterns to include or exclude (default: all non-ignored files)
- [x] `heading`: (Optional) Whether to show file names above matching lines
- [x] `sort`: (Optional) Sort mode for search results
- [x] `max_count`: (Optional) Maximum number of matches to show per file
- [x] `after_context`: (Optional) Number of lines to show after each match
- [x] `before_context`: (Optional) Number of lines to show before each match
- [x] `separator_field_context`: (Optional) Separator between fields in context lines
- [x] `separator_field_match`: (Optional) Separator between fields in matching lines
- [x] `separator_context`: (Optional) Separator between context lines
- [x] `-U, --multiline`: Enable matching across multiple lines
- [x] `-., --hidden`: Search hidden files and directories

The following flags from ripgrep are not yet implemented in this wrapper:

- [ ] `-C, --context`: Show lines before and after each match
- [ ] `--color`: Controls when to use color in output
- [ ] `-c, --count`: Only show the count of matching lines
- [ ] `--debug`: Show debug messages
- [ ] `--dfa-size-limit`: Limit for regex DFA size
- [ ] `-E, --encoding`: Specify the text encoding of files to search
- [ ] `-F, --fixed-strings`: Treat patterns as literal strings
- [ ] `-i, --ignore-case`: Case insensitive search
- [ ] `-v, --invert-match`: Invert matching
- [ ] `-n, --line-number`: Show line numbers
- [ ] `-x, --line-regexp`: Only show matches surrounded by line boundaries
- [ ] `-M, --max-columns`: Don't print lines longer than this limit
- [ ] `--mmap`: Memory map searched files when possible
- [ ] `--no-ignore`: Don't respect ignore files
- [ ] `--no-unicode`: Disable Unicode-aware search
- [ ] `-0, --null`: Print NUL byte after file names
- [ ] `-o, --only-matching`: Print only matched parts of a line
- [ ] `--passthru`: Print both matching and non-matching lines
- [ ] `-P, --pcre2`: Use the PCRE2 regex engine
- [ ] `-p, --pretty`: Alias for --color=always --heading -n
- [ ] `-r, --replace`: Replace matches with the given text
- [ ] `-S, --smart-case`: Smart case search
- [ ] `-s, --case-sensitive`: Case sensitive search
- [ ] `--stats`: Print statistics about the search
- [ ] `-a, --text`: Search binary files as if they were text
- [ ] `-t, --type`: Only search files matching TYPE
- [ ] `-T, --type-not`: Do not search files matching TYPE
- [ ] `-u, --unrestricted`: Reduce the level of "smart" searching
- [ ] `-V, --version`: Print version information
- [ ] `-w, --word-regexp`: Only show matches surrounded by word boundaries
- [ ] `-z, --search-zip`: Search in compressed files

Note that this list may not be exhaustive and some flags might have partial implementations or behave differently from the original ripgrep. Refer to the source code for the most up-to-date information on implemented features.

### Extending Functionality

To add more ripgrep options to the library, you'll need to modify both the Rust and Python sides of the codebase:

1. Update the `PyArgs` struct in `src/ripgrep_core.rs` to include the new option.
2. Modify the `pyargs_to_hiargs` function in the same file to convert the new Python argument to the corresponding ripgrep argument.
3. Update the Python wrapper code to expose the new option to Python users.

For example, to add a new option `case_sensitive`:

1. Add to `PyArgs`:

   ```rust
   pub case_sensitive: Option<bool>,
   ```

2. In `pyargs_to_hiargs`, add:

   ```rust
   if let Some(case_sensitive) = py_args.case_sensitive {
       low_args.case_sensitive = case_sensitive;
   }
   ```

3. Update the Python wrapper to include the new option.

Remember to handle any necessary type conversions between Python and Rust in the `pyargs_to_hiargs` function.

## Development

This project uses [maturin](https://github.com/PyO3/maturin) for building the Python package from Rust code. To set up a development environment:

1. Ensure you have Rust and Python installed
2. Install maturin: `pip install maturin`
3. Clone the repository
4. Run `maturin develop` to build and install the package locally

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Acknowledgements

This project is based on [ripgrep](https://github.com/BurntSushi/ripgrep) by Andrew Gallant.

## Publishing to PyPI

This package uses GitHub Actions for automated publishing. When a new release is created on GitHub, wheels are automatically built for multiple platforms (Linux, macOS, Windows) and published to PyPI.

To publish a new version:

1. Update version in `pyproject.toml` and `Cargo.toml`
2. Commit and push changes
3. Create a new GitHub release with a tag (e.g., `v0.1.0`)
4. GitHub Actions will automatically build and publish to PyPI

---

This project is maintained by [Indent](https://indent.com).

use pyo3::prelude::*;

mod ripgrep_core;
use ripgrep_core::{py_files, py_search, PySortMode, PySortModeKind};

#[pymodule]
fn python_ripgrep(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<PySortMode>()?;
    m.add_class::<PySortModeKind>()?;
    m.add_function(wrap_pyfunction!(py_search, m)?)?;
    m.add_function(wrap_pyfunction!(py_files, m)?)?;
    Ok(())
}

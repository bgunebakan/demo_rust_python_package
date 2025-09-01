use pyo3::prelude::*;
use pyo3::types::PyModule;

#[pyclass]
pub struct Calculator {
    #[pyo3(get, set)]
    pub name: String,
}

#[pymethods]
impl Calculator {
    #[new]
    fn new(name: String) -> Self {
        Calculator { name }
    }

    fn add(&self, a: f64, b: f64) -> f64 {
        a + b
    }

    fn multiply(&self, a: f64, b: f64) -> f64 {
        a * b
    }

    fn sum_list(&self, numbers: Vec<f64>) -> f64 {
        numbers.iter().sum()
    }

    fn __repr__(&self) -> String {
        format!("Calculator(name='{}')", self.name)
    }
}

#[pyfunction]
fn word_count(text: &str) -> usize {
    text.split_whitespace().count()
}

#[pyfunction]
fn reverse_string(text: &str) -> String {
    text.chars().rev().collect()
}

#[pymodule]
fn demo_rust_python_package(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<Calculator>()?;
    m.add_function(wrap_pyfunction!(word_count, m)?)?;
    m.add_function(wrap_pyfunction!(reverse_string, m)?)?;
    Ok(())
}

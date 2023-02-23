# Development notes

## PYPOWER

``runpf`` integrates ``pfsoln`` to solve power flow, and ``rundcpf``is an wrapper of ``runpf``.

### Structure

Note: With packages ``graphviz`` and ``pydeps``, we can have visualize the module dependency.

Module ``runopf``

![alt text](./fig/runopf.svg "Structure of ``runopf``")

Module ``opf``

![alt text](./fig/opf.svg "Structure of ``opf``")

Module ``opf_setup``

![alt text](./fig/opf_setup.svg "Structure of ``opf``")

Module of ``opf_execute``

![alt text](./fig/opf_execute.svg "Structure of ``opf_execute``")

Module of ``pipsopf_solver``

![alt text](./fig/pipsopf_solver.svg "Structure of ``pipsopf_solver``")

Visualize PYPOWER:

```
python /Users/jinningwang/Documents/work/ams/dev/notes/fig/plot_deps.py
```
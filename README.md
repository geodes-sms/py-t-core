# Py-T-Core
Py-T-Core is a Python implementation of the [T-Core](http://rdcu.be/mE8D). T-Core is a framework to building your own domain-specific, custom-built model transformation engines. It offers primitive transformation constructs that can be combined to define and encapsulate reusable model transformation idioms. The user can use existing transformation building blocks from an extensible library or define his own transformation units.

## Features
- Precondition and postcondition patterns to declaratively specify (graph transformation) rules.
- Matching precondition patterns of a rule on an input model.
- Rewriting the model to satisfy the postcondition of a rule.
- Validation of consistent rule applications to detect conflicts and resolve them.
- Manipulation of matches to iterate through them and rollback to previous match states.
- Control of flow of rule applications with choices and concurrency
- Composition mechanisms for structure, reuse & encapsulation

For more information, read [this article.](http://rdcu.be/mE8D)
>`E. Syriani, H. Vangheluwe, and B. LaShomb. T-Core: A Framework for Custom-built Transformation Languages. Software & Systems Modeling: 14(3), pp. 1215-1243 (2015).`

# Distribution
This distribution contains the following files and folders:
- `tc_python`: implementation of most common transformation units (e.g., ARule, FRule, etc.) and other more advanced units (e.g., XRule) in Python
- `t_core`: all primitive transformation operators
- `core`: matching algorithm and Himesis data structure (abstraction over igraph)
- `util`: utility module for common operations
- `examples`: contains a simple transformation example (simply run [main.py](examples/simple/main.py)) and a fully running example of modeling a mutual exclusion problem with four transformations ([InitModel](examples/mutex/InitModel.py), [ALAP](examples/mutex/ALAP.py), [LTS](examples/mutex/LTS.py),[STS](examples/mutex/STS.py))

The source code is licensed under a [GNU LESSER GENERAL PUBLIC LICENSE 3](https://www.gnu.org/licenses/lgpl-3.0.en.html) ![GNU LGPL v3](https://img.shields.io/badge/license-LGPLv3-blue.svg)

# Installation
T-Core is intended to be used as a Python library.
To use T-Core, you need to install:
- Latest version of Python 2.X (see [https://www.python.org/downloads/](https://www.python.org/downloads/))
- igraph (see [http://igraph.org/python/](http://igraph.org/python/))

# Instructions

Most users will use Py-T-Core (the `tc_python` module).
To implement a Py-T-Core transformation, you need the following modules: `core`, `util`, `t_core`, `tc_python`.

T-Core takes as input a input graph to transform, a set of graph transformation rules (pre/postcondition patterns, a.k.a. Left-hand side and Right-hand side).

T-Core operates on a custom data structure called Himesis (see the [article](http://rdcu.be/mE8D) for more information). You can programatically construct a Himesis graph through its API and then call the `compile()` method to serialize it in a Python class that you can later import. However, it is best to generate the graph from our other tool [AToMPM](https://atompm.github.io/) to make sure all the node attributes are well-formed. For example, a Himesis graph must have an attribute `HConstansts.META_MODEL` and `HConstansts.GUID`. Furthermore, the pre- and postcondition graphs must have attributes names prefixed correctly.


# Change log

## Version 1.0
#### By Eugene Syriani (Sep 2014)
- Custom data-structure (Himesis) over igraph
- Very efficient graph matching algorithm
- Pre-defined transformation units for Python (ARule, FRule, etc.)
- Two fully running examples

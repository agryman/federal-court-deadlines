# federal-court-due-date

This project implements the Federal Court rules for how to calculate the 
due date for service and filing of your documents.

Refer to the 
[Federal Court Guidelines
](https://www.fct-cf.gc.ca/en/pages/representing-yourself/deadlines-calculator/guideline)
for an overview of the rules.

This project will be divided into two phases.

## Phase 1

The goal of the first phase will be to develop a reference implementation of the rules in Python. 
This will ensure that we have a correct understanding of the rules.
We have chosen Python because it is a highly-productive development
platform.
However, it may not be the best platform for use in a legal office
environment.

## Phase 2

The second phase of the project will be to package
the rules for use in a legal office setting. 
The packaging must be:
* secure,
* easy to install, and
* easy to use

Our working assumption is that Excel is a suitable platform.
Microsoft recently released support for Python so we may be
able to directly reuse the code developed in Phase 1.
However, Python support in Excel may not be available in the
target legal office.
We may therefore need to reimplement the code as Excel macros.
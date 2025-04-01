# federal-court-deadlines

This project implements the Federal Court of Canada rules for how to calculate 
deadlines for service and filing of documents.

Refer to the 
[Federal Court Guidelines
](https://www.fct-cf.gc.ca/en/pages/representing-yourself/deadlines-calculator/guideline)
for an overview of the rules.

Install this project using the following command:

```bash
pip install git+https://github.com/agryman/federal-court-deadlines.git
```

Access files in this project using URLs like this:

```
https://raw.githubusercontent.com/agryman/federal-court-deadlines/main/notebooks/images/guideline/general-example-3.png
```

## Project Phases

This project will be divided into two phases.

### Phase 1

The goal of the first phase is to develop a reference implementation of the rules in Python. 
This will ensure that I have a correct understanding of the rules.
I have chosen Python because it is a highly-productive development platform.
However, it may not be the best platform for use in a legal office environment.

#### Google Colab

I have investigated the suitability of Google Colab for hosting Jupyter notebooks.
Colab looks very promising.
However, I ran into a problem with the Python `calendar` module.
My initial implementation made use of some features of `calendar`
that were added in Python 3.12. 
This is a problem because at present Colab is using Python 3.11.11.
The fix this I need to:
* downgrade my development environment to Python 3.11.11, and
* implement the missing features of `calendar` in my code.

I installed Python 3.11 using homebrew.
```shell
brew install python@3.11
```

The Python command is:
```shell
/opt/homebrew/bin/python3.11
```

##### Environment-Specific Code

Add the following notebook code cell to install the project only in the
Colab environment:

```
import sys
IN_COLAB = "google.colab" in sys.modules
if IN_COLAB:
    !pip install git+https://github.com/agryman/federal-court-deadlines.git
```

### Phase 2

The second phase of the project will be to package
the rules for use in a legal office setting. 
The packaging must be:
* secure,
* easy to install, and
* easy to use

If Jupyter notebooks are not a suitable way to deliver this capability then
my working assumption is that Excel is a suitable platform.
Microsoft recently released support for Python so I may be
able to directly reuse the code developed in Phase 1.
However, Python support in Excel may not be available in the
target legal office.
At present, it is only available to early adopters so it is unlikely to
be suitable for a legal office.
I may therefore need to reimplement the code as Excel macros.

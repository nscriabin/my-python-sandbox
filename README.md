# Into

A **sandbox** for testing various Python things in your local environment.

To be explicit - this sandbox is not suited for production workloads. There is no project structure, tests, formatters or linters. Just a flexible and configurable environment to quickly execute some Python code and inspect the result.

## Setup

- Install [uv](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer).
- Install the necessary packages - `uv sync`. This will install the version of Python specified in [.python-version](.python-version).

To run Python commands from your uv virtual environment you have multiple choices:

- Prefix every command with `uv run` e.g. `uv run python scripts/basic_pandas_example.py`
- Activate virtual environment shell - `source .venv/bin/activate` - and run any commands from there e.g. `python scripts/basic_pandas_example.py`.
  - To deactivate the virtual environment shell - `deactivate`.
- Some IDEs e.g. VS Code, automatically recognizes that you have a virtual environment setup in the repo. This means that if you are using the terminal inside the IDE you don't need to run `source .venv/bin/activate` or use `uv run`. Python commands will work automatically.

## Adding/changing a package

1. Add/change the package in [pyproject.toml](pyproject.toml).
2. Run `uv sync`.
   1. This will update the `.lock` with the new dependencies but will also update the the dependencies to the latest compatible versions.

N.B. Following [best practices](https://docs.astral.sh/uv/guides/projects/#uvlock), the `.lock` is version controlled to ensure engineers use the same packages in their local development.

## Jupyter Notebooks

For quick and interactive exploration, Jupyter notebooks can be helpful. See [notebooks](notebooks/exploration.ipynb).

N.B. The `ipykernel` is part of [pyproject.toml](/pyproject.toml).

### For VS Code

To use Jupyter notebooks within your VS Code:

1. Install [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) package.
2. Open the `.ipynb` file.
   1. Select Kernel (top right corner) --> `Select Another Kernel... -> Python Environment --> Select your uv venv created in this repo`.
   2. After selecting your uv venv, it will become the first suggested option for other notebooks.

> [!WARNING]
> Jupyter notebooks in VSCode can get very slow. Starting a kernel can take a minute. Sometimes kernels will be restarting for a while. If something, gets stuck, simply `Ctrl+Shift+P --> Developer: Reload Window`. This will restart VS Code, killing all kernels. Things usually work afterwards.

### Standalone Jupyter Notebooks

There is also an [option](https://www.process.st/templates/how-to-setup-a-jupyter-notebook-in-vs-code-virtual-env-kernels/) to run Jupyter Notebooks outside your IDE but using the venv from this repo.
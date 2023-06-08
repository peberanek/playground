# https://www.pyinvoke.org/
from invoke import task


@task(help={"all_files": "Run on all files (not just the staged ones)."})
def linters(ctx, all_files=False):
    """Run code checks and linters on staged files."""
    cmd = "pre-commit run"
    if all_files:
        cmd += " --all-file"
    ctx.run(cmd, pty=True)

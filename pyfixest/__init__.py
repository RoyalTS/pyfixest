# Import modules
from pyfixest import (
    did,
    errors,
    estimation,
    report,
    utils,
)
from pyfixest.did import did2s, event_study, lpdid, panelview

# Import frequently used functions and classes
from pyfixest.estimation import (
    bonferroni,
    feols,
    fepois,
    feglm,
    rwolf,
)
from pyfixest.report import coefplot, dtable, etable, iplot, make_table, summary
from pyfixest.utils import (
    get_data,
    get_ssc,
    ssc,
)

__all__ = [
    "feols",
    "fepois",
    "feglm",
    "etable",
    "dtable",
    "make_table",
    "summary",
    "iplot",
    "coefplot",
    "bonferroni",
    "rwolf",
    "get_data",
    "ssc",
    "get_ssc",
    "did",
    "errors",
    "estimation",
    "report",
    "utils",
    "event_study",
    "lpdid",
    "did2s",
    "panelview",
]

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("pyfixest")
except PackageNotFoundError:
    __version__ = "unknown"

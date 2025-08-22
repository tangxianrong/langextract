# Copyright 2025 Google LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""langextract_edit: Extract structured information from text with LLMs.

This package provides the main extract and visualize functions,
with lazy loading for other submodules accessed via attribute access.
"""

from __future__ import annotations

import importlib
import sys
from typing import Any, Dict

from langextract_edit import visualization
from langextract_edit.extraction import extract as extract_func

__all__ = [
    # Public convenience functions (thin wrappers)
    "extract",
    "visualize",
    # Submodules exposed lazily on attribute access for ergonomics:
    "annotation",
    "data",
    "providers",
    "schema",
    "inference",
    "factory",
    "resolver",
    "prompting",
    "io",
    "visualization",
    "exceptions",
    "core",
    "plugins",
]

_CACHE: Dict[str, Any] = {}


def extract(*args: Any, **kwargs: Any):
  """Top-level API: lx.extract(...)."""
  return extract_func(*args, **kwargs)


def visualize(*args: Any, **kwargs: Any):
  """Top-level API: lx.visualize(...)."""
  return visualization.visualize(*args, **kwargs)


# PEP 562 lazy loading
_LAZY_MODULES = {
    "annotation": "langextract_edit.annotation",
    "chunking": "langextract_edit.chunking",
    "data": "langextract_edit.data",
    "data_lib": "langextract_edit.data_lib",
    "debug_utils": "langextract_edit.core.debug_utils",
    "exceptions": "langextract_edit.exceptions",
    "factory": "langextract_edit.factory",
    "inference": "langextract_edit.inference",
    "io": "langextract_edit.io",
    "progress": "langextract_edit.progress",
    "prompting": "langextract_edit.prompting",
    "providers": "langextract_edit.providers",
    "resolver": "langextract_edit.resolver",
    "schema": "langextract_edit.schema",
    "tokenizer": "langextract_edit.tokenizer",
    "visualization": "langextract_edit.visualization",
    "core": "langextract_edit.core",
    "plugins": "langextract_edit.plugins",
    "registry": "langextract_edit.registry",  # Backward compat - will emit warning
}


def __getattr__(name: str) -> Any:
  if name in _CACHE:
    return _CACHE[name]
  modpath = _LAZY_MODULES.get(name)
  if modpath is None:
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
  module = importlib.import_module(modpath)
  # ensure future 'import langextract_edit.<name>' returns the same module
  sys.modules[f"{__name__}.{name}"] = module
  setattr(sys.modules[__name__], name, module)
  _CACHE[name] = module
  return module


def __dir__():
  return sorted(__all__)

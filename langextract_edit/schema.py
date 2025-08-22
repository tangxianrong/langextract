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

"""Schema compatibility layer.

This module provides backward compatibility for the schema module.
New code should import from langextract_edit.core.schema instead.
"""

from __future__ import annotations

# Re-export core schema items with deprecation warnings
import warnings

from langextract_edit._compat import schema


def __getattr__(name: str):
  """Handle imports with appropriate warnings."""
  core_items = {
      "BaseSchema": ("langextract_edit.core.schema", "BaseSchema"),
      "Constraint": ("langextract_edit.core.schema", "Constraint"),
      "ConstraintType": ("langextract_edit.core.schema", "ConstraintType"),
      "EXTRACTIONS_KEY": ("langextract_edit.core.schema", "EXTRACTIONS_KEY"),
      "FormatModeSchema": ("langextract_edit.core.schema", "FormatModeSchema"),
  }

  if name in core_items:
    mod, attr = core_items[name]
    warnings.warn(
        f"`langextract_edit.schema.{name}` has moved to `{mod}.{attr}`. Please"
        " update your imports. This compatibility layer will be removed in"
        " v2.0.0.",
        FutureWarning,
        stacklevel=2,
    )
    module = __import__(mod, fromlist=[attr])
    return getattr(module, attr)
  elif name == "GeminiSchema":
    return schema.__getattr__(name)

  raise AttributeError(f"module 'langextract_edit.schema' has no attribute '{name}'")

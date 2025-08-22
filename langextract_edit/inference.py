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

"""Language model inference compatibility layer.

This module provides backward compatibility for the inference module.
New code should import from langextract_edit.core.base_model instead.
"""

from __future__ import annotations

from langextract_edit._compat import inference


def __getattr__(name: str):
  """Forward to _compat.inference for backward compatibility."""
  # Handle InferenceType specially since it's defined in _compat
  if name == "InferenceType":
    return inference.InferenceType

  return inference.__getattr__(name)

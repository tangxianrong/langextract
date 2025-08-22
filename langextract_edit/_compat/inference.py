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

"""Compatibility shim for langextract_edit.inference imports."""

from __future__ import annotations

import enum
import warnings


class InferenceType(enum.Enum):
  """Enum for inference types - kept for backward compatibility."""

  ITERATIVE = "iterative"
  MULTIPROCESS = "multiprocess"


def __getattr__(name: str):
  moved = {
      "BaseLanguageModel": ("langextract_edit.core.base_model", "BaseLanguageModel"),
      "ScoredOutput": ("langextract_edit.core.types", "ScoredOutput"),
      "InferenceOutputError": (
          "langextract_edit.core.exceptions",
          "InferenceOutputError",
      ),
      "GeminiLanguageModel": (
          "langextract_edit.providers.gemini",
          "GeminiLanguageModel",
      ),
      "OpenAILanguageModel": (
          "langextract_edit.providers.openai",
          "OpenAILanguageModel",
      ),
      "OllamaLanguageModel": (
          "langextract_edit.providers.ollama",
          "OllamaLanguageModel",
      ),
  }
  if name in moved:
    mod, attr = moved[name]
    warnings.warn(
        f"`langextract_edit.inference.{name}` is deprecated and will be removed in"
        f" v2.0.0; use `{mod}.{attr}` instead.",
        FutureWarning,
        stacklevel=2,
    )
    module = __import__(mod, fromlist=[attr])
    return getattr(module, attr)
  raise AttributeError(name)

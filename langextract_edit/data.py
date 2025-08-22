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

"""Compatibility shim for langextract_edit.data imports.

This module provides backward compatibility for code that imports from
langextract_edit.data. All functionality has moved to langextract_edit.core.data.
"""

from __future__ import annotations

# Re-export everything from core.data for backward compatibility
# pylint: disable=wildcard-import,unused-wildcard-import
from langextract_edit.core.data import *

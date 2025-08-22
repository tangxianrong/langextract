# Backward Compatibility Layer

This directory contains backward compatibility shims for deprecated imports.

## Deprecation Timeline

All code in this directory will be removed in langextract_edit v2.0.0.

## Migration Guide

The following imports are deprecated and should be updated:

### Inference Module
- `from langextract_edit.inference import BaseLanguageModel` → `from langextract_edit.core.base_model import BaseLanguageModel`
- `from langextract_edit.inference import ScoredOutput` → `from langextract_edit.core.types import ScoredOutput`
- `from langextract_edit.inference import InferenceOutputError` → `from langextract_edit.core.exceptions import InferenceOutputError`
- `from langextract_edit.inference import GeminiLanguageModel` → `from langextract_edit.providers.gemini import GeminiLanguageModel`
- `from langextract_edit.inference import OpenAILanguageModel` → `from langextract_edit.providers.openai import OpenAILanguageModel`
- `from langextract_edit.inference import OllamaLanguageModel` → `from langextract_edit.providers.ollama import OllamaLanguageModel`

### Schema Module
- `from langextract_edit.schema import BaseSchema` → `from langextract_edit.core.schema import BaseSchema`
- `from langextract_edit.schema import Constraint` → `from langextract_edit.core.schema import Constraint`
- `from langextract_edit.schema import ConstraintType` → `from langextract_edit.core.schema import ConstraintType`
- `from langextract_edit.schema import EXTRACTIONS_KEY` → `from langextract_edit.core.schema import EXTRACTIONS_KEY`
- `from langextract_edit.schema import GeminiSchema` → `from langextract_edit.providers.schemas.gemini import GeminiSchema`

### Exceptions Module
- All exceptions: `from langextract_edit.exceptions import *` → `from langextract_edit.core.exceptions import *`

### Registry Module
- `from langextract_edit.registry import *` → `from langextract_edit.plugins import *`
- `from langextract_edit.providers.registry import *` → `from langextract_edit.providers.router import *`

## For Contributors

Do not add new code to this directory. All new development should use the canonical imports from `core/` and `providers/`.

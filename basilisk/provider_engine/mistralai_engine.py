import logging
from functools import cached_property

from .base_engine import ProviderAIModel
from .openai_engine import OpenAIEngine, ProviderCapability

log = logging.getLogger(__name__)


class MistralAIEngine(OpenAIEngine):
	capabilities: set[ProviderCapability] = {ProviderCapability.TEXT}

	@cached_property
	def models(self) -> list[ProviderAIModel]:
		"""
		Get models
		"""
		log.debug("Getting MistralAI models")
		# See <https://docs.mistral.ai/getting-started/models/>
		models = [
			ProviderAIModel(
				id="mistral-large-latest",
				# Translators: This is a model description
				description=_(
					"Our flagship model that's ideal for complex tasks that require large reasoning capabilities or are highly specialized (Synthetic Text Generation, Code Generation, RAG, or Agents)"
				),
				context_window=128000,
				max_temperature=1.0,
				default_temperature=0.7,
			),
			ProviderAIModel(
				id="open-mistral-nemo",
				name="Mistral Nemo",
				# Translators: This is a model description
				description=_(
					"A 12B model built with the partnership with Nvidia. It is easy to use and a drop-in replacement in any system using Mistral 7B that it supersedes"
				),
				context_window=128000,
				max_temperature=1.0,
				default_temperature=0.7,
			),
			ProviderAIModel(
				id="codestral-latest",
				name="Codestral",
				# Translators: This is a model description
				description=_(
					"A cutting-edge generative model that has been specifically designed and optimized for code generation tasks, including fill-in-the-middle and code completion"
				),
				context_window=32000,
				max_temperature=1.0,
				default_temperature=0.7,
			),
			ProviderAIModel(
				id="open-mistral-7b",
				name="Mistral 7B",
				# Translators: This is a model description
				description=_(
					"The first dense model released by Mistral AI, perfect for experimentation, customization, and quick iteration"
				),
				context_window=32000,
				max_temperature=1.0,
				default_temperature=0.7,
			),
			ProviderAIModel(
				id="open-mixtral-8x7b",
				name="Mixtral 8x7B",
				# Translators: This is a model description
				description=_(
					"A sparse mixture of experts model. As such, it leverages up to 45B parameters but only uses about 12B during inference, leading to better inference throughput at the cost of more vRAM"
				),
				context_window=32000,
				max_temperature=1.0,
				default_temperature=0.7,
			),
			ProviderAIModel(
				id="open-mixtral-8x22b",
				name="Mixtral 8x22B",
				# Translators: This is a model description
				description=_(
					"A bigger sparse mixture of experts model. As such, it leverages up to 141B parameters but only uses about 39B during inference, leading to better inference throughput at the cost of more vRAM"
				),
				context_window=64000,
				max_temperature=1.0,
				default_temperature=0.7,
			),
			ProviderAIModel(
				id="open-codestral-mamba",
				name="Codestral Mamba",
				# Translators: This is a model description
				description=_(
					"A Mamba 2 language model specialized in code generation"
				),
				context_window=256000,
				max_temperature=1.0,
				default_temperature=0.7,
			),
		]
		return models

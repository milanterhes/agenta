# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_dict import remove_none_from_dict
from ...errors.unprocessable_entity_error import UnprocessableEntityError
from ...types.evaluator import Evaluator
from ...types.evaluator_config import EvaluatorConfig
from ...types.http_validation_error import HttpValidationError

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class EvaluatorsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_evaluators_endpoint(self) -> typing.List[Evaluator]:
        """
        Endpoint to fetch a list of evaluators.

        Returns:
        List[Evaluator]: A list of evaluator objects.

        ---
        from agenta.client import AgentaApi

        client = AgentaApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.evaluators.get_evaluators_endpoint()
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", "evaluators"
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[Evaluator], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_evaluator_configs(self, *, app_id: str) -> typing.List[EvaluatorConfig]:
        """
        Endpoint to fetch evaluator configurations for a specific app.

        Args:
        app_id (str): The ID of the app.

        Returns:
        List[EvaluatorConfigDB]: A list of evaluator configuration objects.

        Parameters:
            - app_id: str.
        ---
        from agenta.client import AgentaApi

        client = AgentaApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.evaluators.get_evaluator_configs(
            app_id="app_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", "evaluators/configs"
            ),
            params=remove_none_from_dict({"app_id": app_id}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[EvaluatorConfig], _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create_new_evaluator_config(
        self,
        *,
        app_id: str,
        name: str,
        evaluator_key: str,
        settings_values: typing.Dict[str, typing.Any],
    ) -> EvaluatorConfig:
        """
        Endpoint to fetch evaluator configurations for a specific app.

        Args:
        app_id (str): The ID of the app.

        Returns:
        EvaluatorConfigDB: Evaluator configuration api model.

        Parameters:
            - app_id: str.

            - name: str.

            - evaluator_key: str.

            - settings_values: typing.Dict[str, typing.Any].
        ---
        from agenta.client import AgentaApi

        client = AgentaApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.evaluators.create_new_evaluator_config(
            app_id="app_id",
            name="name",
            evaluator_key="evaluator_key",
            settings_values={},
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", "evaluators/configs"
            ),
            json=jsonable_encoder(
                {
                    "app_id": app_id,
                    "name": name,
                    "evaluator_key": evaluator_key,
                    "settings_values": settings_values,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(EvaluatorConfig, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_evaluator_config(self, evaluator_config_id: str) -> EvaluatorConfig:
        """
        Endpoint to fetch evaluator configurations for a specific app.

        Returns:
        List[EvaluatorConfigDB]: A list of evaluator configuration objects.

        Parameters:
            - evaluator_config_id: str.
        ---
        from agenta.client import AgentaApi

        client = AgentaApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.evaluators.get_evaluator_config(
            evaluator_config_id="evaluator_config_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"evaluators/configs/{evaluator_config_id}",
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(EvaluatorConfig, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update_evaluator_config(
        self,
        evaluator_config_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        evaluator_key: typing.Optional[str] = OMIT,
        settings_values: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
    ) -> EvaluatorConfig:
        """
        Endpoint to update evaluator configurations for a specific app.

        Returns:
        List[EvaluatorConfigDB]: A list of evaluator configuration objects.

        Parameters:
            - evaluator_config_id: str.

            - name: typing.Optional[str].

            - evaluator_key: typing.Optional[str].

            - settings_values: typing.Optional[typing.Dict[str, typing.Any]].
        ---
        from agenta.client import AgentaApi

        client = AgentaApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.evaluators.update_evaluator_config(
            evaluator_config_id="evaluator_config_id",
        )
        """
        _request: typing.Dict[str, typing.Any] = {}
        if name is not OMIT:
            _request["name"] = name
        if evaluator_key is not OMIT:
            _request["evaluator_key"] = evaluator_key
        if settings_values is not OMIT:
            _request["settings_values"] = settings_values
        _response = self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"evaluators/configs/{evaluator_config_id}",
            ),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(EvaluatorConfig, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete_evaluator_config(self, evaluator_config_id: str) -> bool:
        """
        Endpoint to delete a specific evaluator configuration.

        Args:
        evaluator_config_id (str): The unique identifier of the evaluator configuration.

        Returns:
        bool: True if deletion was successful, False otherwise.

        Parameters:
            - evaluator_config_id: str.
        ---
        from agenta.client import AgentaApi

        client = AgentaApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.evaluators.delete_evaluator_config(
            evaluator_config_id="evaluator_config_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"evaluators/configs/{evaluator_config_id}",
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(bool, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncEvaluatorsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_evaluators_endpoint(self) -> typing.List[Evaluator]:
        """
        Endpoint to fetch a list of evaluators.

        Returns:
        List[Evaluator]: A list of evaluator objects.

        ---
        from agenta.client import AsyncAgentaApi

        client = AsyncAgentaApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        await client.evaluators.get_evaluators_endpoint()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", "evaluators"
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[Evaluator], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_evaluator_configs(
        self, *, app_id: str
    ) -> typing.List[EvaluatorConfig]:
        """
        Endpoint to fetch evaluator configurations for a specific app.

        Args:
        app_id (str): The ID of the app.

        Returns:
        List[EvaluatorConfigDB]: A list of evaluator configuration objects.

        Parameters:
            - app_id: str.
        ---
        from agenta.client import AsyncAgentaApi

        client = AsyncAgentaApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        await client.evaluators.get_evaluator_configs(
            app_id="app_id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", "evaluators/configs"
            ),
            params=remove_none_from_dict({"app_id": app_id}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[EvaluatorConfig], _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create_new_evaluator_config(
        self,
        *,
        app_id: str,
        name: str,
        evaluator_key: str,
        settings_values: typing.Dict[str, typing.Any],
    ) -> EvaluatorConfig:
        """
        Endpoint to fetch evaluator configurations for a specific app.

        Args:
        app_id (str): The ID of the app.

        Returns:
        EvaluatorConfigDB: Evaluator configuration api model.

        Parameters:
            - app_id: str.

            - name: str.

            - evaluator_key: str.

            - settings_values: typing.Dict[str, typing.Any].
        ---
        from agenta.client import AsyncAgentaApi

        client = AsyncAgentaApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        await client.evaluators.create_new_evaluator_config(
            app_id="app_id",
            name="name",
            evaluator_key="evaluator_key",
            settings_values={},
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", "evaluators/configs"
            ),
            json=jsonable_encoder(
                {
                    "app_id": app_id,
                    "name": name,
                    "evaluator_key": evaluator_key,
                    "settings_values": settings_values,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(EvaluatorConfig, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_evaluator_config(self, evaluator_config_id: str) -> EvaluatorConfig:
        """
        Endpoint to fetch evaluator configurations for a specific app.

        Returns:
        List[EvaluatorConfigDB]: A list of evaluator configuration objects.

        Parameters:
            - evaluator_config_id: str.
        ---
        from agenta.client import AsyncAgentaApi

        client = AsyncAgentaApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        await client.evaluators.get_evaluator_config(
            evaluator_config_id="evaluator_config_id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"evaluators/configs/{evaluator_config_id}",
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(EvaluatorConfig, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update_evaluator_config(
        self,
        evaluator_config_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        evaluator_key: typing.Optional[str] = OMIT,
        settings_values: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
    ) -> EvaluatorConfig:
        """
        Endpoint to update evaluator configurations for a specific app.

        Returns:
        List[EvaluatorConfigDB]: A list of evaluator configuration objects.

        Parameters:
            - evaluator_config_id: str.

            - name: typing.Optional[str].

            - evaluator_key: typing.Optional[str].

            - settings_values: typing.Optional[typing.Dict[str, typing.Any]].
        ---
        from agenta.client import AsyncAgentaApi

        client = AsyncAgentaApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        await client.evaluators.update_evaluator_config(
            evaluator_config_id="evaluator_config_id",
        )
        """
        _request: typing.Dict[str, typing.Any] = {}
        if name is not OMIT:
            _request["name"] = name
        if evaluator_key is not OMIT:
            _request["evaluator_key"] = evaluator_key
        if settings_values is not OMIT:
            _request["settings_values"] = settings_values
        _response = await self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"evaluators/configs/{evaluator_config_id}",
            ),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(EvaluatorConfig, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete_evaluator_config(self, evaluator_config_id: str) -> bool:
        """
        Endpoint to delete a specific evaluator configuration.

        Args:
        evaluator_config_id (str): The unique identifier of the evaluator configuration.

        Returns:
        bool: True if deletion was successful, False otherwise.

        Parameters:
            - evaluator_config_id: str.
        ---
        from agenta.client import AsyncAgentaApi

        client = AsyncAgentaApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        await client.evaluators.delete_evaluator_config(
            evaluator_config_id="evaluator_config_id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"evaluators/configs/{evaluator_config_id}",
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(bool, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

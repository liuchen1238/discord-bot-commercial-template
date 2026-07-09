"""Tracks which plugins are loaded and their metadata."""
from dataclasses import dataclass, field


@dataclass
class PluginInfo:
    name: str
    version: str
    commands: list[str] = field(default_factory=list)


class PluginRegistry:
    def __init__(self):
        self._plugins: dict[str, PluginInfo] = {}

    def register(self, info: PluginInfo) -> None:
        self._plugins[info.name] = info

    def get(self, name: str) -> PluginInfo | None:
        return self._plugins.get(name)

    def all(self) -> list[PluginInfo]:
        return list(self._plugins.values())


registry = PluginRegistry()

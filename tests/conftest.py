import importlib.util
import sys
import types
from pathlib import Path


if "html2text" not in sys.modules:
    html2text_stub = types.ModuleType("html2text")

    class _HTML2Text:
        def __init__(self):
            self.ignore_links = False
            self.ignore_images = True
            self.body_width = 0

        def handle(self, html: str) -> str:
            return html

    html2text_stub.HTML2Text = _HTML2Text
    sys.modules["html2text"] = html2text_stub

if "requests" not in sys.modules:
    requests_stub = types.ModuleType("requests")

    def _get(*args, **kwargs):
        raise RuntimeError("requests.get should not be called in unit tests")

    requests_stub.get = _get
    sys.modules["requests"] = requests_stub


def load_src_module(name: str):
    repo_root = Path(__file__).resolve().parents[1]
    module_path = repo_root / "src" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, module_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load module {name} from {module_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

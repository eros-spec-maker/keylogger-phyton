import builtins
import importlib.util
import sys
import types
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "keylogger_educacional.py"


def carregar_app():
    fake_pynput = types.ModuleType("pynput")
    fake_pynput.keyboard = types.SimpleNamespace(Key=object())
    sys.modules["pynput"] = fake_pynput

    spec = importlib.util.spec_from_file_location(
        "keylogger_educacional_test", MODULE_PATH
    )
    app = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(app)
    return app


app = carregar_app()


def test_confirmacao_aceita(monkeypatch):
    monkeypatch.setattr(builtins, "input", lambda *_: "CONCORDO")
    assert app._confirmar() is True


def test_confirmacao_recusada(monkeypatch):
    monkeypatch.setattr(builtins, "input", lambda *_: "NAO")
    assert app._confirmar() is False


def test_confirmacao_ignora_espacos_e_minusculas(monkeypatch):
    monkeypatch.setattr(builtins, "input", lambda *_: "  concordo  ")
    assert app._confirmar() is True


def test_log_grava_em_arquivo_temporario(monkeypatch, tmp_path):
    arquivo = tmp_path / "keylog_teste.txt"
    monkeypatch.setattr(app, "LOG_FILE", str(arquivo))

    app._log("evento de teste")

    conteudo = arquivo.read_text(encoding="utf-8")
    assert "evento de teste" in conteudo
    assert conteudo.endswith("\n")
    assert len(conteudo.splitlines()) == 1

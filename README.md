# Keylogger Educacional (Python)

> **⚠️ AVISO LEGAL E ÉTICO — LEIA ANTES DE USAR**
>
> Este projeto foi criado **exclusivamente para fins educacionais** e de
> conscientização em segurança da informação. O objetivo é demonstrar, de
> forma controlada, como funciona a captura de eventos de teclado em Python.
>
> **É estritamente proibido** o uso deste software em qualquer sistema sem o
> consentimento explícito, informado e documentado do proprietário. O uso
> não autorizado é **ilegal** e **antiético**, podendo configurar crime
> (ex.: interceptação de comunicações, invasão de dispositivo informático).
>
> O autor **não se responsabiliza** por qualquer uso indevido.
> **Use apenas em máquinas virtuais ou sistemas que você possui e controla.**

---

## O que este projeto faz

- Registra teclas pressionadas em um arquivo **local** (`keylog.txt`).
- Inclui **timestamp** por linha para fins de estudo.
- Encerra ao pressionar **ESC**.
- Exige **confirmação explícita** antes de iniciar a captura.

## O que este projeto **NÃO** faz (propositalmente)

- ❌ Não roda em modo stealth / background escondido.
- ❌ Não envia dados por e-mail, rede ou qualquer canal remoto.
- ❌ Não persiste após reinício (sem auto-start).
- ❌ Não ofusca código.
- ❌ Não captura área de transferência, tela ou áudio.

Se você precisa de alguma dessas funcionalidades, **este projeto não é para você**.

## Requisitos

- Python 3.9+
- Sistema operacional com suporte a `pynput` (Linux, macOS, Windows)

## Instalação

```bash
git clone https://github.com/SEU_USUARIO/keylogger-educacional.git
cd keylogger-educacional
python -m venv venv
source venv/bin/activate   # Linux/macOS
# venv\Scripts\activate    # Windows
pip install -r requirements.txt
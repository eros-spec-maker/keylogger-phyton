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
git clone https://github.com/eros-spec-maker/keylogger-phyton.git
cd keylogger-phyton
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
```

## Execução e validação

Execute somente em um ambiente próprio e autorizado:

```bash
python keylogger_educacional.py
```

Leia o aviso exibido e confirme somente se concordar com as
condições de uso. Durante o teste controlado, pressione ESC
para encerrar a captura.

O programa grava os registros localmente em `keylog.txt`.
Confira os resultados apenas no ambiente de laboratório e
não publique nem envie esse arquivo ao GitHub.

## Limitações

O funcionamento da captura de teclado depende do sistema
operacional, das permissões e do ambiente gráfico. A instalação
da dependência, por si só, não garante suporte à captura em
todos os ambientes, incluindo sessões Android/Termux.

# English Flashcards Generator

Gerador automático de flashcards com áudio para estudo de inglês.

Versão atual: **1.3.0**

---

# Recursos

* Geração automática de áudios MP3
* Geração de arquivos CSV para importação no Anki
* Organização por lições
* Backup automático das lições
* Barra de progresso
* Configuração por arquivo JSON
* Registro de logs
* Compatível com Windows

---

# Estrutura do projeto

```
english-flashcards/

├── anki/
├── audios/
├── backup/
├── lessons/
├── logs/
├── scripts/
├── settings/
│   └── settings.json
├── CHANGELOG.md
├── main.py
├── README.md
└── requirements.txt
```

---

# Instalação
# Instalação

git clone <repositorio>

cd english-flashcards-generator

python -m venv .venv

# Windows
.venv\Scripts\activate

pip install -r requirements.txt

python main.py --all

Clone o projeto:

```bash
git clone https://github.com/kassio7812-cop/english-flashcards-generator.git
```

Entre na pasta:

```bash
cd english-flashcards-generator
```

Instale as dependências:

```bash
pip install -r requirements.txt
```
git clone https://github.com/kassio7812-cop/english-flashcards-generator.git

cd english-flashcards-generator

python -m venv .venv

# Windows
.venv\Scripts\activate

pip install -r requirements.txt

python main.py --all
---

# Formato das lições

Cada lição deve ser um arquivo CSV dentro da pasta:

```
lessons/
```

Exemplo:

```
001_greetings.csv
```

Conteúdo:

```csv
id,english,portuguese
1,Hello!,Olá!
2,Good morning.,Bom dia.
3,Good afternoon.,Boa tarde.
```

---

# Executando

Gerar tudo:

```bash
python main.py --all
```

Gerar apenas áudios:

```bash
python main.py --audio
```

Gerar apenas arquivos do Anki:

```bash
python main.py --anki
```

---

# Arquivos gerados

## Áudios

```
audios/
    001_greetings/
        001.mp3
        002.mp3
```

## Arquivos do Anki

```
anki/

001_greetings_import.csv
```

---

# Importando para o Anki

1. Copie todos os arquivos MP3 para a pasta `collection.media` do Anki.
2. No Anki, escolha **Arquivo → Importar**.
3. Selecione o arquivo CSV gerado.
4. Faça o mapeamento dos campos:

* English
* Portuguese
* Audio
* Lesson

O campo **Audio** já é exportado no formato:

```
[sound:001.mp3]
```

---

# Configuração

Arquivo:

```
settings/settings.json
```

Exemplo:

```json
{
    "voice_lang": "en",
    "voice_slow": false,
    "skip_existing_audio": true,
    "create_backup": true,
    "keep_backups": 10,
    "show_progress": true,
    "anki_separator": ",",
    "log_level": "INFO"
}
```

---

# Backup

Antes da geração, as lições podem ser copiadas automaticamente para:

```
backup/
```

---

# Logs

Todos os eventos ficam registrados em:

```
logs/latest.log
```

---

# Tecnologias

* Python
* gTTS
* tqdm

---

# Roadmap

## Versão 2.0

* Importação de TXT
* Importação de PDF
* Importação de DOCX
* Interface gráfica
* Geração automática de lições

---

# Licença

MIT License.
# English Flashcards Generator

Gerador automático de flashcards para estudo de inglês.

## Recursos

- Gerar MP3
- Gerar CSV para Anki
- Organização por lições

## Estrutura

frases/

audios/

anki/

settings/

scripts/

Criar uma lição

python main.py --new 008_animals

Gerar flashcards

python main.py --all
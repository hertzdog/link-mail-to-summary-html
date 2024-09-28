Certo! Ecco il file `README.md` per GitHub con le istruzioni per l'installazione e l'utilizzo del tuo progetto.

---

# Progetto di Riassunto Automatico di Articoli da Email

Questo progetto in Python consente di:

- Estrarre link da email con un'etichetta specifica in Gmail.
- Scaricare e analizzare gli articoli web corrispondenti.
- Generare riassunti e parole chiave utilizzando un modello di linguaggio (LLM) come OpenAI GPT-3.5 o GPT-4.
- Creare pagine HTML per ogni articolo riassunto.
- Generare una pagina indice con tutti gli articoli riassunti, consentendo il filtraggio per parole chiave.
- Suggerire articoli simili basati sul contenuto.

## Caratteristiche

- **Automazione completa**: Dal recupero dei link nelle email alla generazione delle pagine HTML.
- **Utilizzo di LLM**: Riassunti e keywords generati con modelli avanzati di AI.
- **Pagina indice interattiva**: Consente di filtrare gli articoli per parole chiave.
- **Suggerimenti di lettura**: Ogni articolo mostra altri articoli simili.

## Prerequisiti

- **Account Gmail** con accesso IMAP abilitato.
- **Chiave API OpenAI** per utilizzare l'API GPT-3.5 o GPT-4.
- **Anaconda o Miniconda** per gestire l'ambiente Python.

## Installazione

Segui questi passaggi per installare e configurare il progetto:

### 1. Clona il repository

```bash
git clone https://github.com/tuo-username/nome-del-progetto.git
cd nome-del-progetto
```

### 2. Crea l'ambiente Conda

Crea un file chiamato `environment.yml` nella directory principale del progetto con il seguente contenuto:

```yaml
name: articolo_riassunto_env
channels:
  - defaults
  - conda-forge
dependencies:
  - python=3.9
  - beautifulsoup4
  - requests
  - jinja2
  - sqlite
  - scikit-learn
  - spacy
  - pip
  - pip:
    - openai
```

Quindi, crea l'ambiente ed installa le dipendenze:

```bash
conda env create -f environment.yml
```

### 3. Attiva l'ambiente

```bash
conda activate articolo_riassunto_env
```

### 4. Installa il modello di lingua italiana per SpaCy

```bash
python -m spacy download it_core_news_sm
```

### 5. Configura le credenziali

Crea un file `config.py` nella directory principale del progetto e inserisci le tue credenziali:

```python
# config.py

# Configurazione email
EMAIL_ADDRESS = 'il_tuo_indirizzo@gmail.com'
EMAIL_PASSWORD = 'la_tua_password_app'  # Usa una password per le app se hai l'autenticazione a due fattori abilitata

# Configurazione OpenAI API
OPENAI_API_KEY = 'LA_TUA_CHIAVE_API'

# Altre configurazioni
LABEL_NAME = 'ARTICOLI INTERESSANTI'
DATABASE_NAME = 'articoli.db'
```

**Nota:** Non condividere mai le tue credenziali o la tua chiave API pubblicamente. Assicurati che `config.py` sia incluso nel tuo `.gitignore` se utilizzi un sistema di controllo versione.

### 6. Configura l'accesso IMAP per Gmail

- **Abilita l'accesso IMAP** nelle impostazioni del tuo account Gmail.
- **Crea una password per le app** se hai l'autenticazione a due fattori abilitata.

## Utilizzo

### Esecuzione del progetto

Assicurati di essere nella directory principale del progetto e che l'ambiente conda sia attivo.

```bash
python main.py
```

Il programma eseguirà i seguenti passaggi:

1. **Recupero dei link dalle email**: Connette al tuo account Gmail e cerca tutte le email con l'etichetta specificata (`ARTICOLI INTERESSANTI` per default). Estrae i link dal corpo delle email e li salva nel database.

2. **Processamento degli articoli**: Per ogni link non ancora elaborato nel database, scarica il contenuto dell'articolo, genera un riassunto e le parole chiave utilizzando l'API di OpenAI, e crea una pagina HTML per l'articolo.

3. **Generazione della pagina indice**: Crea una pagina `indice.html` che elenca tutti gli articoli riassunti, mostrando la data di sintesi, il titolo (con link alla pagina del riassunto) e le parole chiave. Include una funzione di filtro per le parole chiave.

4. **Suggerimento di articoli simili**: Alla fine di ogni pagina dell'articolo, viene mostrata una sezione "Ti potrebbero interessare" con link ad altri tre articoli simili.

### File generati

- **Pagine HTML degli articoli**: Ogni articolo processato avrà una propria pagina HTML con un nome file parlante (es. `titolo-dell-articolo.html`).
- **Pagina indice**: Un file `indice.html` che elenca tutti gli articoli riassunti e permette il filtraggio per parole chiave.

## Struttura del Progetto

```
progetto/
├── config.py
├── main.py
├── email_processor.py
├── database.py
├── article_processor.py
├── html_generator.py
├── index_generator.py
├── environment.yml
├── templates/
│   ├── article_template.html
│   └── index_template.html
└── README.md
```

## Personalizzazione

- **Etichetta Gmail**: Puoi cambiare l'etichetta usata per filtrare le email modificando il valore di `LABEL_NAME` in `config.py`.
- **Modelli HTML**: I file template per le pagine degli articoli e per la pagina indice si trovano nella cartella `templates/`. Puoi personalizzarli secondo le tue esigenze.

## Limitazioni e Considerazioni

- **Limiti dell'API OpenAI**: L'API ha limiti sulla lunghezza del testo che può essere elaborato. Se il testo estratto dall'articolo è troppo lungo, potresti dover implementare un meccanismo per riassumerlo prima di inviarlo all'API.

- **Costi dell'API OpenAI**: L'utilizzo dell'API di OpenAI potrebbe comportare costi. Assicurati di controllare il tuo utilizzo per evitare spese inattese.

- **Termini di Servizio e Copyright**: Assicurati di rispettare i termini di servizio dei siti web da cui estrai i contenuti e considera le implicazioni legali relative al copyright.

## Risoluzione dei Problemi

- **Errore di autenticazione con Gmail**: Assicurati che l'accesso IMAP sia abilitato e che stai utilizzando una password per le app se hai l'autenticazione a due fattori abilitata.

- **Errori relativi all'API OpenAI**: Verifica che la tua chiave API sia corretta e che tu abbia credito sufficiente nel tuo account OpenAI.

- **Problemi con le dipendenze**: Assicurati che l'ambiente conda sia attivo e che tutte le dipendenze siano installate correttamente.

## Contributi

I contributi sono benvenuti! Sentiti libero di aprire issue o pull request per migliorare il progetto.

## Licenza

Questo progetto è distribuito sotto la licenza MIT. Vedi il file [LICENSE](LICENSE) per maggiori dettagli.

## Contatti

Per domande o supporto, puoi contattare ad@ht-x.com 


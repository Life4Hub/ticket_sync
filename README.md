# ticket-sync

## Projektbeschreibung
Entwicklung einer Schnittstelle zur Synchronisation von Ticket relevanten Daten zwischen verschiedenen internen Ticketsystemen.

### Ziel
Das Ziel des Projekts ist es, eine Schnittstelle zu entwickeln, die zwischen drei Ticketsystemen (Salesforce, ServiceNow und Polarion) agiert. Diese Schnittstelle ermöglicht das Synchronisieren von Änderungen, Zeitangaben und Kommentaren vom Kunden sowie die Dokumentation von Arbeitsprozessen im Ticket.

## Ist-Zustand
- Zuvor einheitlich genutztes Ticketsystem (ServiceNow) wurde aufgeteilt.
- Abteilungen (Support, Admin, R&D) arbeiten isoliert mit eigenen Ticketsystemen.
- Informationsaustausch erfolgt manuell (E-Mails, mündliche Absprachen, Microsoft Teams).
- Verzögerungen, Inkonsistenzen und erhöhter Arbeitsaufwand.
- Schwierigkeiten bei Eskalationen und Analysen.
- Direkte Auswirkungen auf Kundenzufriedenheit und Wettbewerbsfähigkeit.

## Soll-Konzept
- Effizienter Informationsaustausch in Echtzeit zwischen Abteilungen.
- Automatisierung und Standardisierung des Prozesses.
- Mock-Services zur Simulation der Kommunikation zwischen Systemen.
- Event-Trigger zur Verarbeitung von Statusänderungen.
- Nutzung einer SQLite-Datenbank als Zwischenspeicher.
- Validierungsmechanismen zur Sicherstellung der Datenqualität.
- Monitoring-Prozess mit automatischer Fehlererfassung und Benachrichtigung.

## Projektumfeld
- **Entwicklungsumgebung:** Visual Studio Code.
- **Mocking:** Rancher.
- **Programmiersprache:** Python.
- **Kommunikationsschnittstelle:** REST API.
- **Datenbank:** SQLite.
- **Versionskontrolle:** GitHub.
- **Qualitätssicherung:** Unit-Tests.

## Projektphasen / Zeitplanung

### 1. Informationsphase (8 Stunden)
- Ist-Analyse (2 Stunden)
- Soll-Konzept (2 Stunden)
- Analyse der Schnittstellen der Ticketsysteme (4 Stunden)

### 2. Planung (10 Stunden)
- Sequenzdiagramm für die Kommunikation zwischen den Ticketsystemen (3 Stunden)
- Festlegung des Benachrichtigungssystems (2 Stunden)
- Mock-up für Monitoring-Oberfläche (1 Stunde)
- Ermittlung der technischen Rahmenbedingungen (2 Stunden)
- ERM der Datenbank entwerfen (2 Stunden)

### 3. Durchführung (35 Stunden)
- Implementierung der REST-Schnittstelle (10 Stunden)
- Erstellung der Mock-Systeme (15 Stunden)
- Implementierung des Monitorings (3 Stunden)
- Benachrichtigungs-Mail für Fehler erstellen (2 Stunden)
- Erstellung der Datenbank (5 Stunden)

### 4. Kontrolle (27 Stunden)
- Unit-Tests (14 Stunden)
- Erstellung der Projektdokumentation (13 Stunden)

## Setup

### MySQL Configuration

1. Install MySQL and create a database:
   ```sql
   CREATE DATABASE ticket_sync;
   ```

2. Create a user and grant privileges:
   ```sql
   CREATE USER 'your_username'@'localhost' IDENTIFIED BY 'your_password';
   GRANT ALL PRIVILEGES ON ticket_sync.* TO 'your_username'@'localhost';
   FLUSH PRIVILEGES;
   ```

3. Update the `database.py` file with your MySQL credentials.

### Initialize the Database

Run the following command to initialize the database:
```bash
python -c "from database import init_db; init_db()"
```

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd ticket-sync
   ```

2. Install dependencies:
   ```bash
   pip install flask
   ```

3. Initialize the database:
   ```bash
   python -c "from database import init_db; init_db()"
   ```

4. Run the application:
   ```bash
   python main.py
   ```

5. Access the API at `http://127.0.0.1:5000/`.
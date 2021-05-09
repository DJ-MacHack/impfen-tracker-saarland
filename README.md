# Impf-Tracker-Saarland

In diesem Repo finden Sie einen Impfplatztracker (inkl. paralleler Version) und einen Klickbot mit einem Helfertool. Mit den hier angebotetenen Programmen können Sie sich im Saarland schnell und einfach einen Impfplatz verschaffen. 


# Vorraussetzungen

 - Python 3.9.1
 - selenium
 - chromedriver
 - pyautogui
 - keyboard
 - pywin32

# Achtung

Alle Pixelangaben sind abhängig von Ihrer Auflösung, Ihrem Browser und dem Zoom! Wahrscheinlich müssen Sie diese anpassen!
Unsere Einstellungen sind Windows 10 - Google Chrome 90 - 1920x1080 - Zoom: 100%

## autobot.py

Klickt wenn Sie sich auf [Saarland Impflisten Login](https://impfen-saarland.de/service/login) authentifiziert und Ihren Namen gewählt haben, automatisch so lange bis Sie einen Termin für Ihr [Impfzentrum](https://impfen-saarland.de/service/waitlist_entries) haben. **Standardmäßig ist Lebach - Nacht gewählt.**

## clickbot.py

Hat uns die Screenshots **nothing.png** und **screen.png** aufgenommen zum anpassen.

## coronajson.py

Geht durch die API und zeigt jede Sekunde an, welche Termine wann in welchem Impfzentrum frei sind.

## coronajsonpara.py

Wie coronajson.py nur parallelisiert.


# Codeanpassungen
Ändern Sie den Code so viel Sie möchten unter der Bedingung, dass Sie damit keine Impftermine verkaufen. Nur für den privaten nicht kommerziellen Gebrauch gestattet. Bitte beachtet den Fair-Use-Aspekt, dass die Website der Impfplatzvergabe nicht dauerhaft DDosed wird. Danke für Ihre Ehrlichkeit.

# Verbesserungen und Vorschläge
Jeder Verbesserungsvorschlag oder Bug-Report im Issues-Bereich wird reviewed und ggf. verfolgt und implementiert.

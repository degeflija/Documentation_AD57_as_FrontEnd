/**
 * @verbatim
 *

Pflichtenheft für das AUDIO im neuen Vario :
============================================

Ausgabe von in Tonhöhe und Lautstärke regelbarer Töne und diverser Signal-Töne

  // Audio Input Queue definition
  //
  typedef struct
  {
    uint16_t  Signal_Id;
    uint16_t  Signal_Volume;
    uint16_t  Audio_Volume;
    float     Audio_Frequency;
    uint16_t  Audio_On_IntVal;
    uint16_t  Audio_Off_IntVal;

  } AudioQItem_t;


Tonhöhe steuerbar über einen linearen Parameter "Audio_Frequency" mit der Range -2.0 bis +2.0 .

Dabei soll der Wert -2.0 eine Frequenz von 300 Hz erzeugen, der Wert +2.0 soll der
Frequenz 3000 Hz entsprechen.
Der Wert 0 entspricht der Null im Vario und der Mittenfrequenz, ca 900 Hz.
Die Steuerung der Frequenz soll einen physiologisch wahrnehmbar
gleichmäßigen Frequenzanstieg erzeugen.

Lautstärke steuerbar zwischen Ton-Aus und dem Maximum, was die
Aussteuerung hergibt (Parameter "Audio_Volume").
Die Steuerung der Lautstärke soll den linearen Anstieg des Eingangswert
zwischen 0 und 100 (%) abbilden auf einen physiologisch wahrnehmbar
gleichmäßigen Anstieg der Lautstärke.

Wenn aus der Ansteuerungslogik heraus das Audio getaktet wird
( "Audio_On_IntVal"  und "Audio_Off_IntVal" in msec).
dann soll das Audio in der Lage sein, den Volume-Sprung  (zB  0 auf 50 oder 90 auf 0 ) zu an-
und abschwellen zu lassen.

Die Zeit des Einschwingens auf den neuen Volume-Wert muss experimentell
herausgefunden werden. Das war nach meinen Aufzeichnungen (Albatros) zuletzt ca. ¼ Sekunde.
Ich würde diesen Wert jedoch nicht in Stein meißeln wollen.

Analog dazu wollte ich dann auch noch die Frequenzsteuerung glätten,
weil die Frequenzsprünge mein Hörempfinden beleidigt haben. Dazu kam ich
nicht mehr.

Die Steuerung der Ton-Ausgabe erfolgt alle 50-100 (?) msec.

Das Audio soll inherent über einen Vorrat von vorfabrizierten Signalen verfügen,
die nach Id und Volume gesteuert werden können.


 *
 * * @endverbatim
 */

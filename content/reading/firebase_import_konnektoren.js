#!/usr/bin/env node
/**
 * Firebase Import: B2 Topic 1 (Konnektoren) — 96 Questions
 * Collection: moduleQuizQuestions
 * 
 * Run: node firebase_import_konnektoren.js
 * Requires: Firestore rules set to allow read/write
 */

const https = require('https');

const PROJECT_ID = 'b2-deutsch-app';
const API_KEY = 'AIzaSyDHUwnlKx-ArzA5yZD4WhXI5sfACTzkedc';

// 96 Questions for B2 Topic 1: Konnektoren
const questions = [
  // === ALS (12) ===
  { id: 'b2_01_als_q001', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'als', questionText: '___ ich in Deutschland ankam, konnte ich kein Deutsch.', options: ['Wenn', 'Als', 'Während', 'Bevor'], correctAnswer: 'Als', explanation: '"Als" wird für einmalige Situationen in der Vergangenheit verwendet. Beispiel: Als ich in Deutschland ankam, sprach ich kein Deutsch.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_als_q002', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'als', questionText: '___ ich gestern nach Hause kam, hat es geregnet.', options: ['Bevor', 'Als', 'Bis', 'Während'], correctAnswer: 'Als', explanation: '"Als" wird für einmalige vergangene Handlungen verwendet.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_als_q003', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'als', questionText: '___ ich ein Kind war, habe ich in Istanbul gelebt.', options: ['Wenn', 'Während', 'Als', 'Seitdem'], correctAnswer: 'Als', explanation: '"Als" beschreibt eine einmalige Situation in der Kindheit.', difficulty: 'medium', level: 'B2' },
  { id: 'b2_01_als_q004', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'als', questionText: '___ ich die Nachricht gelesen habe, war ich sehr überrascht.', options: ['Während', 'Als', 'Bevor', 'Sobald'], correctAnswer: 'Als', explanation: '"Als" zeigt eine abgeschlossene Handlung in der Vergangenheit.', difficulty: 'medium', level: 'B2' },
  { id: 'b2_01_als_q005', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'als', questionText: '___ er 2019 nach Deutschland kam, sprach er nur Türkisch.', options: ['Seitdem', 'Als', 'Wenn', 'Während'], correctAnswer: 'Als', explanation: '"Als" wird für einmalige vergangene Ereignisse mit Jahreszahlen verwendet.', difficulty: 'medium', level: 'B2' },
  { id: 'b2_01_als_q006', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'als', questionText: '___ ich mich umgedreht habe, war niemand mehr da.', options: ['Sobald', 'Als', 'Bis', 'Solange'], correctAnswer: 'Als', explanation: '"Als" beschreibt eine plötzliche, einmalige Handlung in der Vergangenheit.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_als_q007', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'als', questionText: '___ wir in München ankamen, hat es geschneit.', options: ['Während', 'Als', 'Bevor', 'Wenn'], correctAnswer: 'Als', explanation: '"Als" wird bei der Ankunft an einem Ort verwendet.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_als_q008', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'als', questionText: '___ ich jünger war, habe ich viel Fußball gespielt.', options: ['Wenn', 'Als', 'Seitdem', 'Während'], correctAnswer: 'Als', explanation: '"Als" beschreibt eine Lebensphase in der Vergangenheit.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_als_q009', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'als', questionText: '___ ich die Tür geöffnet habe, sah ich meinen alten Freund.', options: ['Bevor', 'Als', 'Bis', 'Sobald'], correctAnswer: 'Als', explanation: '"Als" zeigt eine plötzliche Begegnung in der Vergangenheit.', difficulty: 'medium', level: 'B2' },
  { id: 'b2_01_als_q010', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'als', questionText: '___ sie ihren Abschluss gemacht hatte, begann sie zu arbeiten.', options: ['Als', 'Während', 'Wenn', 'Solange'], correctAnswer: 'Als', explanation: '"Als" zeigt eine Abfolge von zwei vergangenen Handlungen.', difficulty: 'medium', level: 'B2' },
  { id: 'b2_01_als_q011', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'als', questionText: '___ ich zum ersten Mal in Berlin war, habe ich das Brandenburger Tor besucht.', options: ['Während', 'Als', 'Bevor', 'Wenn'], correctAnswer: 'Als', explanation: '"Als" wird für die erste Erfahrung an einem Ort verwendet.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_als_q012', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'als', questionText: '___ wir das Angebot erhalten haben, haben wir sofort geantwortet.', options: ['Als', 'Sobald', 'Während', 'Wenn'], correctAnswer: 'Als', explanation: '"Als" zeigt eine schnelle Reaktion auf ein vergangenes Ereignis.', difficulty: 'hard', level: 'B2' },

  // === BEVOR (12) ===
  { id: 'b2_01_bevor_q001', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'bevor', questionText: 'Ich lerne Deutsch, ___ ich nach Deutschland gehe.', options: ['Als', 'Während', 'Bevor', 'Wenn'], correctAnswer: 'Bevor', explanation: '"Bevor" bedeutet "önce" auf Türkisch. Die Handlung danach ist der Hauptpunkt.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_bevor_q002', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'bevor', questionText: '___ du gehst, mache bitte die Tür zu.', options: ['Als', 'Bevor', 'Während', 'Bis'], correctAnswer: 'Bevor', explanation: '"Bevor" zeigt die Handlung, die zuerst kommt.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_bevor_q003', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'bevor', questionText: 'Er ruft an, ___ er zu uns kommt.', options: ['Während', 'Bevor', 'Sobald', 'Als'], correctAnswer: 'Bevor', explanation: '"Bevor" bedeutet, dass die Handlung im Nebensatz zuerst kommt.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_bevor_q004', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'bevor', questionText: '___ du ins Bett gehst, solltest du die Zähne putzen.', options: ['Während', 'Bevor', 'Nachdem', 'Als'], correctAnswer: 'Bevor', explanation: '"Bevor" zeigt eine Routine-Handlung vor dem Schlafen.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_bevor_q005', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'bevor', questionText: 'Sie hat alles vorbereitet, ___ die Gäste ankamen.', options: ['Bevor', 'Während', 'Als', 'Wenn'], correctAnswer: 'Bevor', explanation: '"Bevor" zeigt, dass die Vorbereitung vor dem Eintreffen der Gäste geschah.', difficulty: 'medium', level: 'B2' },
  { id: 'b2_01_bevor_q006', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'bevor', questionText: '___ du etwas kaufst, vergleiche bitte die Preise.', options: ['Während', 'Bevor', 'Nachdem', 'Sobald'], correctAnswer: 'Bevor', explanation: '"Bevor" gibt einen Rat vor dem Einkauf.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_bevor_q007', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'bevor', questionText: 'Ich möchte mit dir sprechen, ___ du gehst.', options: ['Als', 'Bevor', 'Während', 'Wenn'], correctAnswer: 'Bevor', explanation: '"Bevor" zeigt die Dringlichkeit des Gesprächs vor dem Gehen.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_bevor_q008', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'bevor', questionText: '___ du das Auto fährst, schnalle dich bitte an.', options: ['Während', 'Bevor', 'Nachdem', 'Als'], correctAnswer: 'Bevor', explanation: '"Bevor" gibt eine Sicherheitsanweisung vor dem Fahren.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_bevor_q009', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'bevor', questionText: 'Er hat lange gearbeitet, ___ er Urlaub gemacht hat.', options: ['Während', 'Bevor', 'Nachdem', 'Als'], correctAnswer: 'Bevor', explanation: '"Bevor" zeigt die Reihenfolge: Arbeit kam vor dem Urlaub.', difficulty: 'medium', level: 'B2' },
  { id: 'b2_01_bevor_q010', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'bevor', questionText: '___ du eine E-Mail schreibst, prüfe bitte die Rechtschreibung.', options: ['Während', 'Bevor', 'Sobald', 'Wenn'], correctAnswer: 'Bevor', explanation: '"Bevor" gibt einen Tipp vor dem Schreiben.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_bevor_q011', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'bevor', questionText: 'Wir müssen das Formular ausfüllen, ___ wir einreisen dürfen.', options: ['Während', 'Bevor', 'Nachdem', 'Während'], correctAnswer: 'Bevor', explanation: '"Bevor" zeigt die Voraussetzung für die Einreise.', difficulty: 'medium', level: 'B2' },
  { id: 'b2_01_bevor_q012', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'bevor', questionText: '___ du das Essen zubereitest, wasche dir bitte die Hände.', options: ['Sobald', 'Bevor', 'Während', 'Wenn'], correctAnswer: 'Bevor', explanation: '"Bevor" gibt eine Hygieneanweisung vor dem Kochen.', difficulty: 'easy', level: 'B2' },

  // === BIS (12) ===
  { id: 'b2_01_bis_q001', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'bis', questionText: 'Ich warte hier, ___ du fertig bist.', options: ['Während', 'Bis', 'Bevor', 'Sobald'], correctAnswer: 'Bis', explanation: '"Bis" zeigt den Endpunkt einer Handlung. Man wartet bis etwas passiert.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_bis_q002', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'bis', questionText: 'Er blieb im Büro, ___ sein Chef kam.', options: ['Während', 'Bis', 'Bevor', 'Als'], correctAnswer: 'Bis', explanation: '"Bis" zeigt die Zeitgrenze — er blieb bis zur Ankunft des Chefs.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_bis_q003', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'bis', questionText: '___ ich Zeit habe, kann ich dir helfen.', options: ['Während', 'Bis', 'Bevor', 'Sobald'], correctAnswer: 'Bis', explanation: '"Bis" zeigt hier die Bedingung — bis ich Zeit habe.', difficulty: 'medium', level: 'B2' },
  { id: 'b2_01_bis_q004', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'bis', questionText: 'Sie las das Buch, ___ sie eingeschlafen ist.', options: ['Während', 'Bis', 'Bevor', 'Wenn'], correctAnswer: 'Bis', explanation: '"Bis" zeigt den Endpunkt — sie las bis zum Einschlafen.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_bis_q005', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'bis', questionText: '___ der Arzt kommt, musst du im Bett bleiben.', options: ['Während', 'Bis', 'Bevor', 'Sobald'], correctAnswer: 'Bis', explanation: '"Bis" zeigt die Anweisung bis zum Eintreffen des Arztes.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_bis_q006', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'bis', questionText: 'Wir haben gewartet, ___ der Zug angekommen ist.', options: ['Während', 'Bis', 'Bevor', 'Sobald'], correctAnswer: 'Bis', explanation: '"Bis" zeigt die Zeitgrenze des Wartens.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_bis_q007', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'bis', questionText: 'Er sprach nicht, ___ er die Wahrheit erfahren hatte.', options: ['Während', 'Bis', 'Bevor', 'Nachdem'], correctAnswer: 'Bis', explanation: '"Bis" zeigt den Zeitpunkt, ab dem er sprach — als er die Wahrheit erfuhr.', difficulty: 'medium', level: 'B2' },
  { id: 'b2_01_bis_q008', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'bis', questionText: '___ alle Gäste gegangen waren, haben wir aufgeräumt.', options: ['Während', 'Bis', 'Bevor', 'Sobald'], correctAnswer: 'Bis', explanation: '"Bis" zeigt den Endpunkt — aufgeräumt wurde nach dem Gehen der Gäste.', difficulty: 'medium', level: 'B2' },
  { id: 'b2_01_bis_q009', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'bis', questionText: 'Ich werde warten, ___ du zurückkommst.', options: ['Während', 'Bis', 'Bevor', 'Sobald'], correctAnswer: 'Bis', explanation: '"Bis" zeigt den Endpunkt des Wartens.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_bis_q010', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'bis', questionText: '___ das Spiel zu Ende war, haben wir geklatscht.', options: ['Während', 'Bis', 'Bevor', 'Wenn'], correctAnswer: 'Bis', explanation: '"Bis" zeigt den Zeitpunkt des Klatschens — als das Spiel endete.', difficulty: 'medium', level: 'B2' },
  { id: 'b2_01_bis_q011', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'bis', questionText: 'Das Kind blieb ruhig, ___ seine Mutter kam.', options: ['Während', 'Bis', 'Bevor', 'Sobald'], correctAnswer: 'Bis', explanation: '"Bis" zeigt den Zeitpunkt der Veränderung — als die Mutter kam.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_bis_q012', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'bis', questionText: '___ der Film begann, haben wir Popcorn gekauft.', options: ['Während', 'Bis', 'Bevor', 'Nachdem'], correctAnswer: 'Bis', explanation: '"Bis" zeigt die Zeit vor dem Beginn — wir kauften Popcorn davor.', difficulty: 'medium', level: 'B2' },

  // === SEITDEM (12) ===
  { id: 'b2_01_seitdem_q001', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'seitdem', questionText: '___ ich in Berlin wohne, fühle ich mich sehr wohl.', options: ['Als', 'Während', 'Seitdem', 'Bevor'], correctAnswer: 'Seitdem', explanation: '"Seitdem" zeigt eine Handlung, die in der Vergangenheit begann und immer noch andauert.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_seitdem_q002', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'seitdem', questionText: '___ er mit dem Rauchen aufgehört hat, fühlt er sich besser.', options: ['Bevor', 'Seitdem', 'Wenn', 'Während'], correctAnswer: 'Seitdem', explanation: '"Seitdem" zeigt die Veränderung nach dem Aufhören einer Gewohnheit.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_seitdem_q003', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'seitdem', questionText: '___ sie in Deutschland lebt, spricht sie fließend Deutsch.', options: ['Während', 'Seitdem', 'Bevor', 'Als'], correctAnswer: 'Seitdem', explanation: '"Seitdem" zeigt die kontinuierliche Verbesserung seit einem Zeitpunkt.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_seitdem_q004', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'seitdem', questionText: '___ ich mit dem Kurs angefangen habe, gehe ich jeden Tag zur Schule.', options: ['Als', 'Seitdem', 'Während', 'Bevor'], correctAnswer: 'Seitdem', explanation: '"Seitdem" zeigt die neue Routine seit dem Start des Kurses.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_seitdem_q005', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'seitdem', questionText: 'Er ist nicht mehr nervös, ___ er regelmäßig meditiert.', options: ['Während', 'Seitdem', 'Bevor', 'Wenn'], correctAnswer: 'Seitdem', explanation: '"Seitdem" zeigt die positive Veränderung nach einer Gewohnheit.', difficulty: 'medium', level: 'B2' },
  { id: 'b2_01_seitdem_q006', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'seitdem', questionText: '___ wir umgezogen sind, kennen wir viele neue Leute.', options: ['Während', 'Seitdem', 'Bevor', 'Als'], correctAnswer: 'Seitdem', explanation: '"Seitdem" zeigt die Veränderung im sozialen Leben nach dem Umzug.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_seitdem_q007', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'seitdem', questionText: '___ du mir geholfen hast, ist alles viel einfacher geworden.', options: ['Während', 'Seitdem', 'Bevor', 'Als'], correctAnswer: 'Seitdem', explanation: '"Seitdem" zeigt die Verbesserung nach der Hilfe.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_seitdem_q008', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'seitdem', questionText: '___ sie eine neue Stelle gefunden hat, ist sie viel glücklicher.', options: ['Bevor', 'Seitdem', 'Während', 'Wenn'], correctAnswer: 'Seitdem', explanation: '"Seitdem" zeigt die emotionale Veränderung nach dem Jobwechsel.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_seitdem_q009', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'seitdem', questionText: '___ ich 2023 umgezogen bin, wohne ich in einer größeren Wohnung.', options: ['Während', 'Seitdem', 'Bevor', 'Wenn'], correctAnswer: 'Seitdem', explanation: '"Seitdem" zeigt die andauernde Situation nach dem Umzug.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_seitdem_q010', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'seitdem', questionText: '___ er in Hamburg wohnt, arbeitet er bei einer großen Firma.', options: ['Während', 'Seitdem', 'Bevor', 'Als'], correctAnswer: 'Seitdem', explanation: '"Seitdem" zeigt die Verknüpfung zweier andauernder Situationen.', difficulty: 'medium', level: 'B2' },
  { id: 'b2_01_seitdem_q011', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'seitdem', questionText: 'Ich bin nicht mehr müde, ___ ich früher ins Bett gehe.', options: ['Während', 'Seitdem', 'Bevor', 'Wenn'], correctAnswer: 'Seitdem', explanation: '"Seitdem" zeigt die positive Veränderung nach einer Gewohnheitsänderung.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_seitdem_q012', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'seitdem', questionText: '___ wir uns kennengelernt haben, schreiben wir uns fast jeden Tag.', options: ['Während', 'Seitdem', 'Bevor', 'Als'], correctAnswer: 'Seitdem', explanation: '"Seitdem" zeigt die andauernde Gewohnheit seit dem Kennenlernen.', difficulty: 'easy', level: 'B2' },

  // === WÄHREND (12) ===
  { id: 'b2_01_wahrend_q001', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'während', questionText: '___ sie kocht, hört sie Musik.', options: ['Bevor', 'Während', 'Nachdem', 'Bis'], correctAnswer: 'Während', explanation: '"Während" zeigt zwei Handlungen, die gleichzeitig passieren.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_wahrend_q002', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'während', questionText: '___ er im Büro war, hat seine Frau angerufen.', options: ['Bevor', 'Während', 'Nachdem', 'Wenn'], correctAnswer: 'Während', explanation: '"Während" zeigt eine Handlung, die während einer anderen passiert.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_wahrend_q003', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'während', questionText: 'Ich habe gelernt, ___ mein Bruder ferngesehen hat.', options: ['Bevor', 'Während', 'Nachdem', 'Sobald'], correctAnswer: 'Während', explanation: '"Während" zeigt parallele Handlungen zweier Personen.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_wahrend_q004', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'während', questionText: '___ sie auf den Bus gewartet hat, hat sie ein Buch gelesen.', options: ['Bevor', 'Während', 'Nachdem', 'Als'], correctAnswer: 'Während', explanation: '"Während" zeigt zwei simultane Handlungen beim Warten.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_wahrend_q005', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'während', questionText: '___ ich in der Küche stand, habe ich das Fenster aufgemacht.', options: ['Bevor', 'Während', 'Nachdem', 'Sobald'], correctAnswer: 'Während', explanation: '"Während" zeigt eine Handlung, die während einer anderen Situation geschah.', difficulty: 'medium', level: 'B2' },
  { id: 'b2_01_wahrend_q006', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'während', questionText: 'Er hat Kaffee getrunken, ___ er die Zeitung gelesen hat.', options: ['Bevor', 'Während', 'Nachdem', 'Wenn'], correctAnswer: 'Während', explanation: '"Während" zeigt zwei entspannende Handlungen gleichzeitig.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_wahrend_q007', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'während', questionText: '___ mein Mann kocht, räume ich die Wohnung auf.', options: ['Bevor', 'Während', 'Nachdem', 'Als'], correctAnswer: 'Während', explanation: '"Während" zeigt zwei verschiedene Personen bei gleichzeitigen Haushaltsaufgaben.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_wahrend_q008', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'während', questionText: 'Das Kind hat geweint, ___ die Mutter es gewickelt hat.', options: ['Bevor', 'Während', 'Nachdem', 'Bis'], correctAnswer: 'Während', explanation: '"Während" zeigt die Gleichzeitigkeit von Unruhe und Pflege.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_wahrend_q009', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'während', questionText: '___ sie im Krankenhaus lag, hat sie viele Bücher gelesen.', options: ['Bevor', 'Während', 'Nachdem', 'Sobald'], correctAnswer: 'Während', explanation: '"Während" zeigt eine Handlung während eines Krankenhausaufenthalts.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_wahrend_q010', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'während', questionText: 'Ich habe mir Notizen gemacht, ___ der Professor gesprochen hat.', options: ['Bevor', 'Während', 'Nachdem', 'Wenn'], correctAnswer: 'Während', explanation: '"Während" zeigt konzentriertes Zuhören und gleichzeitiges Schreiben.', difficulty: 'medium', level: 'B2' },
  { id: 'b2_01_wahrend_q011', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'während', questionText: '___ die Sonne unterging, saßen wir auf der Terrasse.', options: ['Bevor', 'Während', 'Nachdem', 'Als'], correctAnswer: 'Während', explanation: '"Während" zeigt eine Handlung, die während eines Naturereignisses geschieht.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_wahrend_q012', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'während', questionText: '___ du mit dem Hund gehst, nimm bitte eine Leine mit.', options: ['Bevor', 'Während', 'Nachdem', 'Sobald'], correctAnswer: 'Während', explanation: '"Während" zeigt die Begleithandlung beim Gassigehen.', difficulty: 'easy', level: 'B2' },

  // === WENN (12) ===
  { id: 'b2_01_wenn_q001', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'wenn', questionText: '___ es regnet, bleibe ich zu Hause.', options: ['Als', 'Während', 'Wenn', 'Bevor'], correctAnswer: 'Wenn', explanation: '"Wenn" wird für wiederholte oder zukünftige Situationen verwendet.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_wenn_q002', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'wenn', questionText: '___ du Zeit hast, besuch mich bitte.', options: ['Als', 'Während', 'Wenn', 'Bevor'], correctAnswer: 'Wenn', explanation: '"Wenn" drückt eine Einladung bei einer Bedingung aus.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_wenn_q003', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'wenn', questionText: 'Immer, ___ ich Stress habe, gehe ich spazieren.', options: ['Als', 'Während', 'Wenn', 'Bevor'], correctAnswer: 'Wenn', explanation: '"Wenn" mit "Immer" zeigt eine wiederholte Reaktion auf eine Situation.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_wenn_q004', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'wenn', questionText: '___ man in Deutschland arbeitet, muss man Steuern zahlen.', options: ['Als', 'Während', 'Wenn', 'Bevor'], correctAnswer: 'Wenn', explanation: '"Wenn" drückt eine allgemeine Wahrheit oder Regel aus.', difficulty: 'medium', level: 'B2' },
  { id: 'b2_01_wenn_q005', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'wenn', questionText: 'Jedes Mal, ___ ich nach Deutschland reise, besuche ich meine Freunde.', options: ['Als', 'Wenn', 'Während', 'Bevor'], correctAnswer: 'Wenn', explanation: '"Wenn" mit "Jedes Mal" zeigt eine regelmäßige Gewohnheit bei Reisen.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_wenn_q006', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'wenn', questionText: '___ du mich brauchst, bin ich für dich da.', options: ['Als', 'Wenn', 'Während', 'Bevor'], correctAnswer: 'Wenn', explanation: '"Wenn" drückt ein Versprechen bei einer Bedingung aus.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_wenn_q007', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'wenn', questionText: '___ du Fleisch kochst, achte auf die Temperatur.', options: ['Als', 'Wenn', 'Während', 'Bevor'], correctAnswer: 'Wenn', explanation: '"Wenn" gibt eine Anweisung bei einer bestimmten Tätigkeit.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_wenn_q008', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'wenn', questionText: '___ die Schule aus ist, gehen die Kinder nach Hause.', options: ['Als', 'Wenn', 'Während', 'Bevor'], correctAnswer: 'Wenn', explanation: '"Wenn" zeigt eine regelmäßige Situation nach einem Ereignis.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_wenn_q009', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'wenn', questionText: 'Immer ___ ich diesen Song höre, denke ich an dich.', options: ['Als', 'Wenn', 'Während', 'Bevor'], correctAnswer: 'Wenn', explanation: '"Wenn" zeigt eine emotionale Reaktion, die sich wiederholt.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_wenn_q010', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'wenn', questionText: '___ der Frühling kommt, werden die Tage länger.', options: ['Als', 'Wenn', 'Während', 'Bevor'], correctAnswer: 'Wenn', explanation: '"Wenn" zeigt eine jährlich wiederkehrende Veränderung.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_wenn_q011', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'wenn', questionText: '___ man krank ist, sollte man zum Arzt gehen.', options: ['Als', 'Wenn', 'Während', 'Bevor'], correctAnswer: 'Wenn', explanation: '"Wenn" drückt eine allgemeine Empfehlung bei einer Bedingung aus.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_wenn_q012', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'wenn', questionText: '___ du morgen frei hast, können wir etwas unternehmen.', options: ['Als', 'Wenn', 'Während', 'Bevor'], correctAnswer: 'Wenn', explanation: '"Wenn" drückt eine Möglichkeit bei einer zukünftigen Bedingung aus.', difficulty: 'easy', level: 'B2' },

  // === SOBALD (12) ===
  { id: 'b2_01_sobald_q001', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'sobald', questionText: '___ ich ankomme, rufe ich dich an.', options: ['Während', 'Bevor', 'Sobald', 'Als'], correctAnswer: 'Sobald', explanation: '"Sobald" bedeutet "as soon as" — unmittelbare Abfolge zweier Handlungen.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_sobald_q002', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'sobald', questionText: '___ er die Wahrheit erfahren hatte, wurde er wütend.', options: ['Während', 'Bevor', 'Sobald', 'Wenn'], correctAnswer: 'Sobald', explanation: '"Sobald" zeigt die unmittelbare emotionale Reaktion auf eine Information.', difficulty: 'medium', level: 'B2' },
  { id: 'b2_01_sobald_q003', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'sobald', questionText: '___ die Prüfung vorbei ist, machen wir eine Party.', options: ['Während', 'Bevor', 'Sobald', 'Als'], correctAnswer: 'Sobald', explanation: '"Sobald" zeigt die Feier, die unmittelbar nach der Prüfung beginnt.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_sobald_q004', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'sobald', questionText: '___ du fertig bist, können wir essen gehen.', options: ['Während', 'Bevor', 'Sobald', 'Wenn'], correctAnswer: 'Sobald', explanation: '"Sobald" zeigt die Einladung, die vom Fertigwerden abhängt.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_sobald_q005', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'sobald', questionText: '___ die Ampel grün wird, fahren wir weiter.', options: ['Während', 'Bevor', 'Sobald', 'Als'], correctAnswer: 'Sobald', explanation: '"Sobald" zeigt die unmittelbare Reaktion auf ein Signal.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_sobald_q006', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'sobald', questionText: '___ er die Nachricht gelesen hat, antwortete er sofort.', options: ['Während', 'Bevor', 'Sobald', 'Wenn'], correctAnswer: 'Sobald', explanation: '"Sobald" zeigt die schnelle Reaktion auf eine Nachricht.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_sobald_q007', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'sobald', questionText: '___ es aufhört zu regnen, gehen wir nach draußen.', options: ['Während', 'Bevor', 'Sobald', 'Als'], correctAnswer: 'Sobald', explanation: '"Sobald" zeigt die Handlung, die nach dem Ende einer anderen beginnt.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_sobald_q008', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'sobald', questionText: '___ ich bezahlt werde, kaufe ich mir ein neues Handy.', options: ['Während', 'Bevor', 'Sobald', 'Wenn'], correctAnswer: 'Sobald', explanation: '"Sobald" zeigt die unmittelbare Handlung nach dem Erhalt des Geldes.', difficulty: 'medium', level: 'B2' },
  { id: 'b2_01_sobald_q009', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'sobald', questionText: '___ das Licht anging, konnte ich alles sehen.', options: ['Während', 'Bevor', 'Sobald', 'Als'], correctAnswer: 'Sobald', explanation: '"Sobald" zeigt die unmittelbare Folge einer Handlung.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_sobald_q010', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'sobald', questionText: '___ du das liest, wirst du verstehen.', options: ['Während', 'Bevor', 'Sobald', 'Wenn'], correctAnswer: 'Sobald', explanation: '"Sobald" zeigt die unmittelbare Erkenntnis nach dem Lesen.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_sobald_q011', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'sobald', questionText: '___ wir in München ankommen, suchen wir ein Hotel.', options: ['Während', 'Bevor', 'Sobald', 'Als'], correctAnswer: 'Sobald', explanation: '"Sobald" zeigt die erste Handlung nach der Ankunft.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_sobald_q012', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'sobald', questionText: '___ der Film zu Ende ist, gehen wir essen.', options: ['Während', 'Bevor', 'Sobald', 'Wenn'], correctAnswer: 'Sobald', explanation: '"Sobald" zeigt die Planung unmittelbar nach dem Film.', difficulty: 'easy', level: 'B2' },

  // === SOLANGE (12) ===
  { id: 'b2_01_solange_q001', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'solange', questionText: '___ du lernst, darfst du hier bleiben.', options: ['Während', 'Solange', 'Bevor', 'Sobald'], correctAnswer: 'Solange', explanation: '"Solange" bedeutet "as long as" — die Erlaubnis gilt während der Lernzeit.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_solange_q002', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'solange', questionText: '___ du hier bleibst, werde ich glücklich sein.', options: ['Während', 'Solange', 'Bevor', 'Als'], correctAnswer: 'Solange', explanation: '"Solange" zeigt die Bedingung für das Glück während einer Zeitperiode.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_solange_q003', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'solange', questionText: 'Er hat ihr zugehört, ___ sie gesprochen hat.', options: ['Während', 'Solange', 'Bevor', 'Sobald'], correctAnswer: 'Solange', explanation: '"Solange" zeigt die Dauer der Aufmerksamkeit während des Sprechens.', difficulty: 'medium', level: 'B2' },
  { id: 'b2_01_solange_q004', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'solange', questionText: '___ du die Wahrheit sagst, habe ich keine Fragen.', options: ['Während', 'Solange', 'Bevor', 'Wenn'], correctAnswer: 'Solange', explanation: '"Solange" zeigt die Bedingung während einer Zeitperiode der Ehrlichkeit.', difficulty: 'medium', level: 'B2' },
  { id: 'b2_01_solange_q005', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'solange', questionText: 'Das Auto kann hier stehen, ___ wir einkaufen.', options: ['Während', 'Solange', 'Bevor', 'Sobald'], correctAnswer: 'Solange', explanation: '"Solange" zeigt die erlaubte Zeitdauer des Parkens.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_solange_q006', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'solange', questionText: 'Ich werde dich unterstützen, ___ du es brauchst.', options: ['Während', 'Solange', 'Bevor', 'Wenn'], correctAnswer: 'Solange', explanation: '"Solange" zeigt die Dauer des Unterstützungsangebots.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_solange_q007', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'solange', questionText: '___ du Geduld hast, wird alles gut.', options: ['Während', 'Solange', 'Bevor', 'Nachdem'], correctAnswer: 'Solange', explanation: '"Solange" zeigt die Bedingung während einer Zeitperiode der Geduld.', difficulty: 'medium', level: 'B2' },
  { id: 'b2_01_solange_q008', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'solange', questionText: 'Er ist zu Hause geblieben, ___ seine Frau krank war.', options: ['Während', 'Solange', 'Bevor', 'Sobald'], correctAnswer: 'Solange', explanation: '"Solange" zeigt die Dauer des Zuhausebleibens während der Krankheit.', difficulty: 'medium', level: 'B2' },
  { id: 'b2_01_solange_q009', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'solange', questionText: '___ ich kann, helfe ich dir bei deinem Projekt.', options: ['Während', 'Solange', 'Bevor', 'Wenn'], correctAnswer: 'Solange', explanation: '"Solange" zeigt die zeitlich begrenzte Hilfe während meiner Fähigkeit.', difficulty: 'medium', level: 'B2' },
  { id: 'b2_01_solange_q010', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'solange', questionText: 'Du darfst mein Buch behalten, ___ du es brauchst.', options: ['Während', 'Solange', 'Bevor', 'Sobald'], correctAnswer: 'Solange', explanation: '"Solange" zeigt die Zeitperiode der Erlaubnis.', difficulty: 'easy', level: 'B2' },
  { id: 'b2_01_solange_q011', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'solange', questionText: '___ wir hier wohnen, gehen wir jeden Sonntag in die Kirche.', options: ['Während', 'Solange', 'Bevor', 'Als'], correctAnswer: 'Solange', explanation: '"Solange" zeigt die Routine während eines Wohnaufenthalts.', difficulty: 'medium', level: 'B2' },
  { id: 'b2_01_solange_q012', module: 'B2', topicNumber: '1. Topic', topicName: 'Konnektoren', konnektor: 'solange', questionText: '___ es dunkel ist, sollte man das Licht anmachen.', options: ['Während', 'Solange', 'Bevor', 'Sobald'], correctAnswer: 'Solange', explanation: '"Solange" zeigt die Handlung während einer Zeitperiode der Dunkelheit.', difficulty: 'easy', level: 'B2' },
];

// Helper: POST to Firestore REST API
function firestorePost(collection, docId, fields) {
  return new Promise((resolve, reject) => {
    const body = JSON.stringify({ fields });
    const options = {
      hostname: 'firestore.googleapis.com',
      path: `/v1/projects/${PROJECT_ID}/databases/(default)/documents/${collection}?documentId=${docId}&key=${API_KEY}`,
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Content-Length': Buffer.byteLength(body) }
    };
    const req = https.request(options, res => {
      let d = '';
      res.on('data', c => d += c);
      res.on('end', () => resolve({ status: res.statusCode, body: d }));
    });
    req.on('error', reject);
    req.write(body);
    req.end();
  });
}

// Convert to Firestore field format
function toFields(obj) {
  const fields = {};
  for (const [k, v] of Object.entries(obj)) {
    if (typeof v === 'string') fields[k] = { stringValue: v };
    else if (typeof v === 'number') fields[k] = { integerValue: v };
    else if (typeof v === 'boolean') fields[k] = { booleanValue: v };
    else fields[k] = { stringValue: String(v) };
  }
  return fields;
}

async function main() {
  console.log('🚀 Importing B2 Topic 1 (Konnektoren) — 96 questions to moduleQuizQuestions\n');

  // Import topic metadata first
  console.log('📚 Step 1: Creating topic document...');
  await firestorePost('topics', 'b2_01', toFields({
    id: 'b2_01',
    module: 'B2',
    topicNumber: '1. Topic',
    topicName: 'Konnektoren',
    subTopics: 'als, bevor, bis, seitdem, während, wenn, sobbing, solange',
    questionCount: 96,
    type: 'module'
  }));
  console.log('  ✅ Topic b2_01 created\n');

  // Import 96 questions
  console.log('📝 Step 2: Importing 96 questions...\n');
  const konnektors = ['als', 'bevor', 'bis', 'seitdem', 'während', 'wenn', 'sobald', 'solange'];
  
  for (const k of konnektors) {
    const kQuestions = questions.filter(q => q.konnektor === k);
    console.log(`  [${k}] ${kQuestions.length} questions...`);
    
    for (const q of kQuestions) {
      await firestorePost('moduleQuizQuestions', q.id, toFields(q));
      process.stdout.write('  ✓');
    }
    console.log(` ✅`);
  }

  console.log('\n🎉 Done! 96 questions imported to moduleQuizQuestions');
  console.log('\n📊 View in Firebase Console:');
  console.log('  https://console.firebase.google.com/project/b2-deutsch-app/firestore');
  console.log('  → moduleQuizQuestions collection');
  console.log('  → topics/b2_01 document');
}

main().catch(console.error);

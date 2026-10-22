Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Apollonius (ambassador): Apollonius (Ancient Greek: Απολλώνιος ) was the spokesman of an embassy sent by the Seleucid ruler Antiochus IV Epiphanes to Rome in 173 BCE.  He brought from Antiochus tribute and rich presents, and requested that the Roman Senate would renew with Antiochus the alliance which had existed between his father, Antiochus III the Great, and the Romans.

Daniel (biblical figure): Daniel (, Hebrew "God is my Judge") is the hero of the Book of Daniel.  A noble Jewish youth of Jerusalem, he is taken into captivity by Nebuchadnezzar of Babylon and serves the king and his successors with loyalty and ability until the time of the Persian conqueror Cyrus, all the while remaining true to the God of Israel.  Some conservative scholars continue to argue that Daniel was a genuine individual and that the book that bears his name reflects real history, but the broad consensus is that Daniel never existed and that the book is a cryptic allusion to the reign of the 2nd century BCE Greek king Antiochus IV Epiphanes.

Land of Onias: The Land of Onias (Greek: Ὀνίας ) is the name given in Hellenistic Egyptian, Jewish, and Roman sources to an area in Ancient Egypt's Nile delta where a large number of Jews settled.  The Land of Onias, which included the city of Leontopolis (Λεόντων πόλις), was located in the nome of Heliopolis.  While accounts differ on the details, it is known that the Jews of Leontopolis had a functioning Temple, presided over by kohanim of the family of Onias IV (for whom the "Land of Onias" is named).  Like its predecessor the Jewish Temple at Elephantine (destroyed in the 4th century BCE), the Temple at Leontopolis was the only Jewish sanctuary outside of Jerusalem where sacrifices were offered.  Aside from a somewhat uncertain allusion of the Hellenist Artapanus, only Josephus gives information about this temple.  The Talmudic accounts are internally contradictory.  The establishment of a central sanctuary in Egypt was probably undertaken in response, in part, to the disorders that arose in Judea under Antiochus IV Epiphanes, the desecration of the Temple at Jerusalem under his reign, the supplanting of the legitimate family of priests by the installation of Alcimus, the personal ambition of Onias IV, and the vast extent of the Jewish diaspora in Egypt that created demand for a sanctuary of this nature.

Ptolemy Macron: Ptolemy Macron (fl.  2nd century BCE) was a Seleucid general of King Antiochus IV Epiphanes (c. 215 BCE – 164 BCE) of Syria.  His life is covered in parts of the first two Books of the Maccabees, which call him the son of Dorymenes and give him the cognomen "Macron".

Hyspaosines: Hyspaosines or Aspasine ( in arabic هيسباوسينز or أسباسين) ,(c. 209 BC - 124 BC) was a satrap installed by Antiochus IV Epiphanes and later the first King (before 127-124 BC) of Characene or Mesene (Meshun).  Hyspaosines is mainly known from coins, but also appears in texts of cuneiform script (in the Babylonian astronomical diaries).  Pliny the Elder mentions that he was the son of a certain "Sagdodonacos the king of Arabs".

Heliodorus (minister): Heliodorus (Greek: Ἡλιόδωρος ) was a legate of Seleucus IV Philopator c. 187 BC – 175 BC.  Some historical sources say that he assassinated Seleucus seized the throne for himself, before Antiochus IV Epiphanes, the brother of the late king, with the help of the Pergamon monarch, Eumenes II, recovered it.

Antiochus IV of Commagene: Gaius Julius Antiochus IV Epiphanes (Ancient Greek: Γάιος Ἰούλιος Ἀντίοχος ὀ Ἐπιφανής , before 17 AD – after 72 AD), the last king of Commagene, reigned between 38–72 as a client king to the Roman Empire.  The epithet "Epiphanes" means "the Glorious".

Seleucid Dynastic Wars: The Seleucid Dynastic Wars were a series of wars of succession that were fought between competing branches of the Seleucid Royal household for control of the Seleucid Empire.  Beginning as a by-product of several succession crises that arose from the reigns of Seleucus IV Philopator and his brother Antiochus IV Epiphanes in the 170s and 160s, the wars typified the final years of the empire and were an important cause of its decline as a major power in the Near East and Hellenistic world.  The last war ended with the collapse of the kingdom and its annexation by the Romans in 63 BC.

Antiochus IV Epiphanes: Antiochus IV Epiphanes ( ; Ancient Greek: Ἀντίοχος Δ΄ ὁ Ἐπιφανής , "Antíochos D' ho Epiphanḗs", "God Manifest"; c. 215 BC – 164 BC) was a Hellenistic Greek king of the Seleucid Empire from 175 BC until his death in 164 BC.  He was a son of King Antiochus III the Great.  His original name was Mithradates (alternative form "Mithridates"); he assumed the name Antiochus after he ascended the throne.

Babylonian astronomical diaries: The Babylonian astronomical diaries are a collection of Babylonian cuneiform texts which contain systematic records of astronomical observations and political events, as well as predictions based on astronomical observations.  They also include other information, such as commodity prices for particular dates and weather reports.

Question: Hyspaosines was a satrap installed by Antiochus IV Epiphanes, and later the first King of Characene or Mesene (Meshun), he's mainly known from coins, but also appears in texts of cuneiform script, which contain systematic records of astronomical observations and political events, as well as predictions is titled?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_of_interest": {
      "type": "string",
      "description": "The name of the historical figure mentioned."
    },
    "text_format": {
      "type": "string",
      "description": "The type of script or format of the text."
    },
    "text_content_summary": {
      "type": "string",
      "description": "A summary of the content found in the text."
    },
    "text_title": {
      "type": "string",
      "description": "The specific title of the collection of texts."
    }
  },
  "required": [
    "person_of_interest",
    "text_format",
    "text_content_summary",
    "text_title"
  ],
  "additionalProperties": false
}

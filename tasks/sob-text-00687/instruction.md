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
Late Period of ancient Egypt: The Late Period of ancient Egypt refers to the last flowering of native Egyptian rulers after the Third Intermediate Period from the 26th Saite Dynasty into Achaemenid Persian conquests and ended with the conquest by Alexander the Great and establishment of the Ptolemaic Kingdom.  It ran from 664 BC until 332 BC.  With the Macedonian Greek conquest in the latter half of the 4th century BC, the age of Hellenistic Egypt began.

Hellenistic astrology: Hellenistic astrology is a tradition of horoscopic astrology that was developed and practiced in the late Hellenistic period in and around the Mediterranean region, especially in Egypt.  The texts and technical terminology of this tradition of astrology were largely written in Greek (or sometimes Latin).  The tradition originated sometime around the late 2nd or early 1st century BCE, and then was practiced until the 6th or 7th century CE.  This type of astrology is commonly referred to as "Hellenistic astrology" because it was developed in the late Hellenistic period, although it continued to be practiced for several centuries after the end of what historians usually classify as the Hellenistic era.

Egypt–Italy relations: Egypt–Italy relations refer to relations between Egypt and Italy.  Relations were first established during the period of the Roman Republic, when the Ptolemaic Kingdom frequently interacted with Rome, culminating in the Roman annexation of Egypt in 30 BC.  With the dissolution of the Western Roman Empire in 476 AD and Egypt's continuation as a province of the Eastern Roman Empire until the Islamic conquest in 642 AD, there were no independent states of Italy and Egypt, and as such no diplomatic relations.  Cultural ties between Egypt and Italy distanced further over time with the Islamisation of Egypt and the strength of Catholicism in Italy.  It would not be until Egypt's official independence from the Ottomans in 1914 that relations with Italy would be reestablished.  With the rise of Mussolini and fascism in Italy and the eventual Italian invasion of Egypt during World War II, relations became severely strained.  However, after the war, relations were re-established and the countries now have a cordial relationship.  Egypt has an embassy in both Rome and Milan, while Italy has an embassy in both Cairo and Alexandria.  Egypt and Italy are both members of the Union for the Mediterranean.

Ptolemaic dynasty: The Ptolemaic dynasty (Ancient Greek: Πτολεμαῖοι , "Ptolemaioi"), sometimes also known as the Lagids or Lagidae (Ancient Greek: Λαγίδαι , "Lagidai", after Lagus, Ptolemy I's father), was a Macedonian Greek royal family, which ruled the Ptolemaic Kingdom in Egypt during the Hellenistic period.  Their rule lasted for 275 years, from 305 to 30 BC.  They were the last dynasty of ancient Egypt.

Hellenistic armies: The Hellenistic armies is the term applied to the armies of the successor kingdoms of the Hellenistic period, which emerged after the death of Alexander the Great.  After his death, Alexander's huge empire was torn between his successors, the Diadochi (Greek: Διάδοχοι ).  During the Wars of the Diadochi, the Macedonian army, as developed by Alexander and Philip II, gradually adopted new units and tactics, further developing Macedonian warfare and improving on the tactics used in the Classical era.  The armies of the Diadochi bear few differences from that of Alexander, but during the era of the Epigonoi (Ἐπίγονοι, "Successors"), the differences were obvious, favoring numbers over quality and weight over maneuverability.  The limited availability of Greek conscripts in the east led to an increasing dependence on mercenary forces, whereas in the west, Hellenistic armies were continuously involved in wars, which soon exhausted local manpower, paving the way for Roman supremacy.  The major Hellenistic states were the Seleucid Empire, Ptolemaic Egypt and the Antigonid kingdom (Macedonia).  Smaller states included: Attalid Pergamum, Pontus, Epirus, the Achaean League, the Aetolian League, Syracuse, and other states (like Athens, Sparta etc.).

Oenanthe of Egypt: Oenanthe (Greek: Οἰνἀνθη , her name means "wineflower" - from οἶνος "wine" and ἄνθος "flower" - flourished 3rd century BC, died 203 BC) was an Egyptian Greek noblewoman and through marriage was a relation of the Ptolemaic dynasty.

Alexander Helios: Alexander Helios (Greek: Ἀλέξανδρος Ἥλιος ; late 40 BC – unknown, but possibly between 29 and 25 BC) was a Ptolemaic prince and was the eldest son of the Macedonian queen Cleopatra VII of Ptolemaic Egypt by Roman triumvir Mark Antony.  Alexander's fraternal twin sister was Cleopatra Selene II.  The twins were of Macedonian Greek and Roman heritage, Cleopatra named her son after her collateral ancestor, Alexander the Great.  His second name in Ancient Greek means "Sun"; this was the counterpart of his twin sister’s second name "Selene" (Σελήνη), meaning "Moon".

Ptolemaic Kingdom: The Ptolemaic Kingdom ( ; Ancient Greek: Πτολεμαϊκὴ βασιλεία , "Ptolemaïkḕ basileía") was a Hellenistic kingdom based in Egypt.  It was ruled by the Ptolemaic dynasty which started with Ptolemy I Soter's accession after the death of Alexander the Great in 323 BC and which ended with the death of Cleopatra VII and the Roman conquest in 30 BC.

Ptolemy I Soter: Ptolemy I Soter I (, "Ptolemaĩos Sōtḗr" ≈ Ptolemy (pronounced ) the Savior; c. 367 BC – 283/2 BC), also known as Ptolemy of Lagus (Πτολεμαῖος ὁ Λάγου/Λαγίδης ), was a Macedonian Greek general under Alexander the Great, one of the three Diadochi who succeeded to his empire.  Ptolemy became ruler of Egypt (323–283/2 BC) and founded a dynasty which ruled it for the next three centuries, turning Egypt into a Hellenistic kingdom and Alexandria into a center of Greek culture.  He assimilated some aspects of Egyptian culture, however, assuming the traditional title pharaoh in 305/4 BC.  The use of the title of pharaoh was often situational: pharaoh was used for an Egyptian audience, and Basileus for a Greek audience, as exemplified by Egyptian coinage.

Ptolemaic army: The Ptolemaic army was the army of the Ptolemaic Macedonian kings that ruled Egypt from 305 to 30 BC.  Like most of the other armies of the Diadochi, it was very much Macedonian in style, with the use of the long pike ("sarissa") in a deep phalanx formation.  Despite the strength of the Ptolemaic army, evinced in 217 BC with the victory over the Seleucids at the Battle of Raphia, the Ptolemaic kingdom itself fell into decline and by the time of Julius Caesar, it was but a mere client-kingdom of the Roman Republic.  The army by the time of Caesar’s campaigns in the eastern Mediterranean was a mere shadow of its former self: generally, a highly disorganized assemblage of mercenaries and other foreign troops.

Question: Which of  the Oenanthe of Egypt relations was a Macedonian Greek royal family, which ruled the Ptolemaic Kingdom in Egypt during the Hellenistic period?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "entity_name": {
      "type": "string",
      "description": "The name of the royal family."
    },
    "entity_description": {
      "type": "object",
      "properties": {
        "type": {
          "type": "string",
          "description": "The type of entity, e.g., 'royal family'."
        },
        "origin": {
          "type": "string",
          "description": "The ethnic origin of the royal family."
        },
        "ruled_kingdom": {
          "type": "string",
          "description": "The kingdom ruled by the family."
        },
        "historical_period": {
          "type": "string",
          "description": "The historical period during which the family ruled."
        }
      },
      "required": [
        "type",
        "origin",
        "ruled_kingdom",
        "historical_period"
      ],
      "additionalProperties": false
    },
    "rule_details": {
      "type": "object",
      "properties": {
        "duration_years": {
          "type": "integer",
          "description": "The total duration of their rule in years."
        },
        "start_year_bc": {
          "type": "integer",
          "description": "The start year of their rule (BC)."
        },
        "end_year_bc": {
          "type": "integer",
          "description": "The end year of their rule (BC)."
        }
      },
      "required": [
        "duration_years",
        "start_year_bc",
        "end_year_bc"
      ],
      "additionalProperties": false
    },
    "relation_to_oenanthe": {
      "type": "string",
      "description": "How the entity was related to Oenanthe of Egypt."
    }
  },
  "required": [
    "entity_name",
    "entity_description",
    "rule_details",
    "relation_to_oenanthe"
  ],
  "additionalProperties": false
}

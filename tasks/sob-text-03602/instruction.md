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
Artemis Tauropolos: Artemis Tauropolos, in ancient Greece, was an epithet for the goddess Artemis, variously interpreted as "worshipped at Tauris", "pulled by a yoke of bulls", or "hunting bull goddess".  A statue of Artemis "Tauropolos" in her temple at Brauron in Attica was supposed to have been brought from the Taurians by Iphigenia.  Tauropolia was also a festival of Artemis in Athens.

Laphria (festival): Laphria (Ancient Greek: τὰ Λάφρια) was an ancient Greek religious festival in honour of the goddess Artemis, held every year in Patras.  There was a sanctuary of Artemis Laphria on the acropolis of Patras.  The sanctuary had an image of Artemis Laphria, that was brought there from Calydon in Aetolia after it was laid waste by Augustus.  Every year, the people held a "festival of the Laphria" in the goddess's honour "which was peculiar to their place".  They made a barrier of tall logs round the altar, "still green", so that the stockade would not burn.  They piled the driest wood on the altar, for kindling, and then smoothed the approaches to the pyre by laying earth on the altar steps.  On the first day, the people walked in procession of the "greatest grandeur" for the goddess.  A virgin priestess brought up the rear, riding in a chariot which was drawn by tame yoke deer.  The next day, living animals are sacrificed, including edible birds, boars, deer, gazelles, wolves and bears, but also fruit from trees.  The altar was set on fire.  Animals forced out by the first leap of the flames, or escaping at full tilt were thrown back into the fire, to their death, by those who had brought them.  There was no record of anyone being injured by the animals.

USS Artemis (AKA-21): USS "Artemis" (AKA-21) was an "Artemis"-class attack cargo ship named after the asteroid 105 Artemis, which in turn was named after the Greek goddess Artemis.  She served as a commissioned ship for 2 years and 4 months.

Caryatid: A caryatid ( ; Greek: Καρυάτις , plural: Καρυάτιδες) is a sculpted female figure serving as an architectural support taking the place of a column or a pillar supporting an entablature on her head.  The Greek term "karyatides" literally means "maidens of Karyai", an ancient town of Peloponnese.  Karyai had a famous temple dedicated to the goddess Artemis in her aspect of Artemis Karyatis: "As Karyatis she rejoiced in the dances of the nut-tree village of Karyai, those Karyatides, who in their ecstatic round-dance carried on their heads baskets of live reeds, as if they were dancing plants".

Temple of Artemis: The Temple of Artemis or Artemision (, Turkish: "Artemis Tapınağı" ), also known less precisely as the Temple of Diana, was a Greek temple dedicated to the goddess Artemis.  It was located in Ephesus (near the modern town of Selçuk in present-day Turkey).  One of the Seven Wonders of the Ancient World, it was completely rebuilt three times before its final destruction in 401 AD.  Only foundations and sculptural fragments of the latest of the temples at the site remain.

Seven Wonders of the Ancient World: The Seven Wonders of the World or the Seven Wonders of the Ancient World is a list of remarkable constructions of classical antiquity given by various authors in guidebooks or poems popular among ancient Hellenic tourists.  Although the list, in its current form, did not stabilise until the Renaissance, the first such lists of seven wonders date from the 1st-2nd century BC.  The original list inspired innumerable versions through the ages, often listing seven entries.  Of the original Seven Wonders, only one—the Great Pyramid of Giza, the oldest of the ancient wonders—remains relatively intact.  The Colossus of Rhodes, the Lighthouse of Alexandria, the Mausoleum at Halicarnassus, the Temple of Artemis and the Statue of Zeus were all destroyed.  The location and ultimate fate of the Hanging Gardens are unknown, and there is speculation that they may not have existed at all.

Temple of Artemis, Corfu: The Temple of Artemis is an Archaic Greek temple in Corfu, Greece, built in around 580 BC in the ancient city of Korkyra (or Corcyra), in what is known today as the suburb of Garitsa.  The temple was dedicated to Artemis.  It is known as the first Doric temple exclusively built with stone.  It is also considered the first building to have incorporated all of the elements of the Doric architectural style.  Very few Greek temple reliefs from the Archaic period have survived, and the large fragments of the group from the pediment are the earliest significant survivals.

Caryatis: In ancient Greek religion Artemis Caryatis was an epithet of Artemis that was derived from the small "polis" of Karyai in Laconia; there an archaic open-air "temenos" was dedicated to Carya, the "Lady of the Nut-Tree", whose priestesses were called the "caryatidai", represented on the Athenian Acropolis as the marble caryatids supporting the porch of the Erechtheum.  The late accounts made of the eponymous Carya a virgin who had been transformed into a nut-tree, whether for her unchastity (with Dionysus) or to prevent her rape.  The particular form of veneration of Artemis at Karyai suggests that in pre-classical ritual Carya was goddess of the nut tree who was later assimilated into the Olympian goddess Artemis.  Pausanias noted that each year women performed a dance called the "caryatis" at a festival in honor of Artemis Caryatis called the "Caryateia".

Apanchomene: Apanchomene (Ancient Greek: Ἀπαγχομένη ) was in Greek mythology an epithet for the goddess Artemis that meant "the strangled goddess" or "she who hangs herself".  The origin of this name is thus related by Pausanias: in the neighborhood of the town of Caphyae in Arcadia, in a place called Condylea, there was a sacred grove of Artemis Condyleatis.  On one occasion when some boys were playing in this grove, they put a string around the goddess's statue, and said in their jokes they would strangle Artemis.  Some of the inhabitants of Caphyae who found the boys engaged in their sport, stoned them to death.

List of Classical Age states: The classical age (also the classical antiquity, classical period or classical era) is a broad term for a long period of cultural history generally centered on the Mediterranean Sea and Near East, comprising the interlocking ancient civilizations, c. 600 BC to 200 AD.  It is the period in which societies flourished and wielded great influence throughout East Asia, Europe, North Africa, South Asia and the Middle East.  It is conventionally taken to begin with the earliest-recorded Greek poetry of Homer (8th–7th century BC), and continues through the emergence of Christianity and the decline of the Roman Empire (5th century AD).  It ends with the dissolution of classical culture at the close of Late Antiquity and (AD 300–600), blending into the Dark Ages or Middle Age (AD 600–1000).  Such a wide sampling of history and territory covers many disparate cultures and periods.  "Classical antiquity" may refer also to an idealised vision among later people of what was, in Edgar Allan Poe's words, "the glory that was Greece, the grandeur that was Rome!"  The culture of the ancient Greeks, together with some influences from the ancient Orient, prevailed throughout classical antiquity as the basis of art,the Bronze Age generally followed the Neolithic period.  but in some parts of the world, the Copper Age served as a transition from the Neolithic to the Bronze Age.

Question: Among what group of people made guidebooks or poems popular of a list of remarkable constructions of classical antiquity, including a Greek temple dedicated to the goddess Artemis that was completely rebuilt three times before its final destruction in 401 AD ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "group_of_people": {
      "type": "string",
      "description": "The group of people among whom guidebooks or poems about classical antiquity were popular."
    },
    "list_of_constructions_name": {
      "type": "string",
      "description": "The name of the list of remarkable constructions."
    },
    "temple_details": {
      "type": "object",
      "properties": {
        "temple_name": {
          "type": "string",
          "description": "The name of the Greek temple dedicated to Artemis."
        },
        "goddess_dedicated_to": {
          "type": "string",
          "description": "The goddess to whom the temple was dedicated."
        },
        "rebuild_count": {
          "type": "integer",
          "description": "The number of times the temple was completely rebuilt."
        },
        "final_destruction_year": {
          "type": "integer",
          "description": "The year of the temple's final destruction."
        },
        "is_one_of_seven_wonders": {
          "type": "boolean",
          "description": "Indicates if the temple was one of the Seven Wonders of the Ancient World."
        }
      },
      "required": [
        "temple_name",
        "goddess_dedicated_to",
        "rebuild_count",
        "final_destruction_year",
        "is_one_of_seven_wonders"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "group_of_people",
    "list_of_constructions_name",
    "temple_details"
  ],
  "additionalProperties": false
}

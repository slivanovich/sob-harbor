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
George and Martha: George and Martha is a series of children's books written and illustrated by James Marshall between 1972 and 1988.  Each book in the series contained a number of short stories describing interactions between two hippos, George and Martha.  The books inspired an animated children's television show which comprised 26 episodes made in 1999, and a musical in 2011.

Ancient Greek accent: Ancient Greek had a pitch accent.  One of the final three syllables of an Ancient Greek word carried an accent.  Each syllable contains a vowel with one or two vocalic morae, and one mora in a word was accented; the accented mora was pronounced at a higher pitch than other morae.  Two-mora syllables could have rising or falling pitch patterns or normal pitch; one-mora syllables could have high or normal pitch.  Rules restricted where an accented mora could appear, but within those restrictions, accent was free: it could appear in different positions in a given word.  Usually a word's accent was either recessive, or as close to the beginning of the word as restrictions would allow, or it was placed on the last syllable, the ultima; but in some cases the second syllable from the end was accented even when accent rules allowed the third syllable from the end to be accented.

Themisto: In Greek mythology, Themisto (Ancient Greek: Θεμιστώ ), daughter of Hypseus, was the third and last wife of Athamas.  According to some sources, she had four children by him: Leucon, Erythrius, Schoeneus, and Ptous.  In other sources there were but two: Sphincius and Orchomenus, or else Schoeneus and Leucon.  Some say that the father of Leucon was Poseidon (see also Leuconoe).  Her name is derived from the Ancient Greek word: "θεμιστος" which means "belonging to the law", or "belonging to the customs".

Dendrimer: Dendrimers are repetitively branched molecules.  The name comes from the Greek word δέντρο (dendro).  which translates to "tree". The Greek word δενδριμερές is translated as a part of the tree.  It is named like that, because it is like to see a tree from the top.  Synonymous terms for dendrimer include arborols and cascade molecules.  However, dendrimer is currently the internationally accepted term.  A dendrimer is typically symmetric around the core, and often adopts a spherical three-dimensional morphology.  The word dendron is also encountered frequently.  A dendron usually contains a single chemically addressable group called the focal point or core.  The difference between dendrons and dendrimers is illustrated in the top figure, but the terms are typically encountered interchangeably.

Gorgon: In Greek mythology, a Gorgon ( ; plural: Gorgons, Ancient Greek: Γοργών/Γοργώ "Gorgon"/"Gorgo") is a female creature.  The name derives from the ancient Greek word gorgós, which means "dreadful", and appears to come from the same root as the Sanskrit word "garğ" which is defined as a guttural sound, similar to the growling of a beast, thus possibly originating as an onomatopoeia.  While descriptions of Gorgons vary across Greek literature and occur in the earliest examples of Greek literature, the term commonly refers to any of three sisters who had hair made of living, venomous snakes, as well as a horrifying visage that turned those who beheld her to stone.  Traditionally, while two of the Gorgons were immortal, Stheno and Euryale, their sister Medusa was not, and she was slain by the demigod and hero Perseus.

Hippopotamus: The common hippopotamus ("Hippopotamus amphibius"), or hippo, is a large, mostly herbivorous and aggressive mammal in sub-Saharan Africa, and one of only two extant species in the family Hippopotamidae, the other being the pygmy hippopotamus ("Choeropsis liberiensis" or "Hexaprotodon liberiensis").  The name comes from the ancient Greek for "river horse" (ἱπποπόταμος ).  After the elephant and rhinoceros, the common hippopotamus is the third-largest type of land mammal and the heaviest extant artiodactyl.  Despite their physical resemblance to pigs and other terrestrial even-toed ungulates, the closest living relatives of the Hippopotamidae are cetaceans (whales, dolphins, porpoises, etc.) from which they diverged about .  The common ancestor of whales and hippos split from other even-toed ungulates around .  The earliest known hippopotamus fossils, belonging to the genus "Kenyapotamus" in Africa, date to around .

Xylophagy: Xylophagy is a term used in ecology to describe the habits of an herbivorous animal whose diet consists primarily (often solely) of wood.  The word derives from Greek "ξυλοφάγος" ("xulophagos") "eating wood", from "ξύλον" ("xulon") "wood" and "φαγεῖν" ("phagein") "to eat", an ancient Greek name for a kind of a worm-eating bird.  Animals feeding only on dead wood are called sapro-xylophagous or saproxylic.

Romanization of Greek: Romanization of Greek is the transliteration (letter-mapping) or transcription (sound-mapping) of text from the Greek alphabet into the Latin alphabet.  The conventions for writing and romanizing Ancient Greek and Modern Greek differ markedly, which can create confusion.  The sound of the English letter B (/b/ ) was written as β in ancient Greek but is now written as the digraph μπ , while the modern β sounds like the English letter V (/v/ ) instead.  The Greek name Ἰωάννης became Johannes in Latin and then John in English, but in Greek itself has instead become Γιάννης ; this might be written as Yannis, Jani, Ioannis, Yiannis, or Giannis, but not Giannes or Giannēs as it would have been in ancient Greek.  The masculine Greek word Ἅγιος or Άγιος might variously appear as Hagiοs, Agios, Aghios, or Ayios, or simply be translated as "Holy" or "Saint" in English forms of Greek placenames.

Fennec fox: The fennec fox or fennec ("Vulpes zerda") is a small nocturnal fox found in the Sahara of North Africa.  Its most distinctive feature is its unusually large ears, which also serve to dissipate heat.  Its name comes from the Arabic word فنك ("fanak"), which means "fox", and the species name "zerda" comes from the Greek word "xeros" which means dry, referring to the fox's habitat.  The fennec is the smallest species of canid.  Its coat, ears, and kidney functions have adapted to high-temperature, low-water, desert environments.  In addition, its hearing is sensitive enough to hear prey moving underground.  It mainly eats insects, small mammals, and birds.

Kairos: Kairos (καιρός ) is an Ancient Greek word meaning the right, critical or opportune moment.  The ancient Greeks had two words for time: chronos (χρόνος ) and kairos.  While the former refers to chronological or sequential time, the latter signifies a proper or opportune time for action.  What is happening when referring to kairos depends on who is using the word.  While chronos is quantitative, kairos has a qualitative, permanent nature.  "Kairos" also means "weather" in Modern Greek.  The plural, καιροί ("kairoi" (Ancient and Modern Greek)) means "the times".

Question: The George and Martha sereis of childrens books feature an animal whose name comes from an ancient Greek word that means what?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "book_series_name": {
      "type": "string",
      "description": "The name of the children's book series."
    },
    "featured_animal": {
      "type": "string",
      "description": "The type of animal featured in the book series."
    },
    "animal_name_origin": {
      "type": "object",
      "properties": {
        "language": {
          "type": "string",
          "description": "The language from which the animal's name is derived."
        },
        "original_word_transliteration": {
          "type": "string",
          "description": "The transliteration of the original word in the source language."
        },
        "meaning": {
          "type": "string",
          "description": "The meaning of the original word."
        }
      },
      "required": [
        "language",
        "original_word_transliteration",
        "meaning"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "book_series_name",
    "featured_animal",
    "animal_name_origin"
  ],
  "additionalProperties": false
}

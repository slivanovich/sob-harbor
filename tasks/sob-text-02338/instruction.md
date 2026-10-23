{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMary Beckman: Mary E. Beckman is a Professor of Linguistics at the Ohio State University.  She edited the Journal of Phonetics from 1990 to 1994.  Perhaps her most significant contribution to linguistics is the fact that in 1987, together with John Kingston, she organized the first Laboratory Phonology conference at Columbus, Ohio, and served with Kingston as series editor for the Cambridge University Press series \"Papers in Laboratory Phonology\" from 1987 through 2004.  The laboratory phonology movement was one of the two most important developments during the 1990s in the linguistic subdisciplines that study language sound systems, and gave rise to the Association for Laboratory Phonology.  The other important development was Optimality Theory.\n\nOld Norse: Old Norse was a North Germanic language that was spoken by inhabitants of Scandinavia and inhabitants of their overseas settlements during about the 9th to 13th centuries.\n\nSt Mary de Haura Church, Shoreham-by-Sea: St Mary de Haura Church is an Anglican church (formerly a Catholic church) in the ancient \"New Shoreham\" area of Shoreham-by-Sea in the district of Adur, one of seven local government districts in the English county of West Sussex.  It was founded at the end of the 11th century as a large cruciform church which, due to its original scale, has been described as a collegiate church—a reflection of the port of Shoreham's importance at the time.  The former east end of that building survives to form the present church, and much 12th-century work remains.  It functions as Shoreham-by-Sea's \"town church\" for major religious and social events, as well as serving its small town-centre parish.  English Heritage has listed it at Grade I for its architectural and historical importance.\n\nAntidotarium Nicolai: The Antidotarium Nicolai, also known as the \"Antidotarium parvum\" or small antidotarium, was a late 11th or early 12th-century Latin book with about 150 recipes for the creation of medicines from plants and minerals.  It was written in the circles of the Schola Medica Salernitana, the center of European medical knowledge in the High Middle Ages.  It was based in part on the \"Antidotarium\" of Constantine the African, an 11th-century work also written in Salerno which was itself partially a translation of older Arabic works.  It has been called \"without doubt one of the most influential medical texts in medieval literature\", \"the essential pharmacopeia of the Middle Ages\" and \"the bible of medieval practical pharmacy\".  It was often coupled with the \"Circa instans\", another 12th century compendium of less complex medicines.\n\nPearl in the Palm: The Pearl in the Palm or the Timely Pearl (Tangut: 𗼇𘂜𗟲𗿳𗖵𘃎𘇂𗊏 ; ) is a bilingual glossary between the <a href=\"Chinese%20language\">Chinese</a> and <a href=\"Tangut%20language\">Tangut</a> languages.  It survives as a single complete copy of a 12th-century woodblock printed book that was discovered in the Tangut city of Kharakhoto.  In addition, a single page from a different copy of the same edition of the \"Pearl in the Palm\" was found at the Northern Mogao Caves in 1989.  The book transcribes the pronunciation of Chinese words into Tangut characters, and the pronunciation of Tangut characters into Chinese characters, and so is a very important source for Tangut historical phonology, and was the primary source before the publication of monolingual Tangut dictionaries.\n\nGenerative grammar: Generative grammar is a linguistic theory that regards grammar as a system of rules that generates exactly those combinations of words that form grammatical sentences in a given language.  Noam Chomsky first used the term in relation to the theoretical linguistics of grammar that he developed in the late 1950s.  Linguists who follow the generative approach have been called generativists.  The generative school has focused on the study of syntax, but has also addressed other aspects of a language's structure, including morphology and phonology.\n\nThe Sound Pattern of English: The Sound Pattern of English (frequently referred to as SPE) is a 1968 work on phonology (a branch of linguistics) by Noam Chomsky and Morris Halle.  It presents a view of the phonology of English, and has been very influential in both the field of phonology and in the analysis of the English language.  Chomsky and Halle present a view of phonology as a linguistic subsystem, separate from other components of the grammar, that transforms an underlying phonemic sequence according to rules and produces as its output the phonetic form that is uttered by a speaker.  The theory fits with the rest of Chomsky's early theories of language in the sense that it is transformational; as such it serves as a landmark in Chomsky's theories by adding a clearly articulated theory of phonology to his previous work which focused on syntax.\n\nFirst Grammatical Treatise: The First Grammatical Treatise (Icelandic: \"Fyrsta málfræðiritgerðin\" ) is a 12th-century work on the phonology of the Old Norse or Old Icelandic language.  It was given this name because it is the first of four grammatical works bound in the Icelandic manuscript \"Codex Wormianus\".  The anonymous author is today often referred to as the \"First Grammarian\".\n\nAmr ibn Matta: ʿAmr ibn Mattā or Mattai al-Ṭīrhānī (Latin: \"Amrus\" ) was the author of a 14th-century work known as The Book of the Tower (Arabic: ‎ ‎ \"Kitāb al-Majdal li-l-Istibṣār wa-l-Jadal\").  Ibn Matta's work is modelled after, and takes its title from, the \"Book of the Tower\" by 12th-century Nestorian writer Mari ibn Suleiman. Ibn Matta's work is discussed in a lengthy entry in the ecclesiastical encyclopedia \"Miṣbāḥ al-Zulma\" by Ibn Kabar (d. 1324).\n\nDictogloss: Dictogloss is a language teaching technique that is used to teach grammatical structures, in which students form small groups and summarize a target-language text.  First, the teacher prepares a text that contains examples of the grammatical form to be studied.  The teacher reads the text to the students at normal speed while they take notes.  Students then work in small groups to prepare a summary of their work using the correct grammatical structures, and finally each group presents their work to the rest of the class.  Dictogloss activities encourage learners to focus on the form of their language while also being based in communication, and are used in task-based language teaching.\n\nQuestion:  who speaks the language which is theThe First Grammatical Treatiseis a 12th-century work on its phonology\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"work_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the grammatical treatise.\"\n    },\n    \"century_of_work\": {\n      \"type\": \"string\",\n      \"description\": \"The century in which the work was created.\"\n    },\n    \"language_of_focus\": {\n      \"type\": \"string\",\n      \"description\": \"The language that the treatise focuses on.\"\n    },\n    \"speakers\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"The groups of people who spoke the language.\"\n    },\n    \"speaker_location\": {\n      \"type\": \"string\",\n      \"description\": \"The primary geographical location of the speakers.\"\n    }\n  },\n  \"required\": [\n    \"work_title\",\n    \"century_of_work\",\n    \"language_of_focus\",\n    \"speakers\",\n    \"speaker_location\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "work_title": {
        "type": "string",
        "description": "The title of the grammatical treatise."
      },
      "century_of_work": {
        "type": "string",
        "description": "The century in which the work was created."
      },
      "language_of_focus": {
        "type": "string",
        "description": "The language that the treatise focuses on."
      },
      "speakers": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "The groups of people who spoke the language."
      },
      "speaker_location": {
        "type": "string",
        "description": "The primary geographical location of the speakers."
      }
    },
    "required": [
      "work_title",
      "century_of_work",
      "language_of_focus",
      "speakers",
      "speaker_location"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

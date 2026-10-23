{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAmarna Period: The Amarna Period was an era of Egyptian history during the latter half of the Eighteenth Dynasty when the royal residence of the pharaoh and his queen was shifted to Akhetaten ('Horizon of the Aten') in what is now Amarna.  It was marked by the reign of Amenhotep IV, who changed his name to Akhenaten (1353–1336 BC) in order to reflect the dramatic change of Egypt's polytheistic religion into one where the sun disc Aten was worshipped over all other gods.  Aten was not solely worshipped (the religion was not monotheistic), but the other gods were worshipped to a significantly lesser degree.  The Egyptian pantheon of the equality of all gods and goddesses was restored under Akhenaten's successor, Tutankhamun.\n\nMuisca religion and mythology: The terms Muisca religion and mythology refer to the pre-Columbian beliefs of the Muisca indigenous people of the Cordillera Oriental highlands of the Andes in the vicinity of Bogotá, Colombia.  The tradition includes a selection of received myths concerning the origin and organization of the universe.  Their belief system may be described as a polytheistic religion containing a very strong element of spirituality based on an epistemology of mysticism.\n\nTongan religion: Though it is no longer practiced today, Tonga's ancient religion was practiced for over 2000 years.  Missionaries arrived and persuaded King George Tupou I to convert to Christianity; he ordered and strictly enforced that all Tongans become Christian and no longer practice the ancient polytheistic religion with its supreme god Tangaloa.\n\nAztec religion: The Aztec religion is the Mesoamerican religion of the Aztecs. Like other Mesoamerican religions, it had elements of human sacrifice in connection with a large number of religious festivals which were held according to patterns of the Aztec calendar.  Polytheistic in its theology, the religion recognized a large and ever increasing pantheon of gods and goddesses; the Aztecs would often incorporate deities whose cults came from other geographic regions or peoples into their own religious practice.\n\nAdonism: Adonism is a Neopagan religion founded in 1925 by the German esotericist Franz Sättler (1884-c.1942), who often went by the pseudonym of Dr. Musalam.  Although Sättler claimed that it was the continuation of an ancient pagan religion, it has been recognised by academics as being \"instead the single-handed creation of a highly gifted and educated man\", this figure being Sättler himself.  Adonism is a polytheistic religion, revolving around a belief that there are five principal gods: Belus, Biltis, Adonis, Dido and Molchos.  Adonis is the most prominent of these in the group's theology, being a benevolent figure that Sättler equated with the Christian figure of Satan.  In contrast to Adonis, Molchos is believed by Adonists to be malevolent, and to be responsible for the enslavement of humanity through monotheistic religions such as Judaism, Christianity and Islam: the religion therefore has \"a pronounced anti-Christian bias\".\n\nHurrian religion: The Hurrian religion was the polytheistic religion of the Hurrians, a Bronze Age people of the Near East.  These people settled over a wide area, so there were differences between them, especially between the eastern Hurrians around Nuzi and Arrapha and the western Hurrians in Syria and Anatolia.  From the 14th century BC, the Hurrian religion had a powerful influence on the Hittite religion and the Hurrian pantheon is depicted in the 13th century rock reliefs at the important Hittite sanctuary at Yazılıkaya.\n\nPantheon (religion): A pantheon (from Greek πάνθεον \"pantheon\", literally \"(a temple) of all gods\", \"of or common to all gods\" from πᾶν \"pan-\" \"all\" and θεός \"theos\" \"god\") is the particular set of all gods of any polytheistic religion, mythology, or tradition:\n\nOmetochtli: In Aztec mythology, Ometochtli is the collective or generic name of various individual deities and supernatural figures associated with pulque (\"octli \"), an alcoholic beverage derived from the fermented sap of the \"maguey\" plant.  By the Late Postclassic period of Mesoamerican chronology a collection of beliefs and religious practices had arisen in the context of the manufacture and ritualistic consumption of the beverage, known as the \"pulque (or octli) cult\" with probable origins in a mountainous region of central Mexico.  In Aztec society \"octli\" rituals formed a major component of Aztec religion and observance, and there were numerous local deities and classes of \"sacerdotes\" (\"priests\") associated with it.\n\nFinnish paganism: Finnish paganism was the indigenous pagan religion in Finland, Estonia, and Karelia prior to Christianisation.  It was a polytheistic religion, worshipping a number of different deities.  The principal god was the god of thunder and the sky, Ukko; other important gods included Jumi, Ahti, and Tapio.\n\nPrussian mythology: The Prussian mythology was a polytheistic religion of the Old Prussians, indigenous peoples of Prussia before the Prussian Crusade waged by the Teutonic Knights.  It was closely related to other Baltic faiths, the Lithuanian and Latvian mythologies.  Its myths and legends did not survive as Prussians became Germanized and extinct in the early 18th century.  Fragmentary information on gods and rituals can be found in various medieval chronicles, but most of them are unreliable.  No sources document pagan religion before the forced Christianization in the 13th century.  Most of what is known about Prussian religion is obtained from dubious 16th-century sources (\"Sudovian Book\" and Simon Grunau).\n\nQuestion: Which polytheistic religion has mythology regarding Ometochtili?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"religion_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the polytheistic religion.\"\n    },\n    \"is_polytheistic\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the religion is polytheistic.\"\n    },\n    \"mythological_figure\": {\n      \"type\": \"string\",\n      \"description\": \"The specific mythological figure mentioned in the question.\"\n    },\n    \"figure_description\": {\n      \"type\": \"string\",\n      \"description\": \"A brief description of the mythological figure.\"\n    },\n    \"associated_cults\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"Cults or practices associated with the mythological figure.\"\n    }\n  },\n  \"required\": [\n    \"religion_name\",\n    \"is_polytheistic\",\n    \"mythological_figure\",\n    \"figure_description\",\n    \"associated_cults\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "religion_name": {
        "type": "string",
        "description": "The name of the polytheistic religion."
      },
      "is_polytheistic": {
        "type": "boolean",
        "description": "Indicates if the religion is polytheistic."
      },
      "mythological_figure": {
        "type": "string",
        "description": "The specific mythological figure mentioned in the question."
      },
      "figure_description": {
        "type": "string",
        "description": "A brief description of the mythological figure."
      },
      "associated_cults": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Cults or practices associated with the mythological figure."
      }
    },
    "required": [
      "religion_name",
      "is_polytheistic",
      "mythological_figure",
      "figure_description",
      "associated_cults"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

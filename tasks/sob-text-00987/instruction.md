{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nPoggio Reale (villa): The Poggio Reale villa or Villa Poggio Reale was an Italian Renaissance villa commissioned in 1487 by Alfonso II of Naples as a royal summer residence.  The Italian phrase \"poggio reale\" translates to \"royal hill\" in English.  The villa was designed and built by Giuliano da Maiano and located in the city of Naples, in the district now known as Poggioreale, between the present Via del Campo, Via Santa Maria del Pianto and the new and old Via Poggioreale.  At the time it was built, a period when the capitol city of the Kingdom of Naples was renowned for elegant homes with expansive vistas of the surrounding landscape and Mount Vesuvius, the villa was outside the city walls of Naples and was one of the most important architectural achievements of the Neapolitan Renaissance.  Imitated, admired, robbed of its treasures by another king, left in ruins and partially destroyed, the summer palace of the King of Naples lives on in name as a style.\n\nPoggio Bracciolini: Gian Francesco Poggio Bracciolini (11 February 1380 – 30 October 1459), best known simply as Poggio Bracciolini, was an Italian scholar and an early humanist.  He was responsible for rediscovering and recovering a great number of classical Latin manuscripts, mostly decaying and forgotten in German, Swiss, and French monastic libraries.  His most celebrated find was \"De rerum natura\", the only surviving work by Lucretius.\n\nAstronomica (Manilius): The Astronomica (] or ]), also known as the Astronomicon, is a Latin didactic poem written in hexameters and divided into five books about celestial phenomena.  The \"Astronomica\" was penned c. AD 10– 20 by a Roman poet whose name was likely Marcus Manilius; little is known of Manilius, and although there is evidence that the \"Astronomica\" was read by many other Roman writers, no surviving works quote him.  The poem was rediscovered c. 1416– 1417 by the Italian humanist and scholar Poggio Bracciolini, who had a copy made from which the modern text derives.\n\nArchestratus: Archestratus (Greek: Ἀρχέστρατος \"Archestratos\") was an ancient Greek poet of Gela or Syracuse, in Sicily, who wrote some time in the mid 4th century BCE, and was known as \"the Daedalus of tasty dishes\".  His humorous didactic poem \"Hedypatheia\" (\"Life of Luxury\"), written in hexameters but known only from quotations, advises a gastronomic reader on where to find the best food in the Mediterranean world.  The writer, who was styled in antiquity the Hesiod or Theognis of gluttons, parodies the pithy style of older gnomic poets; most of his attention is given to fish, although some fragments refer to appetizers, and there was also a section on wine.  His poem had a certain notoriety among readers in the 4th and 3rd centuries BCE: it was referred to by the comic poet Antiphanes, by Lynceus of Samos and by the philosophers Aristotle, Chrysippus and Clearchus of Soli.  In nearly every case these references are disparaging, implying that Archestratus's poem—like the sex manual by Philaenis - was likely to corrupt its readers.  This attitude is exemplified in the \"Deipnosophistae\" with citations of Chrysippus:\n\nMarsilio Ficino: Marsilio Ficino (] ; Latin name: \"Marsilius Ficinus\"; 19 October 1433 – 1 October 1499) was an Italian scholar and Catholic priest who was one of the most influential humanist philosophers of the early Italian Renaissance.  He was an astrologer, a reviver of Neoplatonism in touch with every major academic thinker and writer of his day and the first translator of Plato's complete extant works into Latin.  His Florentine Academy, an attempt to revive Plato's Academy, influenced the direction and tenor of the Italian Renaissance and the development of European philosophy.\n\nGiovanni Tortelli: Giovanni Tortelli (around 1400 – before 26 April 1466) was a Renaissance humanist, largely responsible for the creation of the Vatican Library, together with scholars such as Bessarion and Poggio Bracciolini.\n\nFacetiae: The Facetiae is an anthology of jokes by Poggio Bracciolini (1380–1459), first published in 1470.  The collection, \"the most famous jokebook of the Renaissance\", is notable for its inclusion of scatological jokes and tales, six of the tales involving farting and six involving defecation.\n\nLe Mondain: Le Mondain (\"The Worldling\" or \"The Man of the World\") is a philosophical poem written by French enlightenment writer and philosopher Voltaire in 1736.  It satirises Christian imagery, including the story of Adam and Eve, to defend a way of life focused on worldly pleasure rather than the promised pleasure of a religion's afterlife.  It opposes religious morality and especially the teaching of original sin.  Its points echo Voltaire's prose works \"Lettres philosophiques\" and \"Remarques sur Pascal\".  Voltaire noted a trend against using poetic forms to make philosophical arguments, and wrote \"Le Mondain\" in deliberate opposition to this trend.\n\nLucretius: Titus Lucretius Carus ( ; 15 October 99 BC – c. 55 BC) was a Roman poet and philosopher.  His only known work is the didactic philosophical poem \"De rerum natura\" about the tenets and philosophy of Epicureanism, and which is usually translated into English as \"On the Nature of Things\".  Lucretius has been credited with originating the concept of the three-age system which was formalised from 1834 by C. J. Thomsen.\n\nSyair: Syair (Jawi: شعير) is a form of traditional Malay poetry that made up of four-line stanzas or quatrains.  The syair can be a narrative poem, a didactic poem, or a poem used to convey ideas on religion or philosophy, or even one to describe historical event.\n\nQuestion: Which didactic philosophical poem about the tenets and philosophy of Epicureanism is the most celebrated find of the Italian scholar Poggio Bracciolini?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"poem_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the didactic philosophical poem.\"\n    },\n    \"poem_genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre or type of the poem, e.g., 'didactic philosophical poem'.\"\n    },\n    \"philosophical_school\": {\n      \"type\": \"string\",\n      \"description\": \"The philosophical school whose tenets and philosophy are discussed in the poem.\"\n    },\n    \"rediscoverer\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the scholar who rediscovered the poem.\"\n        },\n        \"description\": {\n          \"type\": \"string\",\n          \"description\": \"A brief description of the rediscoverer's profession or role.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"description\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"original_author\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the original author of the poem.\"\n        },\n        \"nationality\": {\n          \"type\": \"string\",\n          \"description\": \"The nationality or origin of the original author.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"nationality\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"poem_title\",\n    \"poem_genre\",\n    \"philosophical_school\",\n    \"rediscoverer\",\n    \"original_author\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "poem_title": {
        "type": "string",
        "description": "The title of the didactic philosophical poem."
      },
      "poem_genre": {
        "type": "string",
        "description": "The genre or type of the poem, e.g., 'didactic philosophical poem'."
      },
      "philosophical_school": {
        "type": "string",
        "description": "The philosophical school whose tenets and philosophy are discussed in the poem."
      },
      "rediscoverer": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the scholar who rediscovered the poem."
          },
          "description": {
            "type": "string",
            "description": "A brief description of the rediscoverer's profession or role."
          }
        },
        "required": [
          "name",
          "description"
        ],
        "additionalProperties": false
      },
      "original_author": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the original author of the poem."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality or origin of the original author."
          }
        },
        "required": [
          "name",
          "nationality"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "poem_title",
      "poem_genre",
      "philosophical_school",
      "rediscoverer",
      "original_author"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nPierre Versins: Pierre Versins (born Jacques Chamson January 12, 1923- April 18, 2001) was a French Science Fiction collector and scholar.  From 1957-62, he published a critical fanzine, \"Ailleurs\".  He published four science fiction novels between 1951 and 1971, including \"En avant, Mars\", \"Les etoiles ne s'en foutent pas\", \"Leprofesseur\", and \"Les transhumains\".  His wife, Martine Thome, is credited as a co-author on many of his short stories.  Versins published \"Encyclopedie de Utopie et de la sf\", which won a special award at Torcon II, the 1973 Worldcon and he won a Pilgrim Award from the Science Fiction Research Association in 1991.  In 1975, he founded the Maison d'Ailleurs, a museum of science fiction, utopia and extraordinary journey in Yverdon-les-Bains, (Switzerland).  During World War II, Versins was incarcerated in Auschwitz.\n\nLes Maîtres du temps: Les Maîtres du temps (lit.  \"The Masters of Time\", a.k.a. \"Time Masters\", \"Az idő urai\" in Hungarian) is a 1982 Franco-Hungarian animated science fiction feature film directed by René Laloux and designed by Mœbius.  It is based on the 1958 science fiction novel \"L'Orphelin de Perdide\" (\"The Orphan of Perdide\") by Stefan Wul.\n\nTokyo: The Last Megalopolis: Tokyo: The Last Megalopolis (Japanese: 帝都物語 , Hepburn: Teito Monogatari ) is a tokusatsu historical dark fantasy/science fiction epic film directed by Akio Jissoji, produced by \"Exe\" studios and distributed by Toho Studios.  It is the first cinematic adaptation of the award-winning historical fantasy novel \"Teito Monogatari\" by Hiroshi Aramata.  The plot is a reimagining of Tokyo's early 20th century history from an occultist perspective.  The film stars Kyusaku Shimada, Shintaro Katsu, Koji Takahashi, Jo Shishido, Junichi Ishida, Mieko Harada, Ko Nishimura, and Shiro Sano among others.  With a budget of around 1 billion yen (roughly $8 million), the movie was one of the most expensive live action Japanese special effects films to have ever been produced during that decade (by contrast, the internationally released 1984 film \"The Return of Godzilla\" was only budgeted at $6.25 million).\n\nStar Wars: Where Science Meets Imagination: \"Star Wars\": Where Science Meets Imagination is a traveling exhibition created by the Museum of Science, Boston, featuring props and costumes used in the \"Star Wars\" films, but focusing primarily on the science behind George Lucas' science fiction epic.  \"Star Wars: Where Science Meets Imagination\" was developed by Boston's Museum of Science, in collaboration with Lucasfilm Ltd., with the support of the National Science Foundation, under Grant No. 0307875.  This exhibit is presented nationally by Bose Corporation.\n\nStefan Wul: Stefan Wul was the \"nom de plume\" of the French science fiction writer Pierre Pairault (27 March 1922 – 26 November 2003).  He was a dental surgeon, but science fiction was his real passion.  Most of his books reflect that, showing a deep knowledge of scientific data.  Pairault retired from dental surgery in 1989, but remained active in the French science fiction scene.\n\nIn Search of Wonder: In Search of Wonder: Essays on Modern Science Fiction is a collection of critical essays by American writer Damon Knight.  Most of the material in the original version of the book was originally published between 1952 and 1955 in various science fiction magazines including \"Infinity Science Fiction\", \"Original SF Stories\", and \"Future SF\".  The essays were highly influential, and contributed to Knight's stature as the foremost critic of science fiction of his generation.  The book also constitutes an informal record of the \"Boom Years\" of science fiction from 1950-1955.\n\nSEK Studio: Scientific Educational Korea or SEK Studio (Chosŏn'gŭl: 조선4·26아동영화촬영소 ; lit.  \"Korean April 26 Children's Film Studio\" ) is a North Korean animation studio, based in Othan-dong, Central District, Pyongyang.  SEK has done work on several animated series from Mondo TV, including \"\"Pocahontas: Princess of the American Indians\"\" and \"\", (due to this two, it has been repeatedly misinformed that SEK has worked for The Walt Disney Company).  SEK also has produced features such as the French science fiction epic \"Gandahar\" (\"The Light Years\") and \"Empress Chung\".\n\nFantastic Planet: Fantastic Planet (French: La Planète sauvage , Czech: Divoká planeta , lit.  \"The Wild Planet\") is a 1973 animated science fiction film directed by René Laloux and written by Laloux and Roland Topor.  Topor also completed the film's production design and it was animated at Jiří Trnka Studio in Prague.  The film was an international co-production between companies from France and Czechoslovakia.  The allegorical story, about humans living on a strange planet dominated by giant humanoid aliens who consider them animals, is based on the 1957 novel \"Oms en série\" by French writer Stefan Wul.\n\nJean-Pierre Andrevon: Jean-Pierre Andrevon (born 19 September 1937 in Bourgoin-Jallieu, Isère) is a French science fiction author, as well as a painter and singer.  He has used the pseudonym \"Alphonse Brutsche\" for novels published under the Fleuve Noir label.  In addition to his regular authorship, he has written scenarios for several prominent comics artists, among others Georges Pichard and Caza, resulting in a body of comic book work.  He has also edited a number of anthologies of French science fiction.\n\nGandahar (film): Gandahar is a 1988 French animated science fantasy film.  The original version was directed by René Laloux, and was based on Jean-Pierre Andrevon's novel \"Les Hommes-machines contre Gandahar\" (\"The Machine-Men versus Gandahar\").\n\nQuestion: Scientific Educational Korea or SEK Studio produced which French science fiction epic whose original version was directed by René Laloux?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the film.\"\n        },\n        \"genre\": {\n          \"type\": \"string\",\n          \"description\": \"The genre of the film, as described in the context.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"genre\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"director\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the film's director.\"\n        }\n      },\n      \"required\": [\n        \"name\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"production_studio\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the studio that produced the film.\"\n        },\n        \"country_of_origin\": {\n          \"type\": \"string\",\n          \"description\": \"The country where the production studio is based.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"country_of_origin\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"film\",\n    \"director\",\n    \"production_studio\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the film."
          },
          "genre": {
            "type": "string",
            "description": "The genre of the film, as described in the context."
          }
        },
        "required": [
          "title",
          "genre"
        ],
        "additionalProperties": false
      },
      "director": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the film's director."
          }
        },
        "required": [
          "name"
        ],
        "additionalProperties": false
      },
      "production_studio": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the studio that produced the film."
          },
          "country_of_origin": {
            "type": "string",
            "description": "The country where the production studio is based."
          }
        },
        "required": [
          "name",
          "country_of_origin"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "film",
      "director",
      "production_studio"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

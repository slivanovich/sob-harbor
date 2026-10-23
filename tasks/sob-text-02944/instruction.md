{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nZé Ramalho: Zé Ramalho (born José Ramalho Neto on October 3, 1949 - Brejo do Cruz - Paraíba, Brazil) is a Brazilian composer and performer.  Zé Ramalho has collaborated with various major Brazilian musicians, including Vanusa, Geraldo Azevedo and Alceu Valença to name a few.  Ze Ramalho is also the first cousin of Elba Ramalho, a well known Brazilian composer and performer.\n\nHeitor Villa-Lobos: Heitor Villa-Lobos (] ; March 5, 1887November 17, 1959) was a Brazilian composer, described as \"the single most significant creative figure in 20th-century Brazilian art music\".  Villa-Lobos has become the best-known South American composer of all time.  A prolific composer, he wrote numerous orchestral, chamber, instrumental and vocal works, totaling over 2000 works by his death in 1959.  His music was influenced by both Brazilian folk music and by stylistic elements from the European classical tradition, as exemplified by his \"Bachianas Brasileiras\" (Brazilian Bachian-pieces).  His Etudes for guitar (1929) were dedicated to Andrés Segovia while his 5 Preludes (1940) were dedicated to Arminda Neves d’Almeida, a.k.a. \"Mindinha\", both are important works in the guitar repertory.\n\nPaulo Costa Lima: Brazilian composer and music theorist, whose main interest has been the vivid interaction between composition and culture, including the political aspects of it, namely, composition as a way of resisting cultural colonization.  He has published books and articles on subjects such as the theory and pedagogy of musical composition, analysis and history of Brazilian contemporary music, analysis of Brazilian popular songs, and the possible dialogue between music, psychoanalysis and cultural semantics.  A member of the Brazilian Academy of Music (created by Heitor Villa-Lobos in 1945), he has received along the last decades more than twenty prizes and commissions.  He belongs to the second generation of the movement initiated by the ‘Group of Composers of Bahia’ that was formed in 1966, launching a one-line manifesto “In principle, we are against all and every asserted principle”.  The manifesto also implies that all suggestions are valid and acceptable, and this inclusivity reflects the cultural diversity and relativity of Bahia - a society created by the encounter and conflict of three civilizations (Europe, Africa and Native American).  Since 1992 his compositional interests addressed the rhythmic tradition of Afro-Bahian candomblé, creating universes of hybridization and contradiction, non-sequitur and humor, involving Afro-Bahian and Avant-Garde contexts and ideas.  He has mentored a new generation of Brazilian composers such as Guilherme Bertissolo, Paulo Rios Filho, Alex Pochat, Tulio Augusto, Vinicius Amaro and Danniel Ferraz.\n\nRemilson Nery: Remilson Nery is a Brazilian composer.\n\nEdu da Gaita: Edu da Gaita (lit.  \"Edu of the Harmonica\", born Eduardo Nadruz in Jaguarão on October 13, 1916 - Rio de Janeiro on August 23, 1982) was a Brazilian composer and harmonica player.  Apart from releasing multiple solo albums, he also performed with Brazilian composer Radamés Gnattali and his sextet, touring Europa and South America\n\nLourival Fontes: Lourival Fontes (July 20, 1899 – March 6, 1967) was a Brazilian journalist and politician best known for being the propaganda minister for President Getúlio Vargas between 1934 and 1942.  He was born in Riachão do Dantas, Sergipe and married the poet Adalgisa Nery in 1940.  He also served as the Ambassador of Brazil to Mexico.\n\nCaetano Veloso: Caetano Emanuel Viana Telles Veloso (] ; born August 7, 1942), better known as Caetano Veloso, is a Brazilian composer, singer, guitarist, writer, and political activist.  Veloso first became known for his participation in the Brazilian musical movement Tropicalismo, which encompassed theatre, poetry and music in the 1960s, at the beginning of the Brazilian military dictatorship.  He has remained a constant creative influence and best-selling performing artist and composer ever since.  Veloso has won nine Latin Grammy Awards and two Grammy Awards.  On November 14, 2012, Veloso was honored as the Latin Recording Academy Person of the Year.\n\nJosé Antônio Rezende de Almeida Prado: José Antônio Rezende de Almeida Prado or Almeida Prado (February 8, 1943 – November 21, 2010) was an important Brazilian composer of classical music and a pianist.  On Almeida Prado's death, his personal friend, conductor João Carlos Martins stated that Prado had possibly been the most important living Brazilian composer.\n\nOsvaldo Lacerda: Osvaldo Costa de Lacerda (March 23, 1927 – July 18, 2011) was a Brazilian composer.  In 1962, he became the first Brazilian composer to receive a Guggenheim Fellowship.  He began piano study at nine, and studied under Camargo Guarnieri and Aaron Copland.  After traveling and spending some time in the United States, he returned to São Paulo, where he taught extensively and founded the Centro de Musica Brasilia.\n\nAdalgisa Nery: Adalgisa Nery (October 29, 1905 – June 7, 1980) was a Brazilian poet, journalist and politician.  She was born in Rio de Janeiro as Adalgisa Maria Feliciana Noel Cancela Ferreira, the daughter of a civil servant.  In 1922 she married Ismael Nery (1900–1934), a painter and poet who introduced Adalgisa to a circle of Brazilian artists and intellectuals that included Manuel Bandeira, Jorge de Lima and Murilo Mendes.  The Nerys lived in Europe from 1927 to 1929, where they met the artist Marc Chagall and the Brazilian composer Heitor Villa-Lobos.  Ismael died of tuberculosis in 1934, leaving Adalgisa with two sons.\n\nQuestion: In which year was the Brazilian composer died with whom Adalgisa Nery met in Europe in between 1927 to 1929?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"composer_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the Brazilian composer.\"\n    },\n    \"death_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the composer died.\"\n    },\n    \"meeting_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"person_met_with\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the person who met the composer.\"\n        },\n        \"location\": {\n          \"type\": \"string\",\n          \"description\": \"The location where the meeting took place.\"\n        },\n        \"meeting_period_start_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The start year of the period when the meeting occurred.\"\n        },\n        \"meeting_period_end_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The end year of the period when the meeting occurred.\"\n        }\n      },\n      \"required\": [\n        \"person_met_with\",\n        \"location\",\n        \"meeting_period_start_year\",\n        \"meeting_period_end_year\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"composer_name\",\n    \"death_year\",\n    \"meeting_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "composer_name": {
        "type": "string",
        "description": "The name of the Brazilian composer."
      },
      "death_year": {
        "type": "integer",
        "description": "The year the composer died."
      },
      "meeting_details": {
        "type": "object",
        "properties": {
          "person_met_with": {
            "type": "string",
            "description": "The name of the person who met the composer."
          },
          "location": {
            "type": "string",
            "description": "The location where the meeting took place."
          },
          "meeting_period_start_year": {
            "type": "integer",
            "description": "The start year of the period when the meeting occurred."
          },
          "meeting_period_end_year": {
            "type": "integer",
            "description": "The end year of the period when the meeting occurred."
          }
        },
        "required": [
          "person_met_with",
          "location",
          "meeting_period_start_year",
          "meeting_period_end_year"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "composer_name",
      "death_year",
      "meeting_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

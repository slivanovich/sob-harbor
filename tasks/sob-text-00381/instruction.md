{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nParlophone: Parlophone Records Limited (also known as Parlophone Records and Parlophone) is a German-British major record label founded in Germany in 1896 by the Carl Lindström Company as Parlophon.  The British branch of the company was founded in 8 August 1923 as The Parlophone Co. Ltd., which developed a reputation in the 1920s as a leading jazz record label.  On 5 October 1926, the Columbia Graphophone Company acquired Parlophone's business, name and release library, and later merged with the Gramophone Company on 31 March 1931 to become Electric & Musical Industries Limited (EMI).  George Martin joined EMI in 1950 as assistant label manager, taking over as manager in 1955.  Martin produced and released a mix of product including comedy recordings of The Goons, the pianist Mrs Mills, and teen idol Adam Faith.\n\nFort Hall: Fort Hall was built in 1834 as a fur trading post by Nathaniel Jarvis Wyeth on the Snake River in the eastern Oregon Country, part of southeastern Idaho in the present-day United States.  He was an inventor and businessman from Boston, Massachusetts, who also founded a post at Fort William, in present-day Portland, Oregon, as part of a plan for a new trading and fisheries company.  Unable to compete with the powerful British Hudson's Bay Company, based at Fort Vancouver, in 1837 Wyeth sold both posts to it.  Great Britain and the United States both operated in the Oregon Country in these years.\n\nNippon Columbia: Nippon Columbia Co., Ltd. (日本コロムビア株式会社 , Nippon Koromubia Kabushiki Kaisha ) , often pronounced \"Korombia\", , is a Japanese record label founded in 1910 as Nipponophone Co., Ltd. (日本蓄音器商会 , Nihon Chikuonki Shōkai ) .  It affiliated itself with the Columbia Graphophone Company of the United Kingdom and adopted the standard UK Columbia trademarks in 1931.  The company changed its name to Nippon Columbia Co., Ltd. in 1946.  It used the Nippon Columbia name until October 1, 2002, when it became Columbia Music Entertainment, Inc. (コロムビアミュージックエンタテインメント株式会社 , Koromubia Myūjikku Entateinmento Kabushiki gaisha ) .  On October 1, 2010, the company returned to its current name.  Outside Japan, the company operates as the Savoy Label Group which releases recordings on the SLG, Savoy Jazz and Denon labels.  It also manufactured electronic products under the Denon brand name until 2001.\n\nAlexander Graham Bell: Alexander Graham Bell (March 3, 1847 – August 2, 1922) was a Scottish-born scientist, inventor, engineer, and innovator who is credited with patenting the first practical telephone and founding the American Telephone and Telegraph Company (AT&T) in 1885.\n\nGraphophone: The Graphophone was the name and trademark of an improved version of the phonograph.  It was invented at the Volta Laboratory established by Alexander Graham Bell in Washington, D.C., United States.\n\nWilliam Woodnut Griscom: William Woodnut Griscom (1851–1897) was an American inventor responsible for introducing electric motors for the purpose of marine propulsion.  With some 40 patents to his name, Griscom also founded the Electro-Dynamic Company in 1880, based in Philadelphia.  Much information in regards to Electro-Dynamic Company (and its origins) has not been made altogether clear.  In 1892, Isaac Rice bailed Electro-Dynamic out following a bankruptcy and became a co-owner.  Two years after Griscom died in an 1897 hunting accident, his company was acquired by Rice's new Electric Boat Company.  He was awarded the John Scott Medal of The Franklin Institute in 1882.  He is buried at the Church of the Redeemer Cemetery in Bryn Mawr, Pennsylvania.\n\nColumbia Records: Columbia Records is an American major record label owned by Sony Music Entertainment through Sony Entertainment, both are subsidiaries of Sony Corporation of America, the United States division of Sony Corporation.  It was founded in 1887 from an earlier enterprise named the American Graphophone Company, the successor to the Volta Graphophone Company.\n\nArzest: Arzest (fully known as \"ARZEST Corporation\") is a Japanese video game development company that develops games for video game consoles.  It was formed on June 25, 2010 by key members of Artoon, which was also founded by Arzest Executive Vice President Naoto Ohshima, best known as the character designer of Sonic the Hedgehog, as well as his nemesis Dr. Eggman.  Arzest was also founded by key Artoon and Sega members who worked on the \"Panzer Dragoon\" series.\n\nLyman Scott House: The Lyman Scott House is a historic house located on U.S. Route 54 in Summer Hill, Pike County, Illinois.  The house was built in 1844 by Lyman Scott, who founded Summer Hill the following year.  Scott, an early Pike County settler who also founded Rockport, built the house as a summer home for his family.  The two-story post and beam house features a front porch over its two front entrances; a gabled dormer was added to the porch in 1870.  Scott, a prominent local merchant, also founded and funded Summer Hill's first school.  Scott also served as a representative to the International Peace Conference in 1850.  In 1853, Scott moved to Kansas, where he served in the state legislature.  The house is the oldest surviving building in Summer Hill.\n\nJ. P. McFadden: James Patrick McFadden (1930–1998) was an American journalist and publisher who founded the Ad Hoc Committee in Defense of Life in 1973 as a reaction to the Roe v. Wade decision by the United States Supreme Court.  He also founded the Human Life Foundation, and in 1974 he launched its publication, the \"Human Life Review\", a quarterly journal of scholarship opposed to abortion.  He also founded the National Committee of Catholic Laymen in 1977.\n\nQuestion: The inventor of the Graphophone also founded what company in 1885?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"inventor\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the inventor.\"\n        },\n        \"invention\": {\n          \"type\": \"string\",\n          \"description\": \"The invention associated with the inventor.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"invention\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"founded_company\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the company founded.\"\n        },\n        \"founding_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the company was founded.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"founding_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"relationship_description\": {\n      \"type\": \"string\",\n      \"description\": \"A description of the relationship between the inventor and the company.\"\n    }\n  },\n  \"required\": [\n    \"inventor\",\n    \"founded_company\",\n    \"relationship_description\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "inventor": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the inventor."
          },
          "invention": {
            "type": "string",
            "description": "The invention associated with the inventor."
          }
        },
        "required": [
          "name",
          "invention"
        ],
        "additionalProperties": false
      },
      "founded_company": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the company founded."
          },
          "founding_year": {
            "type": "integer",
            "description": "The year the company was founded."
          }
        },
        "required": [
          "name",
          "founding_year"
        ],
        "additionalProperties": false
      },
      "relationship_description": {
        "type": "string",
        "description": "A description of the relationship between the inventor and the company."
      }
    },
    "required": [
      "inventor",
      "founded_company",
      "relationship_description"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

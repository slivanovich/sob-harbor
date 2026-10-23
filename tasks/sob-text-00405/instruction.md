{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nLos Angeles Dance Theater: The Los Angeles Dance Theater is a dance-oriented production company founded in 2003 by George Balanchine protege John Clifford.  The company was requested by Warner Bros.  Theatre Ventures, Inc., the live theatre division of Warner Bros.  Studios.  The company was founded for the purpose of creating a live-stage dance version of the film \"Casablanca\". \" \"Casablanca, The Dance\"\" premiered in Beijing, China on the 5th of April, 2005 at the 10,000 seat \"Great Hall of the People\" to sold-out audiences and standing ovations.  A projected world tour was cancelled when Warner Bros. ceased live theatre operations after the failure of their first Broadway musical, \"Lestat\".  Later, Warner Bros. restarted producing musicals, fueling rumors about the revival of the \"Casablanca, The Dance,\" world tour.\n\nThe Geffen Film Company: The Geffen Film Company (also known as The Geffen Company, The Geffen Film Company, Inc., and later Geffen Pictures) was a film distributor and production company founded by David Geffen, the founder of Geffen Records, and future co-founder of DreamWorks.  Geffen founded the company in 1980, having recruited Eric Eisner as president, and distributed its films through Warner Bros. Geffen operated it as a division of Warner Bros., and as a result, following The Geffen Film Company's shutdown in 1998, Warner Bros. now owns the company's library.  However, the only Geffen Film Company title Warner Bros. does not own is the 1996 Mike Judge comedy \"Beavis and Butt-Head Do America\", itself owned by Paramount Pictures.\n\nWarner Bros. Museum: Warner Bros.  Museum, also known as the Warner Bros.  Studio Tour Archive, is the only studio museum in the movie industry in Burbank, California and is dedicated to Warner Bros. Opened in 1996, the 7,000 sq. foot museum brings together costumes, props, animation cells and letters collected from the history of Warner Bros. film-making and television programs.\n\nWarner Bros. International Television: Warner Bros.  International Television (WBITV) also known as Warner Bros.  Worldwide Television, is the global television arm of Warner Bros.  Television and a subsidiary of Warner Bros.  Entertainment formed in 1996.  It is a part of one of the largest media firms in the world, Time Warner.\n\nDuma (2005 film): Duma is a 2005 American family drama adventure film about a young South African boy's friendship with an orphaned cheetah from a story by Carol Flint and Karen Janszen, set in the country of South Africa and based on \"How It Was with Dooms\" by Carol Cawthra Hopcraft and Xan Hopcraft.  It was distributed by Warner Bros.  Pictures, Gaylord Films and C.O.R.E., directed by Carroll Ballard (director of \"The Black Stallion\" and \"Fly Away Home\"), produced by Gaylord Films, Warner Bros., John Wells Productions, Pandora Pictures, Stacy Cohen, E.K. Gaylord II, Kristin Harms, Hunt Lowry and John Wells, written by Karen Janszen and Mark St. Germain, edited by T.M. Christopher, cinematographed by Werner Maritz with music by George Acogny and John Debney and starring Alexander Michaletos, Eamonn Walker, Campbell Scott and Hope Davis.  The film was theatrically released on April 22, 2005 by Warner Bros.  Pictures, Gaylord Films and C.O.R.E..  The film went on receiving very positive reviews from critics and it earned $994,790 on a $12 million budget.  The film won the Family Feature Film at the Genesis Awards in 2006.  The film was rated PG for mild adventure peril.  \"Duma\" was released on DVD on May 16, 2006 by Warner Bros.  Entertainment.\n\nBugs Bunny: Bugs Bunny is an animated cartoon character; created in 1940 by Leon Schlesinger Productions (later Warner Bros.  Cartoons) and voiced originally by Mel Blanc.  Bugs is best known for his starring roles in the \"Looney Tunes\" and \"Merrie Melodies\" series of animated short films, produced by Warner Bros. During the golden age of American animation, his popularity increased.  This era led to his becoming an American cultural icon and the official mascot of Warner Bros.  Entertainment.\n\nWarner Bros. Records: Warner Bros.  Records Inc. is an American major record label established in 1958 as the foundation label of the present-day Warner Music Group (WMG), and now operates as a wholly owned subsidiary of that corporation.  Warner Bros.  Records was established on March 19, 1958, as the recorded-music division of the American film studio Warner Bros..  For most of its early existence it was one of a group of labels owned and operated by larger parent corporations.  The sequence of companies that controlled Warner Bros. and its allied labels evolved through a convoluted series of corporate mergers and acquisitions from the early 1960s to the early 2000s.  Over this period, Warner Bros.  Records grew from a struggling minor player in the music industry to become one of the top recording labels in the world.\n\nJack Hamm: Jack B. Hamm (March 5, 1916 – December 22, 1996) was an American artist from Wichita, Kansas who is recognized both for his Christian-themed artwork and editorial cartoons, and for his books on drawing technique.  He both studied and taught at the Frederic Mizen Academy of Art.  As a cartoonist and comic strip letterer, he worked on the \"Bugs Bunny\", \"Alley Oop\", and \"Boots and Her Buddies\" comic strips before attending Baylor University to study theology.  He taught at Baylor both before and after he graduated in 1948.\n\nFBI Code 98: FBI Code 98 is a 1962 crime drama directed by Leslie H. Martinson and produced by Warner Bros. Originally intended as television pilot, the film was instead released theatrically in the United Kingdom in 1962, and in the United States in 1964.  \"FBI Code 98\" stars many Warner Bros. contract players such as Jack Kelly, Ray Danton, Andrew Duggan and William Reynolds who later costarred on the Warner Bros Television show \"The F.B.I.\".  The film was narrated by William Woodson who previously narrated the radio show \"The FBI in Peace and War\".\n\nWarner Bros. Studio Store: The Warner Bros.  Studio Store was a chain of retail stores selling Looney Tunes and other merchandise based on Warner Bros. films, similar in style to The Disney Store.  They first opened in 1991.  In 1996, Warner Bros. owner Time Warner merged with Turner Broadcasting, which owned Hanna-Barbera and the pre-1986 MGM library, and merchandise based on Turner properties were added to the product lines.  In 2001, all Warner Bros.  Studio Stores went out of business.  In 2006, Warner Bros.  Consumer Products partnered with PMW Retail and reopened the stores in China.\n\nQuestion: Jack Hamm drew which official Warner Bros. mascot?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"mascot_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the official Warner Bros. mascot.\"\n    },\n    \"company_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the company the mascot represents.\"\n    },\n    \"artist_info\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"artist_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the artist who worked on the mascot's comic strip.\"\n        },\n        \"artist_roles\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"Roles of the artist related to the mascot's comic strip.\"\n        }\n      },\n      \"required\": [\n        \"artist_name\",\n        \"artist_roles\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"mascot_creation_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the mascot character was created.\"\n    }\n  },\n  \"required\": [\n    \"mascot_name\",\n    \"company_name\",\n    \"artist_info\",\n    \"mascot_creation_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "mascot_name": {
        "type": "string",
        "description": "The name of the official Warner Bros. mascot."
      },
      "company_name": {
        "type": "string",
        "description": "The name of the company the mascot represents."
      },
      "artist_info": {
        "type": "object",
        "properties": {
          "artist_name": {
            "type": "string",
            "description": "The name of the artist who worked on the mascot's comic strip."
          },
          "artist_roles": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Roles of the artist related to the mascot's comic strip."
          }
        },
        "required": [
          "artist_name",
          "artist_roles"
        ],
        "additionalProperties": false
      },
      "mascot_creation_year": {
        "type": "integer",
        "description": "The year the mascot character was created."
      }
    },
    "required": [
      "mascot_name",
      "company_name",
      "artist_info",
      "mascot_creation_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

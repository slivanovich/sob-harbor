{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nLerika: Valeriya \"Lerika\" Engalycheva (Russian: Валерия Енгалычева ; born 7 April 1999) is a Moldovan-Russian teen singer who represented Moldova in the Junior Eurovision Song Contest 2011 with the song \"No-No\", and Russia in the 2012 contest with \"Sensatsiya\" (Sensation).\n\nHolly Hull: Holly Hull (born Holly-Anne Hull, 17 October 1994, Camberley, Surrey, England) is an English teen singer who won the Disney Channel UK talent search \"My Camp Rock\" in April 2009, after being voted for by viewers.  She is mentored by specialist vocal coach, Martin-Gwyn Williams and was a member of the West End Kids song & dance troupe from 2006 to 2013.\n\nPopstar (film): Popstar is a 2005 American film directed by Richard Gabai and written by Timothy Barton.  The direct-to-video film features teen singer Aaron Carter in his only lead role in a feature film.  The premiere was held in The Woodlands, Texas.  \"Popstar\" was filmed in Calabasas, California, at A.C. Stelle Middle School and the Commons.\n\nYang Peiyi: Yang Peiyi (born July 8, 2001) is a Chinese teen singer.\n\nAaron Carter: Aaron Charles Carter (born December 7, 1987) is an American singer.  He came to fame as a pop and hip hop singer in the late 1990s, establishing himself as a star among pre-teen and teenage audiences during the early 2000s with his four studio albums.\n\nTrisno: Trisno Ishak, more popularly known as Trisno, was born on 18 July 1978 in Singapore.  He is a musician and a teacher.  In 2000, Trisno came to fame as the lead singer of Urban Xchange, which later evolved to Parking Lot Pimp.  Trisno has performed alongside Stacy Orrico, Jamie Cullum, Jay Sean, Missy Higgins and Ben and Joey of The Click Five.  He has also collaborated with Grammy Award winner John Lennon, Grammy Award nominee Brian McKnight, Mr. Cheeks from The Lost Boyz, Malaysian hip-hop duo Too Phat, Malaysian singer Camelia, Singaporean rapper Sheikh Haikel and Taiwanese popstar Evonne.  With his sizzling buttery voice, Trisno has captivated local and international audience.  Coupled along with his versatility in music and adept talent at working the crowd, he is described as \"the guy who was born to be a performer\".\n\nŠarlote Lēnmane: Šarlote Lēnmane (born 8 February 1998) is a Latvian teen singer.  She represented Latvia in the Junior Eurovision Song Contest 2010 in Minsk, Belarus, after five years of Latvia not participating in the competition.\n\nSam Verlinden: Samuel James Verlinden (born 1 October 1997) also known as Solo Artist Sam V is a New Zealand teen singer and actor.  He is best known for his track 'I Just Wanna Love U' which quickly gained a following after famous choreographer Parris Goebel and the ReQuest dance crew surprised Sam with a music video for the song.\n\nMoxy (band): Moxy is a Canadian hard rock and heavy metal band, formed in Toronto, Ontario, in 1974, from previous members of the rock group Leigh Ashford – which included singer Douglas \"Buzz\" Shearman (former teen singer of Sherman & Peabody), alongside Greg Godovitz of Fludd & Goddo, and Gil Moore (later of Triumph), Earl Johnson (former member of King Biscuit Boy), Bill Wade (former member of Outlaw Music and Brutus under the alias Hally Hunter that also included Gino Scarpelli of Goddo) and Terry Juric, (former member of Outlaw Music) as Leigh Ashford.  The group changed its name to Moxy in late 1974.  This name change was accompanied by a change in the group's sound.  Buddy Caine, a former bandmate of Earl Johnson, was added to the group in 1975.\n\nTracy (English singer): Tracy was a UK teen singer from Wembley who recorded 1969–1971 for Columbia UK record producer Bob Barratt.  In 1971 she recorded \"Strange Love\" for the Hammer Horror film \"Lust for a Vampire\", and again as a 45\".\n\nQuestion: Popstar features which pop and hip-hop teen singer?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"film_release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"featured_singer\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The full name of the featured singer.\"\n        },\n        \"music_genres\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"The music genres associated with the singer.\"\n        },\n        \"role_in_film\": {\n          \"type\": \"string\",\n          \"description\": \"The role the singer played in the film.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"music_genres\",\n        \"role_in_film\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"film_release_year\",\n    \"featured_singer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "film_release_year": {
        "type": "integer",
        "description": "The release year of the film."
      },
      "featured_singer": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The full name of the featured singer."
          },
          "music_genres": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "The music genres associated with the singer."
          },
          "role_in_film": {
            "type": "string",
            "description": "The role the singer played in the film."
          }
        },
        "required": [
          "name",
          "music_genres",
          "role_in_film"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "film_title",
      "film_release_year",
      "featured_singer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

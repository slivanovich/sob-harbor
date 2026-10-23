{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nScrooge McDuck: Scrooge McDuck is a fictional character created in 1947 by Carl Barks during his time as a work-for-hire for The Walt Disney Company.  Scrooge is an elderly Scottish anthropomorphic Pekin duck with a yellow-orange bill, legs, and feet.  He typically wears a red or blue frock coat, top hat, pince-nez glasses, and spats.  He is portrayed in animations as speaking with a Scottish accent.\n\nNawlz: NAWLZ is a 24-episode cyberpunk adventure webcomic created by interactive designer and illustrator Stu Campbell, also known as Sutu.  The comic is designed for interactive storytelling, combining interactivity, animation, music and text.  The comic first launched in late 2008 and was followed by an iPad format in 2011.  The comic story follows Harley Chambers as he navigates through the city of Nawlz, a futuristic city full of overlaying virtual realities, mind-altering drugs and a myriad of techno cultures.\n\nAnantana Avantara: Anantana Avantara is a 1989 Indian Kannada-language comedy film directed by and starring Kashinath.  The movie is a light–hearted comedy about the ordeals of a newly married man.  It set a trend in the comic films in Kannada and established Kashinath as a comic story teller.  The movie was an average grosser but has since then achieved cult status in the later decades.  The movie also introduced Upendra as the lyrics writer and assistant director.\n\nWestside Story (5566 album): \"'Westside Story\" is a soundtrack album for the Taiwanese idol drama TV series Westside Story starring 5566.  This album is credited for bringing fame to two Jungiery artists, Cyndi Wang and the now-defunct bubblegum pop group, R&B.\n\nDonald Duck Finds Pirate Gold: \"Donald Duck Finds Pirate Gold\" is a comic book story starring Donald Duck that was originally printed in \"Four Color\" #9 (the first \"Four Color\" issue titled \"Donald Duck\") in October 1942.  In this story Donald and his nephews Huey, Dewey and Louie meet a parrot named Yellow Beak and they wind up searching for the lost treasure of Henry Morgan.  Unfortunately for them Black Pete wants the treasure too.\n\nWeatherman (short story): \"Weatherman\" is a science fiction short story included in \"The Space Opera Renaissance\" collection.  It was written by Lois McMaster Bujold and was first published in the February 1990 issue of \"Analog Science Fiction and Fact\" and is a prelude story starring a character she also used in the Vorkosigan Saga.  It was republished as the first six chapters of \"The Vor Game\".  \"Weatherman\" was nominated for the Nebula Award for Best Novella, while \"The Vor Game\" won the Hugo Award for Best Novel.\n\nDan Dare: Dan Dare is a British science fiction comic hero, created by illustrator Frank Hampson who also wrote the first stories.  Dare appeared in the \"Eagle\" comic story \"Dan Dare, Pilot of the Future\" from 1950 to 1967 (and subsequently in reprints), and dramatised seven times a week on Radio Luxembourg (1951–1956).\n\nHorsing Around with History: \"Horsing Around with History\" is a 32-page comic book story starring Scrooge McDuck, written by Carl Barks and William Van Horn.  It was released in \"Uncle Scrooge Adventures\" #33 (1995).  This was Barks' next-to-last story released in the United States.  Barks came out of retirement to provide a script for this story and he chose William Van Horn to write this story for him.  This story was originally written to celebrate the 30th anniversary of Carl Barks' retirement.\n\nThe Terror of the Transvaal: \"The Terror of the Transvaal\" is a Scrooge McDuck comic story by Don Rosa.  It is the sixth of the original 12 chapters in the series \"The Life and Times of Scrooge McDuck\".  The story takes place from 1887 to 1889.\n\nCorner Bar Pictures: Corner Bar Pictures is an independent production company focused on all project types from animation to feature-length films.  The emphasis is on projects where CBP is involved very early - typically at the writing phase - and extends through post-production.  Corner Bar Pictures was founded in Summit, NJ in 2013 by Marina Donahue; their debut release, \"All In Time\", won 12 festival awards, prior to its release, on the film festival circuit.  Corner Bar Pictures currently has several projects in production: 'Native', a short film shot in Ireland starring Patrick Bergin; 'The Velvet Underground Played at my High School', an animated documentary about the first time the Velvet's played in public; and 'Indianapolis', based on a Sam Shepard short story starring Bill Pullman and Gabourey Sidibe.  The 5-part web series 'Drama: The Web Series' (starring Rachel Donahue) can be found on You Tube and is being reworked into a short film for festival submissions.  Their next full length feature, 'For The Good of the Child', starring Rachel Donahue, will be shot entirely in Ireland, with an anticipated release date of 2018.\n\nQuestion: The Terror of the Transvaal is a comic story starring a character created by whom?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"story_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the comic story.\"\n    },\n    \"starring_character\": {\n      \"type\": \"string\",\n      \"description\": \"The main character featured in the story.\"\n    },\n    \"character_creator\": {\n      \"type\": \"string\",\n      \"description\": \"The person who created the starring character.\"\n    },\n    \"character_creation_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"creation_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the character was created.\"\n        }\n      },\n      \"required\": [\n        \"creation_year\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"story_title\",\n    \"starring_character\",\n    \"character_creator\",\n    \"character_creation_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "story_title": {
        "type": "string",
        "description": "The title of the comic story."
      },
      "starring_character": {
        "type": "string",
        "description": "The main character featured in the story."
      },
      "character_creator": {
        "type": "string",
        "description": "The person who created the starring character."
      },
      "character_creation_details": {
        "type": "object",
        "properties": {
          "creation_year": {
            "type": "integer",
            "description": "The year the character was created."
          }
        },
        "required": [
          "creation_year"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "story_title",
      "starring_character",
      "character_creator",
      "character_creation_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

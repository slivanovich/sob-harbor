{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJo Wyatt: Joanna Louise Wyatt (born 28 September 1970 in London, England) is an English actress and voice actress known for her voice as Little Miss Helpful, Little Miss Naughty, Little Miss Scary and Little Miss Sunshine in \"The Mr. Men Show\".  She also voiced Daisy Kribotnik in \"Love Soup\", a woman in a bar in \"Extras\", Natella in \"Bromwell High\" and a character in \"Guess with Jess\".  Including additional voices in \"Perfect Dark Zero\" and \"Dragon Quest VIII\" as well as narrating \"To Leo with Love\".\n\nSara Kestelman: Sara Kestelman (born 12 May 1944) is an English actress.  She is best known for providing the voice of Kreia in \"\", and for her role as Lady Frances Brandon, Lady Jane Grey's mother, in \"Lady Jane\".\n\nRose Hill (actress): Rose Lilian Hill (5 June 1914 – 22 December 2003) was an English actress and operatic soprano, who remains best known for her role as Madame Fanny La Fan in the British television series \"'Allo 'Allo! \".  She was a former member of the Royal Shakespeare Company.\n\nHayley Mills: Hayley Catherine Rose Vivien Mills (born 18 April 1946) is an English actress.  The daughter of Sir John Mills and Mary Hayley Bell, and younger sister of actress Juliet Mills, Mills began her acting career as a child and was hailed as a promising newcomer, winning the BAFTA Award for Most Promising Newcomer for her performance in the British crime drama film \"Tiger Bay\" (1959), the Academy Juvenile Award for Disney's \"Pollyanna\" (1960) and Golden Globe Award for New Star of the Year – Actress in 1961.  During her early career, she appeared in six films for Walt Disney, including her dual role as twins Susan and Sharon in the Disney film \"The Parent Trap\" (1961).  Her performance in \"Whistle Down the Wind\" (a 1961 adaptation of the novel written by her mother) saw Mills nominated for BAFTA Award for Best British Actress.\n\nFootfalls: Footfalls is a play by Samuel Beckett.  It was written in English, between 2 March and December 1975 and was first performed at the Royal Court Theatre as part of the Samuel Beckett Festival, on May 20, 1976 directed by Beckett himself.  Billie Whitelaw, for whom the piece had been written, played May whilst Rose Hill voiced the mother.\n\nJoyce Blair: Joyce Blair (born Joyce Ogus; 4 November 1932 – 19 August 2006) was an English actress and dancer.  She was the younger sister of Lionel Blair, with whom she often performed.  She was the mother of actress Deborah Sheridan-Taylor, who played Saskia Duncan in \"EastEnders\", and of a son, Adam, who is a photographer.\n\nWendy Craig: Anne Gwendolyn \"Wendy\" Craig (born 20 June 1934) is an English actress who is best known for her appearances in the sitcoms \"Not in Front of the Children\", \"Butterflies\", \"...And Mother Makes Three\" and \"...And Mother Makes Five\".  She played the role of Matron in the TV series \"The Royal\" (2003–11).\n\nEileen O'Brien (actress): Eileen O'Brien is an English actress who has played a wide variety of roles in British television over many years.  She appeared in ITV soap opera, \"Emmerdale\" as Beattie Dixon, grandmother of Alex Moss, who turned up at the beginning of 2013 to look for her grandson.  O'Brien previously appeared in the show as teacher, Bridget Burgess in 2006-2007.  Back in 1987-1988, O'Brien had a recurring role in the BBC soap opera, \"EastEnders\"; she played Edie Smith, the mother of Linda Davidson's character, Mary.\n\nJulie Peasgood: Julie May Peasgood (born 28 May 1956 in Cleethorpes, Lincolnshire) is an English actress, television presenter, author and voice over artist known for her distinctive voice.  She was a pupil at Grimsby's Wintringham School.  She is best known for her role as Fran Pearson in the television soap \"Brookside\" (1991–93).  She later played Jo Steadman in \"Emmerdale\" in 1997 and Jacqui Hudson in \"Hollyoaks\" from 2001–02.\n\nSusan Fitzgerald: Susan Mary Theresa Fitzgerald (28 May 1949 – 9 September 2013) was an Irish actress, best known for her work in television and her work in Irish theatre.  She also played the role of May in Samuel Beckett's \"Footfalls\" for the Gate Theatre's \"Beckett on Film\" project.  At her death she was hailed as \"one of Ireland's best known stage actresses\" and \"the pre-eminent stage actress of her generation and beloved of theatre audiences.\"\n\nQuestion: Who was the English actress who played the voice of the mother in Footfalls\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"play_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the play.\"\n    },\n    \"character_role\": {\n      \"type\": \"string\",\n      \"description\": \"The role played by the actress in the play.\"\n    },\n    \"actress_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The full name of the actress.\"\n        },\n        \"nationality\": {\n          \"type\": \"string\",\n          \"description\": \"The nationality of the actress.\"\n        },\n        \"best_known_for\": {\n          \"type\": \"string\",\n          \"description\": \"The role or work the actress is best known for.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"nationality\",\n        \"best_known_for\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"play_name\",\n    \"character_role\",\n    \"actress_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "play_name": {
        "type": "string",
        "description": "The name of the play."
      },
      "character_role": {
        "type": "string",
        "description": "The role played by the actress in the play."
      },
      "actress_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The full name of the actress."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the actress."
          },
          "best_known_for": {
            "type": "string",
            "description": "The role or work the actress is best known for."
          }
        },
        "required": [
          "name",
          "nationality",
          "best_known_for"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "play_name",
      "character_role",
      "actress_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

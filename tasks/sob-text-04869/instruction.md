{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nCanary in a Cat House: Canary in a Cat House is a collection of twelve short stories by American writer Kurt Vonnegut, published in 1961.  Eleven of the twelve appear in the later collection \"Welcome to the Monkey House\", with \"Hal Irwin's Magic Lamp\" being omitted.  In a later collection of short stories, \"Bagombo Snuff Box\", there is a story with that title although it is a different version.\n\nMiss Temptation: \"Miss Temptation\" is a short story written by Kurt Vonnegut, published in \"The Saturday Evening Post\" in 1956.  The story was collected in Vonnegut's famous anthology \"Welcome to the Monkey House\" and was reprinted online by \"The Saturday Evening Post\" in 2011.\n\nRetrospective (Monkey House album): Retrospective is the name of an anthology album by the music group Monkey House, which was released in 2013 on the Green Dolphin Music label.  Monkey House is a rock/pop/jazz group led by Don Breithaupt.  This release has a total of 44 tracks: 38 songs, plus six interviews.  It includes almost every tune from their first two albums, \"Welcome to the Club\" (1992), and \"True Winter\" (1998), and also has four newer songs that were on the 2005 release entitled \"Big Money: Singles Remasters Rarities 1992-2005\".  Additionally, six tunes not previously released are on this anthology album, five of them being instrumentals, as well as the tune \"I'm Not That Guy\" from the \"Headquarters\" (2012 album) sessions, but had not been included on that album.  Special guests include Little Feat drummer Richie Hayward and former Pat Metheny Group member David Blamires.\n\nWho Am I This Time?: \"Who Am I This Time?\"  is a short story written by Kurt Vonnegut, published in the \"Saturday Evening Post\" in 1961.  The story was collected in Vonnegut's famous anthology \"Welcome to the Monkey House\".  It was originally titled \"My Name is Everyone\".\n\nHeadquarters (Monkey House album): Headquarters is the title of a studio album by the music group Monkey House, released in May 2012, on the Alma Records label, which is affiliated with the Universal Music Group.  It was mainly recorded at the Drive Shed in Toronto.  It was produced and arranged by Don Breithaupt, and the engineer was John 'Beetle' Bailey.  Breithaupt is the founder and leader of Monkey House, who have been recording since 1992.  Their previous two albums were \"Welcome to the Club\" (1992), and \"True Winter\" (1998).  In 2005, they released \"Big Money\", a collection of singles, remasters, and rarities.  Stylistically, the \"Headquarters\" album shows it to be influenced by the music of Steely Dan, with arranged horns and background vocals throughout.  Breithaupt says the tunes are \"pop songs with too many chords!\"  Also, some guitar work comes from guest artists Drew Zingg (who is best known for his work with Boz Scaggs and Steely Dan), as well as from Kim Mitchell and Rik Emmett (founder of the band Triumph).  Also making contributions on this album are Steely Dan trumpet player and musical director Michael Leonhart, with Julie Crochetière and David Blamires adding backup vocals.  \"Headquarters\" has generated increasing attention and multi-genre airplay for Monkey House, with a growing international audience.\n\nKurt Vonnegut: Kurt Vonnegut Jr. ( ; November 11, 1922April 11, 2007) was an American writer.  In a career spanning over 50 years, Vonnegut published 14 novels, three short story collections, five plays, and five works of non-fiction.  He is most famous for his darkly satirical, best-selling novel \"Slaughterhouse-Five\" (1969).\n\nDisplaced Person (American Playhouse): Displaced Person is a 1985 Emmy Award-winning episode of American anthology television series \"American Playhouse\", based on a short story by Kurt Vonnegut.  It was directed by Alan Bridges and adapted by Fred Barron from a story in the \"Welcome to the Monkey House\" collection.  The title of the story in that collection was \"D.P.\"\n\nKurt Vonnegut's Monkey House: Kurt Vonnegut's Monkey House is a Canadian television anthology series which aired on the Showtime network from 1991 to 1993.  Author Kurt Vonnegut hosted the series himself, presenting dramatizations of several of his short stories from the collection \"Welcome to the Monkey House\".\n\nReport on the Barnhouse Effect: \"Report on the Barnhouse Effect\" is the first short story written and published by American writer Kurt Vonnegut.  It originally appeared in the February 11, 1950 issue of \"Collier's Weekly\".  In 1952, the story was included in the science fiction anthology \"Tomorrow, the Stars\", edited by Robert A. Heinlein.  It is also part of the collection \"Welcome to the Monkey House\", published in 1968.\n\nTomorrow and Tomorrow and Tomorrow (short story): \"Tomorrow and Tomorrow and Tomorrow\" is a short story by Kurt Vonnegut originally written in 1953.  It was first published in \"Galaxy Science Fiction\" magazine in January 1954, where the story was titled \"The Big Trip Up Yonder\", which is the protagonist's euphemism for dying.  A revised version bearing the title \"Tomorrow and Tomorrow and Tomorrow\" appeared in Vonnegut's collection of short stories, \"Canary in a Cat House\" (1961), and was reprinted in \"Welcome to the Monkey House\" (1968).  The new title comes from the famous line in Shakespeare's play \"Macbeth\" starting \"Tomorrow and tomorrow and tomorrow\".\n\nQuestion: Who was the American writer with the famous anthology called \"Welcome to the Monkey House\"?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"author_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the American writer.\"\n    },\n    \"nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the writer.\"\n    },\n    \"anthology_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the famous anthology.\"\n        },\n        \"publication_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the anthology was published.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"publication_year\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"author_name\",\n    \"nationality\",\n    \"anthology_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "author_name": {
        "type": "string",
        "description": "The full name of the American writer."
      },
      "nationality": {
        "type": "string",
        "description": "The nationality of the writer."
      },
      "anthology_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the famous anthology."
          },
          "publication_year": {
            "type": "integer",
            "description": "The year the anthology was published."
          }
        },
        "required": [
          "title",
          "publication_year"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "author_name",
      "nationality",
      "anthology_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

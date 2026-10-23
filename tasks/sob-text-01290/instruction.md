{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSword and Sorceress series: The \"Sword and Sorceress\" series is a series of fantasy anthologies originally edited by Marion Zimmer Bradley, and originally published by DAW Books.  As she explained in the foreword to the first volume, she created the anthology to redress the lack of strong female protagonists in the subgenre of sword and sorcery.  At the time, most female characters in sword and sorcery were little more than stock damsels in distress, or pawns who were distributed at the conclusion of the story as \"bad-conduct prizes\" (Bradley's term) for the male protagonists.  Many of the early sword-and-sorcery works featured attitudes toward women that Bradley considered appalling.\n\nMarion Zimmer Bradley's Fantasy Magazine: Marion Zimmer Bradley's Fantasy Magazine was a quarterly fantasy magazine founded and initially edited by fantasy and science fiction author Marion Zimmer Bradley.  Fifty issues appeared from summer 1988 through December 2000.  It was published by MZB Enterprises from 1988-1989, Marion Zimmer Bradley Ltd. from 1990-1993, and the Marion Zimmer Bradley Living Trust from 1994-2000, all based in Berkeley, California.  The Trust continued publication for a short time after Bradley's death in 1999; the magazine went out of business at the end of 2000.\n\nThe Heirs of Hammerfell: The Heirs of Hammerfell is a science fantasy novel by American writer Marion Zimmer Bradley, part of her Darkover series.  It was first published by in hardcover by DAW Books in 1989.  The book takes place during the era of Darkover's history known as the Hundred Kingdoms.  This is the last book in the Darkover series written entirely by Bradley without the assistance of a co-author.\n\nDarkover series: The Darkover series is a science fiction-fantasy chronology consisting of several novels and short stories set in the fictional world of Darkover as created by author Marion Zimmer Bradley.  The word \"Darkover\" is a registered trademark owned by the Marion Zimmer Bradley Literary Works Trust.\n\nThe Spell Sword: The Spell Sword is a sword and planet novel by American writer Marion Zimmer Bradley, part of the Darkover series.  The book was co-authored by Paul Edwin Zimmer, Bradley's brother, though he was not credited.  \"The Spell Sword\" was first published in paperback by DAW in 1974 OCLC 156484864  and has been republished several times.\n\nThe Forest House: The Forest House is a fantasy novel by American writers Marion Zimmer Bradley and Diana L. Paxson, though the latter is uncredited by the publisher.  It is a prequel to Bradley's Arthurian novel \"The Mists of Avalon\".\n\nDarkover: Darkover is the focus planet of the Darkover series of science fiction-fantasy novels and short stories by Marion Zimmer Bradley and others published since 1958.  According to the novels, Darkover is the only human-habitable of seven planets orbiting a fictional red giant star called Cottman.  The word \"Darkover\" is a registered trademark owned by the Marion Zimmer Bradley Literary Works Trust.\n\nMarion Zimmer Bradley: Marion Eleanor Zimmer Bradley (June 3, 1930 – September 25, 1999) was an American author of fantasy, historical fantasy, science fiction, and science fantasy novels, and is best known for the Arthurian fiction novel \"The Mists of Avalon\", and the Darkover series.  While some critics have noted a feminist perspective in her writing, her popularity has been posthumously marred by multiple accusations against her of child sexual abuse and rape by two of her children, Mark and Moira Greyland, among many others.  Zimmer Bradley's first child, David R. Bradley, and her brother, Paul Edwin Zimmer, also became published science fiction and fantasy authors.\n\nMarion Zimmer Bradley's Darkover: Marion Zimmer Bradley's Darkover is a collection of science fantasy short stories by American writer Marion Zimmer Bradley.  The stories are set in Bradley's world of Darkover.  The book was first published by DAW Books (No. 929) in October, 1993.\n\nRobin McKinley: Jennifer Carolyn Robin McKinley (born November 16, 1952), known as Robin McKinley, is an American author of fantasy and children's books.  Her 1984 novel \"The Hero and the Crown\" won the Newbery Medal as the year's best new American children's book.\n\nQuestion: Marion Zimmer Bradley and Robin McKinley, are of which nationality?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"authors\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\"\n          },\n          \"nationality\": {\n            \"type\": \"string\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"nationality\"\n        ],\n        \"additionalProperties\": false\n      }\n    },\n    \"common_nationality\": {\n      \"type\": \"string\"\n    },\n    \"number_of_authors\": {\n      \"type\": \"integer\"\n    }\n  },\n  \"required\": [\n    \"authors\",\n    \"common_nationality\",\n    \"number_of_authors\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "authors": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "nationality": {
              "type": "string"
            }
          },
          "required": [
            "name",
            "nationality"
          ],
          "additionalProperties": false
        }
      },
      "common_nationality": {
        "type": "string"
      },
      "number_of_authors": {
        "type": "integer"
      }
    },
    "required": [
      "authors",
      "common_nationality",
      "number_of_authors"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

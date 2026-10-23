{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nLady Colin Campbell: Georgia Arianna, Lady Colin Campbell (\"née\" Ziadie; born 17 August 1949) is a Jamaican-born British writer, socialite, and television and radio personality.  She has published three books about the British Royal Family.  They include biographies of Diana, Princess of Wales, which was on \"The New York Times\" bestseller list in 1992, and Queen Elizabeth The Queen Mother.  She has also written two autobiographies, one exploring her mother.\n\nSoldiers' Pay: Soldiers' Pay is the first novel published by the American author William Faulkner.  It was originally published by Boni & Liveright on February 25, 1926.  It is unclear if Soldiers' Pay is the first novel written by Faulkner.  It is however the first novel published by the author.  Faulkner was working on two manuscripts while finishing Soldiers' Pay.\n\nTyne O'Connell: Tyne O'Connell (full name Clementyne Rose O'Connell) is an English author born in Windsor, who lives and works in Mayfair, London.  Mayfair serves as a backdrop for much of her contemporary women's fiction, including \"Making The A list\" (Headline Review, 1999) and \"Sex With The Ex\" (Red Dress Ink UK, 2004).  She has written for publications such as \"Ms.\", \"Elle UK\" and \"Journal\".  Her short stories appear in \"Girls' Night Out\" and \"Kid's Night In\".  She is a contributor to \"Holiday Goddess\".  O'Connell is The Eccentrics Club's (whose patron is HRH The Prince Philip, Duke of Edinburgh), \"Most Eccentric Thinker of the Year\" 2015.  <br><br>Bloomsbury USA published a compilation of O'Connell's YA fiction 'Royal Match' and 'Royal Mess' in 2012 to coincide with the Royal Wedding.  Soon after O'Connell was diagnosed with a brain tumour and began writing her history of eccentricity as a quintessential aspect of the British and Irish character.  CNN Style in its documentary 'The Adorned' describes O'Connell \"The Mayfair-based author and socialite seems to have been torn straight from the pages of an Evelyn Waugh novel; with her cut-glass accent, perma-fixed tiara and layers of pearls.\n\nArdashir Vakil: Ardashir Vakil is an author whose first novel, \"Beach Boy\", won a Betty Trask Award in 1997 and was shortlisted for the Whitbread First Novel Award.  His second novel, \"One Day\" was shortlisted for the Encore Award.\n\nRichard Marsh (author): Richard Marsh (12 October 1857 – 9 August 1915) was the pseudonym of the English author born Richard Bernard Heldmann.  A best-selling and prolific author of the late 19th century and the Edwardian period, Marsh is best known now for his supernatural thriller novel \"The Beetle\", which was published the same year as Bram Stoker's \"Dracula\" (1897), and was initially even more popular.  \"The Beetle\" remained in print until 1960.  Marsh produced nearly 80 volumes of fiction and numerous short stories, in genres including horror, crime, romance and humour.  Many of these have been republished recently, beginning with \"The Beetle\" in 2004.  Marsh's grandson Robert Aickman was a notable writer of short \"strange stories\".\n\nEmpress of Mijak: Empress of Mijak (known as Empress in North America and the United Kingdom) is the first novel in the \"Godspeaker\" series by Karen Miller.\n\nIn the Woods: In the Woods is a 2007 mystery novel by Tana French about a pair of Irish detectives and their investigation of the murder of a twelve-year-old girl.  The novel won several awards such as the 2008 Edgar Award for Best First Novel by an American Author, the 2008 Barry Award for Best First Novel, the 2008 Macavity Award for Best First Mystery Novel, and the 2008 Anthony Award for Best First Novel.\n\nEmpress Bianca: Empress Bianca, the first novel by Lady Colin Campbell, was initially published in June 2005.  One month later, Arcadia Books, the British publisher, withdrew the book and pulped all unsold copies in reaction to a legal threat initiated on behalf of Lily Safra under her interpretation that the book was a defamatory roman à clef.  After some changes the book was republished in the United States in 2008 by Dynasty Press.\n\nMaurice Leitch: Maurice Leitch (born 5 July 1933) is an author born in Northern Ireland.  Leitch's work includes novels, short stories, dramas, screenplays and radio and television documentaries.  His first novel was \"The Liberty Lad\", published in 1965.  His second novel, \"Poor Lazarus\" was awarded the Guardian Fiction Prize in 1969, and \"Silver's City\" won the Whitbread Prize in 1981.\n\nNew Day (novel): New Day is a 1949 book by Jamaican author V. S. Reid.  It was Reid's first novel.  \"New Day\" deals with the political history of Jamaica as told by a character named Campbell, who is a boy at the time of the Morant Bay Rebellion (in 1865) and an old man during its final chapters.  It may have been the first novel to use Jamaican vernacular as its language of narration.\n\nQuestion: Empress Bianca is the first novel by an author born on which day ?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"novel\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the novel.\"\n        },\n        \"is_first_novel_by_author\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if this novel is the author's first published novel.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"is_first_novel_by_author\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"author\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The full name of the author.\"\n        },\n        \"birth_date\": {\n          \"type\": \"string\",\n          \"description\": \"The birth date of the author in 'DD Month YYYY' format.\"\n        },\n        \"birth_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The birth year of the author.\"\n        },\n        \"origin_countries\": {\n          \"type\": \"array\",\n          \"items\": {\n            \"type\": \"string\"\n          },\n          \"description\": \"Countries associated with the author's origin or nationality.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"birth_date\",\n        \"birth_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"answer_detail\": {\n      \"type\": \"string\",\n      \"description\": \"The specific birth date of the author as requested by the question.\"\n    }\n  },\n  \"required\": [\n    \"novel\",\n    \"author\",\n    \"answer_detail\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "novel": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the novel."
          },
          "is_first_novel_by_author": {
            "type": "boolean",
            "description": "Indicates if this novel is the author's first published novel."
          }
        },
        "required": [
          "title",
          "is_first_novel_by_author"
        ],
        "additionalProperties": false
      },
      "author": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The full name of the author."
          },
          "birth_date": {
            "type": "string",
            "description": "The birth date of the author in 'DD Month YYYY' format."
          },
          "birth_year": {
            "type": "integer",
            "description": "The birth year of the author."
          },
          "origin_countries": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "description": "Countries associated with the author's origin or nationality."
          }
        },
        "required": [
          "name",
          "birth_date",
          "birth_year"
        ],
        "additionalProperties": false
      },
      "answer_detail": {
        "type": "string",
        "description": "The specific birth date of the author as requested by the question."
      }
    },
    "required": [
      "novel",
      "author",
      "answer_detail"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

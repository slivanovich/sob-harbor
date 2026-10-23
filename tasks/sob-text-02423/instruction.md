{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nCauldron (McDevitt novel): Cauldron is a science fiction novel by American author Jack McDevitt.  It is the sixth novel in the Academy series, featuring Priscilla Hutchins.\n\nLord John series: The \"Lord John\" series is a sequence of historical mystery novels and shorter works written by Diana Gabaldon that center on Lord John Grey, a recurring secondary character in the author's \"Outlander\" series.  Secretly homosexual \"in a time when that particular predilection could get one hanged,\" the character has been called \"one of the most complex and interesting\" of the hundreds of characters in Gabaldon's \"Outlander\" novels.  Starting with the 1998 novella \"Lord John and the Hellfire Club\", the \"Lord John\" spin-off series currently consists of five novellas and three novels.\n\nJohn Everson: John Everson (born March 14, 1966) is an American author of contemporary horror, dark fantasy, science fiction and fantasy fiction.  He is the author of eight novels and four short fiction collections, as well as three mini-collections, all focusing on horror and the supernatural.  His novel \"Covenant\", was originally released in a limited edition hardcover by Delirium Books in 2004 and won the Bram Stoker Award for a First Novel the following year from the Horror Writers Association.  His sixth novel, \"NightWhere\", was a finalist for the Bram Stoker Award in 2012.\n\nMelissa de la Cruz: Melissa de la Cruz (born 1971) is a Filipina American author known for her work in young adult fiction.  She has written several series of young adult novels, including the \"Au Pair\" series and the \"Blue Bloods\" series, and a contemporary fiction series following \"The Beauchamp Family\", as well as a number of stand-alone novels.\n\nGame of Thrones (season 5): The fifth season of the fantasy drama television series \"Game of Thrones\" premiered on HBO on April 12, and concluded on June 14, 2015.  It was broadcast on Sunday at 9:00 pm in the United States, consisting of 10 episodes, each running approximately 50–60 minutes.  The season primarily adapts material from \"A Feast for Crows\" and \"A Dance with Dragons\", the fourth and fifth novels in George R. R. Martin's \"A Song of Ice and Fire\" series, though it also uses elements from the third novel, \"A Storm of Swords\", as well as the upcoming sixth novel \"The Winds of Winter\".  It also contains original content not found in Martin's novels.  The series is adapted for television by David Benioff and D. B. Weiss.\n\nDiana Gabaldon: Diana J. Gabaldon (born January 11, 1952) is an American author, known for the \"Outlander\" series of novels.  Her books merge multiple genres, featuring elements of historical fiction, romance, mystery, adventure and science fiction/fantasy.  A television adaptation of the novels called \"Outlander\" premiered on Starz in 2014.\n\nA Breath of Snow and Ashes: A Breath of Snow and Ashes is the sixth book in the \"Outlander\" series of novels by Diana Gabaldon.  Centered on time travelling 20th century doctor Claire Randall and her 18th century Scottish Highlander warrior husband Jamie Fraser, the books contain elements of historical fiction, romance, adventure and science fiction/fantasy.\n\nLord John Grey (character): Lord John William Grey is a fictional character created by Diana Gabaldon.  He is a recurring secondary character in Gabaldon's \"Outlander\" series of novels, and the main character of the \"Lord John\" series of historical mystery novels and novellas.  Secretly homosexual \"in a time when that particular predilection could get one hanged\", the character has been called \"one of the most complex and interesting\" of the hundreds of characters in Gabaldon's \"Outlander\" novels.\n\nAngel Mountain Saga: The Angel Mountain Saga of eight novels was written by Welsh author Brian John, and was first published at the rate of one volume per year in 2001-2005, with later volumes in 2007, 2009 and 2012.  The publisher is Greencroft Books, based in Newport, Pembrokeshire.  The novels tell of the life and times of Mistress Martha Morgan, a feisty heroine who starts the series in 1796 as a pregnant and suicidal eighteen-year-old and finishes it by going to her grave in 1855.  In the sixth novel she is resurrected (or is she?)  and has further adventures in Merthyr Tydfil and further afield.  Volumes seven and eight are placed into gaps in the narrative related in Volume Three.  The eight novels are \"On Angel Mountain\" (2001), \"House of Angels\" (2002), \"Dark Angel\" (2003), \"Rebecca and the Angels\" (2004), \"Flying with Angels\" (2005), \"Guardian Angel\" (2007), \"Sacrifice\" (2009) and \"Conspiracy of Angels\" (2012).\n\nJamie Fraser (character): James \"Jamie\" Fraser is a fictional character in the \"Outlander\" series of multi-genre novels by American author Diana Gabaldon, and its television adaptation.  In the series, married World War II nurse Claire Randall is visiting Scotland when she finds herself transported from 1945 back to 1743.  There she finds adventure, war and romance with the dashing Highland warrior Jamie Fraser.  Jamie also appears in two novels in the \"Lord John\" series of historical mysteries, and in the 2013 novella \"Virgins\".\n\nQuestion: What American author known for the Outlander series of novels, created her sixth novel, from the same series, called A Breath of Snow?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"author_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the author.\"\n    },\n    \"nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the author.\"\n    },\n    \"series_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the novel series.\"\n    },\n    \"novel_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the specific novel mentioned.\"\n    },\n    \"novel_number_in_series\": {\n      \"type\": \"integer\",\n      \"description\": \"The sequential number of the novel within its series.\"\n    }\n  },\n  \"required\": [\n    \"author_name\",\n    \"nationality\",\n    \"series_name\",\n    \"novel_title\",\n    \"novel_number_in_series\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "author_name": {
        "type": "string",
        "description": "The name of the author."
      },
      "nationality": {
        "type": "string",
        "description": "The nationality of the author."
      },
      "series_name": {
        "type": "string",
        "description": "The name of the novel series."
      },
      "novel_title": {
        "type": "string",
        "description": "The title of the specific novel mentioned."
      },
      "novel_number_in_series": {
        "type": "integer",
        "description": "The sequential number of the novel within its series."
      }
    },
    "required": [
      "author_name",
      "nationality",
      "series_name",
      "novel_title",
      "novel_number_in_series"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

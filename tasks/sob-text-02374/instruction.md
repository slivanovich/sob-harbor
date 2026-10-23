{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMark Salzman: Mark Joseph Salzman (born December 3, 1959 in Greenwich, Connecticut) is an American writer.  Salzman is best known for his 1986 memoir \"Iron & Silk\", which describes his experiences living in China as an English teacher in the early 1980s.\n\nThe Last Defender of Camelot (short story): \"The Last Defender of Camelot\" is a fantasy short story by American writer Roger Zelazny, first published in the Summer 1979 issue of \"Asimov's SF Adventure Magazine\".  It was subsequently published as a chapbook by Underwood/Miller for the May 23, 1980 V-Con 8 where Zelazny was guest of honor.  The story was also the basis of an 1986 episode of the television series \"The Twilight Zone\".\n\nManna from Heaven: Manna from Heaven is a collection of fantasy short stories by American Roger Zelazny.  It was published in 2003 by Zelazny's estate eight years after Zelazny's death.\n\nIron &amp; Silk (1990 film): Iron & Silk is a 1990 movie based on the eponymous book by American writer Mark Salzman.  It details his journey to China after college to study Chinese wu shu, better known in the west as kung fu, and to teach English.  Though not trained as an actor, Salzman starred as himself, as did Pan Qingfu, who claimed no one else could portray him on film.  Salzman's experiences occurred in Changsha, Hunan, though the film was shot in Hangzhou, Zhejiang.  The film was directed by Shirley Sun, and was the editorial debut for Geraldine Peroni.\n\nToday We Choose Faces: Today We Choose Faces is a 1973 science fiction novel by American writer Roger Zelazny.  As originally constructed, Part 1 was an extensive flashback which followed Part 2, but the order of the sections was changed at the request of editor David Hartwell, who felt that the novel worked better in chronological order.  Zelazny later wrote, “I was younger then & more in need of the money at the time & couldn’t afford to argue [with] him about it.  I still prefer it the way I wrote it.”\n\nWay Up High: Way Up High is a children's book by American writer Roger Zelazny.  It is one of two stories he wrote for children, the other being \"Here There Be Dragons\", and one of three books without heroic protagonists.  One thousand copies of each of the two books signed by Zelazny were published in 1992 with illustrations by Vaughn Bodē.\n\nRoger Zelazny: Roger Joseph Zelazny (May 13, 1937 – June 14, 1995) was an American poet and writer of fantasy and science fiction short stories and novels, best known for \"The Chronicles of Amber\".  He won the Nebula award three times (out of 14 nominations) and the Hugo award six times (also out of 14 nominations), including two Hugos for novels: the serialized novel \"...And Call Me Conrad\" (1965), subsequently published under the title \"This Immortal\" (1966) and then the novel \"Lord of Light\" (1967).\n\nUnicorn Variations: Unicorn Variations is a collection of stories and essays by American author Roger Zelazny, published in 1983.  The title story, \"Unicorn Variation\", was written as a result of Zelazny having been asked to contribute to two different upcoming anthologies — one collecting stories set in bars, and one collecting stories about unicorns.  When Zelazny mentioned these requests to his close friend George R. R. Martin, Martin told Zelazny of a third upcoming anthology — one which would collect stories about chess — and jokingly suggested that Zelazny write a story about playing chess against a unicorn in a bar, so that he could sell the story three times.  Zelazny did just that and then went on to win a Hugo Award for the story.\n\nBridge of Ashes: Bridge of Ashes is an experimental science fiction novel by author Roger Zelazny.  The paperback edition was published in 1976 and the hardcover in 1979.  Zelazny describes the book as one of five books from which he learned things “that have borne me through thirty or so others.”  He states that he “felt that if I could pull it off I could achieve some powerful effects.  What I learned from this book is something of the limits of puzzlement in that no man’s land between suspense and the weakening of communication.”\n\nDilvish, the Damned: Dilvish, the Damned is a collection of fantasy stories by American writer Roger Zelazny, first published in 1982.  Its contents were originally published as a series of separate short stories in various fantasy magazines. Prior to publication, Zelazny's working title for the book was \"Nine Black Doves\".  The working title was later re-used for the fifth volume of \"The Collected Short Stories of Roger Zelazny\" collection, as a tribute to Dilvish.  The storyline begun in this collection was resolved in the novel \"The Changing Land\", which was published before the other \"Dilvish\" stories appeared in book form.\n\nQuestion: Roger Zelazny and Mark Salzman, have which mutual occupation?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_1_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the first person mentioned.\"\n    },\n    \"person_1_occupations\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of occupations for the first person.\"\n    },\n    \"person_2_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the second person mentioned.\"\n    },\n    \"person_2_occupations\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of occupations for the second person.\"\n    },\n    \"mutual_occupation\": {\n      \"type\": \"string\",\n      \"description\": \"The occupation shared by both individuals.\"\n    }\n  },\n  \"required\": [\n    \"person_1_name\",\n    \"person_1_occupations\",\n    \"person_2_name\",\n    \"person_2_occupations\",\n    \"mutual_occupation\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_1_name": {
        "type": "string",
        "description": "The name of the first person mentioned."
      },
      "person_1_occupations": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of occupations for the first person."
      },
      "person_2_name": {
        "type": "string",
        "description": "The name of the second person mentioned."
      },
      "person_2_occupations": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of occupations for the second person."
      },
      "mutual_occupation": {
        "type": "string",
        "description": "The occupation shared by both individuals."
      }
    },
    "required": [
      "person_1_name",
      "person_1_occupations",
      "person_2_name",
      "person_2_occupations",
      "mutual_occupation"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

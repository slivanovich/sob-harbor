{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nLeave a Whisper: Leave a Whisper is the debut studio album by American rock band Shinedown.  The album was released on May 27, 2003, faring well due to the success of the singles \"Fly from the Inside\" and \"45\".  Recording took place at Henson Recording Studios and The Blue Room, both in Los Angeles, California.  \"Leave a Whisper\" paved the way for Shinedown's successful second album, \"Us and Them\", and was re-released on June 15, 2004, to incorporate a cover version of Lynyrd Skynyrd's \"Simple Man\".  The album's singles also fared well, \"Fly from the Inside\" reaching No. 5, \"45\" reaching No. 3, \"Simple Man\" reaching No. 5, and \"Burning Bright\" reaching No. 2 on the US Mainstream Rock list.  \"Leave a Whisper\" is Shinedown's second best-selling album.  On August 17, 2004, the album was certified gold for 500,000 copies sold, and by October 21, 2005, the album had sold 1 million copies in the US, and was certified platinum by the RIAA.\n\nPeter Bennett-Jones: Peter Bennett-Jones CBE is a British TV producer and agent.  He is perhaps best known as the former owner of TV production company Tiger Aspect where he was the executive producer of a number of British shows including \"Vicar of Dibley\" and \"Mr. Bean\".  He has also represented actors such as Rowan Atkinson, Lenny Henry, Barry Humphries, Armando Iannucci and Eddie Izzard through his company PBJ Management.  He is Chairman of Burning Bright Prods and Douglas Road Prods.\n\nFearful Symmetry: Fearful Symmetry is a phrase from William Blake's poem \"The Tyger\" (\"Tyger, tyger, burning bright / In the forests of the night, / What immortal hand or eye / Could frame thy fearful symmetry?\") .  It has been used as the name of a number of other works:\n\nMoreau series: The Moreau series of books are four biopunk science fiction novels by S. Andrew Swann, originally published by DAW Books from 1993 to 1999.  Two of the titles are based on lines from the poem \"The Tyger\" by William Blake.\n\nThe Burning Bright: The Burning Bright is a studio album by singer-songwriter Royal Wood, released by Songs of MapleMusic Publishing.  The album was released on March 18, 2014.  The lead single, \"Forever and Ever\", was a top 40 hit in Canada and was the No. 1 most added song on Hot AC Radio.\n\nThe Tyger: \"The Tyger\" is a poem by the English poet William Blake published in 1794 as part of the \"Songs of Experience\" collection.  Literary critic Alfred Kazin calls it \"the most famous of his poems\", and \"The Cambridge Companion to William Blake\" says it is \"the most anthologized poem in English\".  It is one of Blake's most reinterpreted and arranged works.\n\nBurning Bright (film): Burning Bright is a 2010 horror-thriller directed by Carlos Brooks and starring Briana Evigan, Garret Dillahunt, Meat Loaf, and Charlie Tahan.  The film is distributed by Lionsgate.\n\nAlmost Royal: Almost Royal is a faux-reality television series on the BBC America network.  It is their first original comedy series.  It follows the lives of two clueless British aristocrats—Georgie and Poppy Carlton—visiting the United States for the first time.  The series stars Ed Gamble and Amy Hoggart as Georgie and Poppy, respectively.  It is produced by Burning Bright Productions and premiered on June 21, 2014.  Although Georgie and Poppy are both portrayed by actors, the Americans with whom they interact are not aware of this.  On December 4, 2014, the show was renewed for an eight-episode second season, which started airing on January 18, 2016.\n\nQuasar, Quasar, Burning Bright: Quasar, Quasar, Burning Bright is a collection of seventeen scientific essays by Isaac Asimov.  It was the thirteenth of a series of books collecting essays from \"The Magazine of Fantasy and Science Fiction\".  These essays were first published between May 1976 and September 1977.  It was first published by Doubleday & Company in 1978.  Its title is derived from the first line of William Blake's 1794 poem \"The Tyger\".\n\nMarty Burns: Marty Burns, former child-star, general wise-ass and sometimes detective, is the fictional creation of Jay Russell.  Marty made his debut in the novel \"Celestial Dogs\" (1996), working as yet another low-rent, Los Angeles detective.  The novel is a mix of hardboiled detective and supernatural horror, laced with heavy doses of humor and Hollywood in-jokes.  Marty has appeared in two subsequent novels - \"Burning Bright\" (1997) and \"Greed & Stuff\" (2001) - as well as a series of short stories .  His most recent literary appearance was in the novella \"Apocalypse Now, Voyager\" (2005).\n\nQuestion: When was the poem with the lines Tyger, tyger burning bright published?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"poem_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the poem.\"\n    },\n    \"author\": {\n      \"type\": \"string\",\n      \"description\": \"The author of the poem.\"\n    },\n    \"publication_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the poem was published.\"\n    },\n    \"collection\": {\n      \"type\": \"string\",\n      \"description\": \"The collection the poem was part of.\"\n    }\n  },\n  \"required\": [\n    \"poem_title\",\n    \"author\",\n    \"publication_year\",\n    \"collection\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "poem_title": {
        "type": "string",
        "description": "The title of the poem."
      },
      "author": {
        "type": "string",
        "description": "The author of the poem."
      },
      "publication_year": {
        "type": "integer",
        "description": "The year the poem was published."
      },
      "collection": {
        "type": "string",
        "description": "The collection the poem was part of."
      }
    },
    "required": [
      "poem_title",
      "author",
      "publication_year",
      "collection"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

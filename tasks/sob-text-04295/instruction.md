Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Gladiatress: Gladiatress is a 2004 British comedy film, starring Sally Phillips, Fiona Allen and Doon Mackichan.  It is partly a spoof of 2000's "Gladiator".

The Decoy Bride: The Decoy Bride is a 2011 British romantic comedy film written by comedian Sally Phillips and Neil Jaworski, and starring David Tennant, Alice Eve and Kelly Macdonald and set on the fictional island of Hegg, supposedly located in the Outer Hebrides of Scotland.  The film was made by Ecosse Films.

Rescue Me (UK TV series): Rescue Me is a British romantic comedy television series produced by Tiger Aspect Productions and broadcast on BBC One in 2002.  It was created, and principally written, by David Nicholls and stars Sally Phillips as Katie Nash, a woman who is recovering from a divorce while at the same time writing relationship features for "Eden", the women's magazine she works on.  The series was filmed from November to December 2001.  It ran for six episodes, averaging 3.4 million viewers and a 15% audience share in its Sunday night timeslot.  The low ratings meant it was not recommissioned for a second series, leaving an unresolved cliffhanger.  Nicholls had written four episodes of the unmade second series before discovering "Rescue Me" had been cancelled.  As a result, he took a break from screenwriting to concentrate on his debut novel "Starter for Ten".  A cover version of "Rescue Me", performed by Oliver Darley, is the series theme tune.

The Rizen: The Rizen is an upcoming horror film written by Matt Mitchell and produced by Clare Pearce for Lost Eye Films, directed by Matt Mitchell for Lost Eye Films and starring Laura Swift, Sally Phillips, Tom Goodman-Hill, Julian Rhind-Tutt and Bruce Payne.  The film was cast and produced by Clare Pearce and for a UK independent film the cast is full of well known cameos, this is also regarded as a launch pad for the acting career of former Steps man Lee Latchford-Evans.

List of Miranda episodes: "Miranda" is a BBC television series co-written by and starring comedian Miranda Hart.  It first aired on BBC Two on 9 November 2009 and has since moved to BBC One.  The situation comedy also features Sarah Hadland, Tom Ellis, Patricia Hodge and Sally Phillips.  The series is based on Hart's semi-autobiographical writing and followed a television pilot and the BBC Radio 2 comedy "Miranda Hart's Joke Shop".  This was a very popular TV show watched by millions.

Sally Phillips: Sally Elizabeth Phillips (born 10 May 1970) is an English actress, television presenter and comedian.  She co-created and was one of the writers of sketch comedy show "Smack the Pony".  She is also known for her main role in "Miranda" as Tilly, "Parents" as Jenny Pope and "Set the Thames on Fire" as Colette in 2015.  Phillips also co-starred in "Pride and Prejudice and Zombies", as Mrs Bennet, and reprised her role as Sharon in the 2016 film "Bridget Jones's Baby", following "Bridget Jones's Diary" and "".

Set the Thames on Fire: Set the Thames on Fire is a 2016 British science fiction fantasy comedy-drama film directed by Ben Charles Edwards in his directorial debut.  Based on characters created by Edwards and Al Joshua.  The film stars Michael Winder and Max Bennett, alongside an ensemble cast featuring Noel Fielding, Sadie Frost, Sally Phillips, David Hoyle, and Lily Loveless.

Smack the Pony: Smack the Pony is a British sketch comedy show that ran from 1999 until 2003 on Channel 4.  The main performers on the show were Fiona Allen, Doon Mackichan and Sally Phillips.  There were also regular appearances from Sarah Alexander, Darren Boyd and Cavan Clerkin.  The show's popular theme tune was Dusty Springfield's song "In the Middle of Nowhere", sung by Jackie Clune.  As well as the three principal cast members, the show was written by a large number of writers, the core of which went on to write "Green Wing" and "Campus".  In Germany, the first transmission of the show aired on ProSieben, where the theme tune was changed to Texas' 2001 version of "I Don't Want a Lover", and featured a different title sequence.

Comedy horror: Comedy horror is a literary and film genre that combines elements of comedy and horror fiction.  Comedy horror has been described as able to be categorized under three types: "black comedy, parody and spoof."  The genre almost inevitably crosses over with the black comedy genre.  Comedy horror will often use satire on horror clichés as its main source of humour or take a story in a different perspective, such as "The Cabin in the Woods" and "Drag Me to Hell".

Pride and Prejudice and Zombies (film): Pride and Prejudice and Zombies (stylised as Pride + Prejudice + Zombies) is a 2016 British-American historical comedy horror film based on Seth Grahame-Smith's 2009 novel, "Pride and Prejudice and Zombies", which parodies the 1813 novel "Pride and Prejudice" by Jane Austen.  The film is directed by Burr Steers, who wrote the adapted screenplay, and stars Lily James, Sam Riley, Jack Huston, Bella Heathcote, Douglas Booth, Matt Smith, Charles Dance, and Lena Headey.

Question: Sally Phillips co-starred in the British-American historical comedy horror film based on the novel by whom?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film Sally Phillips co-starred in."
    },
    "film_genre": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The genres of the film."
    },
    "sally_phillips_role": {
      "type": "string",
      "description": "The role Sally Phillips played in the film."
    },
    "source_novel_author": {
      "type": "string",
      "description": "The author of the novel the film is based on."
    },
    "source_novel_publication_year": {
      "type": "integer",
      "description": "The publication year of the source novel."
    }
  },
  "required": [
    "film_title",
    "film_genre",
    "sally_phillips_role",
    "source_novel_author",
    "source_novel_publication_year"
  ],
  "additionalProperties": false
}

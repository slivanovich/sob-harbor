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
Alex Delaware: Alex Delaware is a literary character created by Jonathan Kellerman.  The Alex Delaware detective series begins with "When the Bough Breaks", published in 1985.  Delaware appears in 32 of Kellerman's popular murder mysteries.  Kellerman sets the series in Los Angeles.  Delaware is a forensic psychologist; although Kellerman writes a back story in which Delaware practiced as a child psychologist.

P. G. Wodehouse: Sir Pelham Grenville Wodehouse {'1': ", '2': ", '3': ", '4': "} ( ; 15 October 188114 February 1975) was an English author and one of the most widely read humorists of the 20th century.  Born in Guildford, the son of a British magistrate based in Hong Kong, Wodehouse spent happy teenage years at Dulwich College, to which he remained devoted all his life.  After leaving school he was employed by a bank but disliked the work and turned to writing in his spare time.  His early novels were mostly school stories, but he later switched to comic fiction, creating several regular characters who became familiar to the public over the years.  They include the jolly gentleman of leisure Bertie Wooster and his sagacious valet, Jeeves; the immaculate and loquacious Psmith; Lord Emsworth and the Blandings Castle set; the Oldest Member, with stories about golf; and Mr Mulliner, with tall tales on subjects ranging from bibulous bishops to megalomaniac movie moguls.

Survival of the Fittest (novel): Survival of the Fittest is the thirteenth novel by Jonathan Kellerman and is told through the first person point of view of Kellerman's main character, Dr. Alex Delaware.  LAPD Detective Milo Sturgis has asked Alex to help him with another whodunit.  It reached number two in the New York Times Best Seller list for paperbacks.

Therapy (Kellerman novel): Therapy is a mystery novel by American author Jonathan Kellerman

When the Bough Breaks (1986 film): When the Bough Breaks is a 1986 television film directed by Waris Hussein and starring Ted Danson.  The screenplay by Phil Penningroth was adapted from a 1985 novel by Jonathan Kellerman, also titled "When the Bough Breaks".  Danson, who also co-produced, plays the crime-solving forensic psychologist Alex Delaware, a character who appears in a series of novels by Kellerman.

Obsession (novel): Obsession is a mystery novel by American author Jonathan Kellerman.  It is the 21st novel in the Alex Delaware series.

Rage (Kellerman novel): Rage is a mystery novel by American author Jonathan Kellerman

Jesse Kellerman: Jesse Oren Kellerman (born September 1, 1978) is an American novelist and playwright.  He has published the novels: "Sunstroke" (2006), "Trouble" (2007), "The Genius" (2008), "The Executor" (2010), "I'll Catch You" (2012), and with his father, Jonathan Kellerman, "The Golem of Hollywood" (2014).  For his play, "Things Beyond Our Control" (2004) he was honored with a Princess Grace Award, which recognizes emerging talent in theater, dance, and film in the U.S.

Jonathan Kellerman: Jonathan Kellerman (born August 9, 1949) is an American psychologist, and Edgar and Anthony Award-winning author of numerous bestselling suspense novels.

Blood Test (novel): Blood Test is the second novel by Jonathan Kellerman, published in 1986.  It is told from the first-person point of view of Dr. Alex Delaware, a child psychologist who is Kellerman's main character in the majority of his novels.  The novel also includes Delaware's best friend, LAPD Detective, Milo Sturgis.

Question: Who is an American psychologist, Jonathan Kellerman or P. G. Wodehouse?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person identified as an American psychologist."
    },
    "is_american": {
      "type": "boolean",
      "description": "True if the person is American."
    },
    "is_psychologist": {
      "type": "boolean",
      "description": "True if the person is a psychologist."
    },
    "birth_date": {
      "type": "string",
      "description": "The birth date of the identified person."
    },
    "other_notable_roles": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Other significant roles or professions of the identified person."
    }
  },
  "required": [
    "person_name",
    "is_american",
    "is_psychologist",
    "birth_date",
    "other_notable_roles"
  ],
  "additionalProperties": false
}

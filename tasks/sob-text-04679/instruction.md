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
Murray Valeriano: Murray Valeriano is an American comedian, producer, writer and radio host.  Valeriano has written for The Tonight Show Starring Jimmy Fallon, The Tonight Show with Jay Leno, Bill Engvall's "Here's Your Sign Awards" and Ridiculousness.  He co-hosted the ""Off the Cuff with Bill Engvall"" radio show on Sirius/XM and currently hosts and produces the ""Roadstories"" podcast.

Here's Your Christmas Album: Here's Your Christmas Album is a 1999 comedy album by comedian Bill Engvall.  It contains original Christmas songs, some with vocals from Engvall and others by studio singers.

The Bill Engvall Show: The Bill Engvall Show is a sitcom which ran on TBS from July 17, 2007 to September 5, 2009.  The series starred comedian Bill Engvall and was written and created by Engvall and Michael Leeson.  The series was canceled on September 25, 2009.

Christopher Vane (screenwriter): Christopher Vane is an American television producer and television writer.  His credits include "Thundarr the Barbarian", "The Love Boat", "Wings", "Suddenly Susan", "All About the Andersons" and "The Bill Engvall Show".  He was a co-executive producer and writer on "Good Luck Charlie" from 2010-2015.  He was nominated for a Primetime Emmy Award for his work on "Good Luck Charlie" as a part of the producing team.  He is the creator of "Impastor" comedy series, recently picked up for a second season by TV Land.

Skyler Gisondo: Skyler Gisondo (born July 22, 1996) is an American actor and voice actor known for his roles as Bryan Pearson on "The Bill Engvall Show", Nick Daley in "" and James Griswold in "Vacation".  Since March 2017, he has starred as Eric in Netflix's "Santa Clarita Diet", and as Jeremy "Deegs" Deegenstein in "".

Heide Perlman: Heide Paula Perlman (born September 22, 1951 in Brooklyn, New York) is best known for her work as a television script writer.  Perlman began work as a writer on the sitcom "Cheers" from 1982 through 1986; since then she has worked as a writer, producer and/or story editor on "The Tracey Ullman Show", "Frasier", "The George Carlin Show", "Stacked", "The Bill Engvall Show" and others.  She has won two Primetime Emmy Awards and has been nominated for eight others.

For Heaven's Sake (2008 film): For Heaven's Sake is a comedy written by former Emmy Award winner, Ann Marcus.  The film was directed and produced by Nat Christian.  It stars Florence Henderson, Allison Lange, David Paetkau, Yaani King, Kathryn Gordon, Stephanie Patton, Joseph Campanella and Skyler Gisondo.

Delta Farce: Delta Farce is a 2007 American spoof/comedy released by Lions Gate Entertainment on May 11, 2007.  It is directed by C. B. Harding and stars Bill Engvall, Larry the Cable Guy, DJ Qualls and Danny Trejo.  It is the first film after the Blue Collar Comedy Tour concert films to star both Engvall and Larry the Cable Guy.  The title is a play on the Delta Force, one of the United States Army's elite special operations units alongside the Army Rangers and the Green Berets.

Here's Your Sign Award: Bill Engvall's "Here's Your Sign" Awards is a television program that aired on CMT.  It is hosted by Bill Engvall.

Here's Your Sign: Here's Your Sign is the debut comedy album of Bill Engvall.  It was recorded at Mark Ridley's Comedy Castle in Royal Oak, Michigan.  Following years of success doing different comedic acts, Engvall released a CD of his material, including his most famous piece (after which his debut album was named).  After peaking within the top-5 on both the Heatseekers and Hot Country Albums charts, as well as the top-50 on the "Billboard" 200, Engvall saw his career take off as he remains one of the most popular comedians of the past decade.

Question: For Heaven's Sake starred the actor who had what role on The Bill Engvall Show?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the actor who starred in 'For Heaven's Sake' and also had a role on 'The Bill Engvall Show'."
    },
    "film_starred_in": {
      "type": "string",
      "description": "The name of the film the actor starred in."
    },
    "tv_show_appeared_in": {
      "type": "string",
      "description": "The name of the TV show the actor appeared in."
    },
    "role_on_tv_show": {
      "type": "string",
      "description": "The specific role the actor played on 'The Bill Engvall Show'."
    }
  },
  "required": [
    "actor_name",
    "film_starred_in",
    "tv_show_appeared_in",
    "role_on_tv_show"
  ],
  "additionalProperties": false
}

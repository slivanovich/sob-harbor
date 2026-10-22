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
Anna O'Byrne: Anna O'Byrne is an Australian actress and soprano singer best known for her portrayal of Christine Daaé in Andrew Lloyd Webber's "The Phantom of the Opera" and the original Australian production of Lloyd Webber's sequel, "Love Never Dies", for which she was nominated for a Green Room Award.  O'Byrne has also portrayed Maria in "West Side Story", as well as Sister Sarah Brown in "Guys and Dolls".  From 2016, O'Byrne has played Eliza Doolittle in the Julie Andrews directed production of "My Fair Lady" for Opera Australia at the Sydney Opera House, touring in 2017 to Brisbane, Melbourne and back to Sydney.  She is currently based in London and performs internationally.  Her performance career includes opera, theatre, concert, and film.

Sierra Boggess: Sierra Marjory Boggess (born May 20, 1982) is an American theater actress and singer.  She is best known for originating the role of Ariel in "The Little Mermaid" on Broadway and for her multiple appearances as Christine Daaé in "The Phantom of the Opera."  Sierra has been involved in several productions of "The Phantom of the Opera" beginning with the Las Vegas production in 2006.  In 2010 she was cast to reimagine the role of Christine Daaé in Phantom's sequel "Love Never Dies".

Anthony Warlow: Anthony Thorne Warlow {'1': ", '2': ", '3': ", '4': "} (born 18 November 1961 in Wollongong, New South Wales, Australia) is an Australian opera and musical theatre performer, noted for his character acting and considerable vocal range.  He is a classically trained lyric baritone.

Suzanne Legrand: Suzanne Legrand is a French actress, musical theater performer and writer.  Her career started on French TV with the series by in which she played the part of the youngest daughter.  Since then she has played in many television series, movies, theater plays and musicals, in France and in the US.  She has received several awards in international film festivals for her performance in La pisseuse ("Desperate") which she also wrote and directed with Frederic Benzaquen.

Baritone: A baritone is a type of classical male singing voice whose vocal range lies between the bass and the tenor voice types.  It is the most common male voice.  Originally from the Greek βαρύτονος ("barýtonos") , meaning "deep (or heavy) sounding", music for this voice is typically written in the range from the second F below middle C to the F above middle C (i.e. F–F) in choral music, and from the second A below middle C to the A above middle C (A to A) in operatic music, but can be extended at either end.  The baritone voice type is generally divided into the baryton-Martin baritone (light baritone), lyric baritone, "Kavalierbariton", Verdi baritone, dramatic baritone, "baryton-noble" baritone, and the bass-baritone.

Marina Prior: Marina Prior (born 18 October 1963) is an Australian soprano and actress with a career mainly in musical theatre.  From 1990 to 1993, she starred as the original Christine Daaé in the Australian premiere of "The Phantom of the Opera", opposite Anthony Warlow and later Rob Guest.

Kristie Reeves: Kristie Reeves (née Kerstin Weingartner) is a German actress, musical theater performer and producer.  She started her performance career as a dancer in Germany at the age of seven.  By the time she was a teenager she was touring Germany with her dance company "JDC" and after on made her switch to musical theater.  Her first acting role was in the feature film "September Song" which premiered at the Munich Film Festival in 2001.  She has danced with Jennifer Lopez and her choreographies have won her numerous awards.

Marina Prior Live: Marina Prior Live is the first live album by Australian singer Marina Prior. The album was previously only available via her "Songbird (Boxset)", but released individually on CD or music download in December 2014.

The Essential Marina Prior: "The Essential Marina Prior" is a greatest hits album by Australian singer Marina Prior.

Dennis McNeil: Dennis McNeil, (born July 30, 1960, Los Angeles, California) is an American operatic tenor, musical theater performer, and a world renowned concert singer.  He was educated at Miraleste Intermediate School, Loyola High School (1978), the Institute for the American Musical, the Merola Opera Program of San Francisco Opera, and UC-Davis (1983).

Question: When was the Australian opera and musical theater performer born who is a classically trained lyric baritone and opposite to whom Marina Prior starred as the original Christine Daaé?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "performer_name": {
      "type": "string",
      "description": "The name of the Australian opera and musical theater performer."
    },
    "birth_date": {
      "type": "string",
      "description": "The birth date of the performer."
    },
    "nationality": {
      "type": "string",
      "description": "The nationality of the performer."
    },
    "vocal_type": {
      "type": "string",
      "description": "The vocal type of the performer."
    },
    "role_marina_prior_played_opposite": {
      "type": "string",
      "description": "The role Marina Prior played opposite this performer."
    }
  },
  "required": [
    "performer_name",
    "birth_date",
    "nationality",
    "vocal_type",
    "role_marina_prior_played_opposite"
  ],
  "additionalProperties": false
}

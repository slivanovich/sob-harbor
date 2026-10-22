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
Eva Simatou: Eva Simatou is a Greek actress.  She is a first class graduate of the Advanced Drama School Theatro Technis Karolos Koun (Athens Art Theatre).  She has also studied in London at City University and holds a BSc in Sociology and Media Studies and an MA in Arts Management & Criticism.  She was accepted by the Royal Academy of Dramatic Art (RADA) and has successfully completed the Contemporary Drama programme.

Antonia Kinlay: She is a graduate of the Royal Academy of Dramatic Art In the West End, Kinlay has played Melody in Michael Longhurst's production of "Bad Jews" at the Theatre Royal Haymarket and Penny in "Three Lions" at the St James Theatre.  In 2016 she appeared in "The Suicide" at the National Theatre and played the title role in "Lady Anna: All at Sea" at the Park Theatre

Estelle Kohler: Estelle Kohler (born 28 March 1940) is a British theatre and television actress.  Born in South Africa, Kohler made a name for herself as a Shakespearean actor in England.  She is a graduate of Royal Academy of Dramatic Art, of which she is an Associate Member, and was nominated a Laurence Olivier Award in 2000 for her performance as Paulina in the Barbican Centre's production of "The Winter's Tale" (1999 season).  She is also remembered for her performance as Hilary Nash (later Main) in the TV series "The Main Chance", opposite John Stride.  Her voice is featured in several audio books by Naxos Audiobooks.

Royal Academy of Dramatic Art: The Royal Academy of Dramatic Art (RADA) is a drama school in London, England that provides training for film, television and theatre.  It is one of the oldest and most prestigious drama schools in the United Kingdom, founded in 1904 by Herbert Beerbohm Tree.

Katherine Kelly (actress): Katherine Kelly (born 19 November 1979) is an English actress.  A 2001 graduate of the Royal Academy of Dramatic Art, she played Becky McDonald in the ITV soap opera "Coronation Street" from 2006 to 2012, for which she won Best Actress at the 2009 British Soap Awards and Best Serial Drama Performance at the 2012 National Television Awards.  Since 2013, she has starred as Mae, Lady Loxley in the ITV drama series "Mr Selfridge".

Hugh Sinclair (actor): Hugh Sinclair (19 May 1903 – 29 December 1962) was a British actor born in London, England, the son of a clergyman.  He was educated at Charterhouse School and a graduate of the Royal Academy of Dramatic Art.  His first marriage was to the actress Valerie Taylor.  In his book "The Stage Struck Me!"  fellow actor Neville Phillips felt Sinclair always played variations of himself, handsome, debonair, suave and witty and excelled in light comedy.  By contrast Phillips felt his wife, who Sinclair often appeared opposite, was a dramatic actress of tremendous power with a magnificent voice.

Emma Hamilton (film): Emma Hamilton is a 1968 historical drama film directed by Christian-Jaque and starring Michèle Mercier, Richard Johnson and John Mills.  It was partly based on the 1864 novel "La Sanfelice" by Alexandre Dumas and depicts the love affair between Emma Hamilton and Horatio Nelson.  It was a co-production between Italy, West Germany, France and the United States.

Emma Hamilton (actress): Emma Hamilton (born 1984 in Melbourne) is an Australian-born British film, television and theatre actress and graduate of the Royal Academy of Dramatic Art.

Tony Beckley: Derek Anthony "Tony" Beckley (7 October 1929 – 19 April 1980) was an English character actor.  A graduate of the Royal Academy of Dramatic Art, Beckley went on to carve out a career on film and television throughout the 1960s and 1970s often playing villainous roles, as well as being a veteran of numerous stage productions.

Tomahawk Theatre Company: Tomahawk is a theatre company based in Oxford, South East England.  Founded in 2005 by Alex Nicholls and Oliver Baird among others, experienced personnel work alongside young actors, directors and technicians, many of whom have gone on to train in London at the Royal Academy of Dramatic Art (RADA), London Academy of Music and Dramatic Art (LAMDA) and Mountview Academy of Theatre Arts.

Question: Emma Hamilton is an Austarlian-born actress and graduate of the Royal Academy of Dramatic Art which is based in what city?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actress_name": {
      "type": "string",
      "description": "The name of the actress mentioned in the question."
    },
    "drama_school": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the drama school."
        },
        "location": {
          "type": "object",
          "properties": {
            "city": {
              "type": "string",
              "description": "The city where the drama school is located."
            },
            "country": {
              "type": "string",
              "description": "The country where the drama school is located."
            }
          },
          "required": [
            "city",
            "country"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "name",
        "location"
      ],
      "additionalProperties": false
    },
    "is_graduate": {
      "type": "boolean",
      "description": "Indicates if the actress is a graduate of the specified drama school."
    }
  },
  "required": [
    "actress_name",
    "drama_school",
    "is_graduate"
  ],
  "additionalProperties": false
}

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
Paul Torday: Paul Torday (1 August 1946 – 18 December 2013) was a British writer and the author of the comic novel, "Salmon Fishing in the Yemen".  The book was the winner of the 2007 Bollinger Everyman Wodehouse Prize for comic writing and was serialised on BBC Radio 4.  It won the Waverton Good Read Award in 2008.  It was made into a popular movie in 2011, starring Ewan McGregor and Emily Blunt.

Stay (2005 film): Stay is a 2005 American psychological thriller film directed by Marc Forster and written by David Benioff.  It stars Ewan McGregor, Naomi Watts, Ryan Gosling and Bob Hoskins, with production by Regency and distribution by 20th Century Fox.  The film represents intense relationships centering on reality, death, love and the afterlife.

Black Hawk Down (film): Black Hawk Down is a 2001 war film co-produced and directed by Ridley Scott, from a screenplay by Ken Nolan.  It is based on the 1999 non-fiction book of the same name by Mark Bowden, which in turn is based on the 29-part series of articles published in "The Philadelphia Inquirer", chronicling the events of a 1993 raid in Mogadishu by the U.S. military aimed at capturing faction leader Mohamed Farrah Aidid, and the ensuing firefight, known as the Battle of Mogadishu.  The film features a large ensemble cast, including Josh Hartnett, Ewan McGregor, Eric Bana, Tom Sizemore, William Fichtner, Jason Isaacs, Tom Hardy in his feature film debut, and Sam Shepard.

Frances Healy: Frances "Franny" Healy (born 24 August 1970) is an Irish actress, comedian, radio personality and TV presenter.  She starred as "Niamh Corrigan" in the famous BBC Scotland soap opera "River City".  Other television credits include Taggart and the Irish soap Fair City.  Film credits include The Magdalene Sisters and The Serpent's Kiss, where she starred alongside Ewan McGregor.  Theatre credits include "The Vagina Monologues", "The Seagull" and "Juno and the Paycock".

Ewan McGregor filmography: The filmography of Scottish actor, voice actor and director Ewan McGregor.  McGregor made his debut in the British television series "Lipstick on Your Collar".  He followed this one year later by appearing in Bill Forsyth's "Being Human" (1994), Danny Boyle's thriller "Shallow Grave" (1994).  Two years later, he plays the heroin addict Mark Renton in Danny Boyle's "Trainspotting" which garnered his international recognition.  He reprised the role in the sequel film "T2 Trainspotting" (2017).

Naomi Watts: Naomi Ellen Watts (born 28 September 1968) is an English actress and film producer.  She made her screen debut in the Australian drama film "For Love Alone" (1986) and then appeared in the Australian television series' "Hey Dad. . ! " (1990), "Brides of Christ" (1991), "Home and Away" (1991) and the coming-of-age comedy-drama film "Flirting" (1991).  After moving to America, Watts appeared in films, including "Tank Girl" (1995), "" (1996) and "Dangerous Beauty" (1998) and had the lead role in the television series "Sleepwalkers" (1997–1998).

Ed Blum: Ed Blum is the director and producer of "Scenes of a Sexual Nature" (2006), a low budget British movie starring Ewan McGregor and Sophie Okonedo, filmed entirely on Hampstead Heath.  This was his first full-length feature and as Blum said, was made "for less than "Love Actually" 's catering budget."

American Pastoral (film): American Pastoral is a 2016 American crime-drama film directed by Ewan McGregor and written by John Romano, based on the 1997 novel of the same name by Philip Roth.  The film stars McGregor, Jennifer Connelly, Dakota Fanning, Peter Riegert, Rupert Evans, Uzo Aduba, Molly Parker and David Strathairn.  Principal photography began on September 21, 2015, in Pittsburgh.

Marcel Langenegger: Marcel Langenegger (April 2, 1967 – September 10, 2015) was a Swiss film director, film producer and screenwriter from Rebstein, Switzerland.  His 2008 debut feature film, "Deception", starred Hugh Jackman, Ewan McGregor, and Michelle Williams.

Tube Tales: Tube Tales is a collection of nine short films based on the true-life experiences of London Underground passengers as submitted to Time Out magazine.  The stories were scripted and filmed independently of each other.  Filming took place on the London Underground network in 1999 by nine directors including Stephen Hopkins, Charles McDougall and Bob Hoskins, with directorial debuts by Ewan McGregor and Jude Law.  The film was produced by Richard Jobson and is also Simon Pegg's film debut, in a small role.

Question: The actress that starred in "Stay" alongside Ewan McGregor made her film debut in which movie?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actress_name": {
      "type": "string",
      "description": "The name of the actress who starred alongside Ewan McGregor in the specified film."
    },
    "film_with_ewan_mcgregor": {
      "type": "string",
      "description": "The title of the film where the actress starred with Ewan McGregor."
    },
    "debut_film": {
      "type": "string",
      "description": "The title of the film in which the actress made her debut."
    },
    "debut_film_year": {
      "type": "integer",
      "description": "The release year of the actress's debut film."
    }
  },
  "required": [
    "actress_name",
    "film_with_ewan_mcgregor",
    "debut_film",
    "debut_film_year"
  ],
  "additionalProperties": false
}

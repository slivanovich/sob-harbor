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
JJ Appleton: JJ Appleton, born Jon Jason Appleton, is an American musician and singer-songwriter based in New York City who has toured throughout the United States extensively in support of his own records and also with other bands including Jamie Cullum, Newton Faulkner, Pete Yorn, Edwin McCain, Sister Hazel, Joan Osborne, Keb Mo, Hootie and the Blowfish.  Appleton has been described by the Washington Post as a songwriter with a “pop-rock sound but with considerably more edgy energy, adding figurative lightning to the stormy night.”  Previously a member of the popular New York band The Grasshoppers, Appleton released his first solo album "500 Moments" in 2003 which led to appearances on the NBC television show "Last Call with Carson Daly", a feature on E!'s "Wild On", and a national affiliation with Budweiser's True Music Live program and Gibson Guitars.  Appleton released his album "Uphill to Purgatory" in the United States in 2005 which was then re-released in the United Kingdom in 2006 as "Someone Else's Problem" and included three songs from the "500 Moments" EP.  Based on the recognition he was receiving in England, Appleton decided to move to London in 2006 where he became a regularly featured performer at popular venues such as Ronnie Scott's, The Borderline, and The Regal Room.  In the meantime, the single "Walk Into The Room" and it's accompanying video became a favorite on English radio and MTV Two.  In 2015, Appleton released an acoustic blues album entitled "Dirty Memory" with harmonicist Jason Ricci.

Tobias Menzies: Tobias Menzies (born 7 March 1974) is an English stage, television and film actor.  While working in theatre, he starred in television shows such as "Rome" (2005–2007) where he played Brutus and "Game of Thrones" (2013–2016) where he played Edmure Tully.  He is probably best known for his dual role as Frank Randall and Jonathan "Black Jack" Randall in "Outlander" (2014–present), for which he received a Golden Globe Award nomination.

The Sound of Music Live!: The Sound of Music Live!  is a television special that was originally broadcast by NBC on December 5, 2013.  Produced by Craig Zadan and Neil Meron, the special was an adaptation of Rodgers and Hammerstein's Broadway musical "The Sound of Music", starring country singer Carrie Underwood as Maria von Trapp, performed and televised live from Grumman Studios in Bethpage, New York.

Michael Hordern: Sir Michael Murray Hordern, CBE (3 October 19112 May 1995) was an English stage and film actor whose career spanned nearly 60 years.  He is best known for his Shakespearean roles, especially that of King Lear, which he played to much acclaim on stage in Stratford-upon-Avon in 1969 and London in 1970.  He then successfully assumed the role on television five years later.  He often appeared in film, rising from a bit part actor in the late 1930s to a member of the main cast; by the time of his death he had appeared in nearly 140 cinema roles.  His later work was predominantly in television and radio.

The Sound of Music Live (2015): The Sound of Music Live is a television special that was originally broadcast by ITV on 20 December 2015.  The special was an adaptation of Rodgers and Hammerstein's Broadway musical "The Sound of Music", starring Kara Tointon as Maria von Trapp, performed and televised live from 3 Mills Studios in London.  Notable cast members include: Kara Tointon, Katherine Kelly, Alexander Armstrong, Julian Ovenden, Mel Giedroyc, Maria Friedman and notable child actors including Guy Trundle, Tom Sargent and Zac Lester, among others.

Kyrle Bellew: Harold Kyrle Money Bellew (28 March 1850 – 2 November 1911), better known as Kyrle Bellew, was an English stage and silent film actor in the late 19th and early 20th century.  He notably toured with Cora Brown-Potter in the 1880s and 1890s, and was cast as the leading man in many stage productions alongside her.  He was also a signwriter, gold prospector and rancher mainly in Australia.

Julian Ovenden: Julian Mark Ovenden (born 29 November 1976) is an English stage, television and film actor and singer.  He has starred on Broadway and in the West End, in television series in both the UK and US, as well as having an international career as a concert and recording artist.

Gordon Harker: Gordon Harker (7 August 1885 – 2 March 1967) was an English stage and film actor.  he had a long career on the stage, from 1902 to the 1950s.  One of the last plays he starred in was "Small Hotel", a popular comedy he toured in 1955.  In addition, he appeared in 68 films between 1921 and 1959, including three silent films directed by Alfred Hitchcock and in several scenes in "Elstree Calling" (1930), a revue film co-directed by Hitchcock.  He was known for his performance as Inspector Hornleigh in a trilogy of films produced between 1938 and 1940, as well in "Saloon Bar" (1940), based on a stage play he had starred in and another one of his stage successes The Poltergeist made into the film "Things Happen at Night" (1947), a poltergeist comedy he co-starred in with Alfred Drayton and Robertson Hare.  His last major screen role was as the wiley waiter Albert in the 1957 motion picture version of "Small Hotel"

Something Good (Richard Rodgers song): "Something Good" is a song written by Richard Rodgers for the film version of "The Sound of Music".  It replaced the original song sung by Maria and Captain Georg von Trapp called "An Ordinary Couple".  Since then the song has been used in the various reproduction of the play and most recently the 2013 television special, "The Sound of Music Live! ".

Laura Benanti: Laura Ilene Benanti (born Laura Ilene Vidnovic; July 15, 1979) is an American actress and singer.  She played Louise in the 2008 Broadway revival of "Gypsy", winning the Tony Award, and appeared in the stage musical "Women on the Verge of a Nervous Breakdown" in 2010, winning the Drama Desk Award and Outer Critics Circle Award for Best Featured Actress in a Musical.  She played Baroness Elsa Schräder in the 2013 NBC television production of "The Sound of Music Live! " and in 2015 began playing twin sisters Alura and Astra in the TV series "Supergirl".  Beginning in 2017, Benanti appears as Edie in the TBS comedy "The Detour".

Question: The Sound of Music Live cast included an English stage, television and film actor and singer who starred on what?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the actor identified in the context."
    },
    "actor_nationality": {
      "type": "string",
      "description": "The nationality of the actor."
    },
    "actor_professions": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of professions or roles the actor is known for."
    },
    "starred_on_location": {
      "type": "string",
      "description": "The specific location or type of production the actor starred on, as asked in the question."
    },
    "production_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the production the actor was part of."
        },
        "year": {
          "type": "integer",
          "description": "The year the production was broadcast."
        }
      },
      "required": [
        "title",
        "year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "actor_name",
    "actor_nationality",
    "actor_professions",
    "starred_on_location",
    "production_details"
  ],
  "additionalProperties": false
}

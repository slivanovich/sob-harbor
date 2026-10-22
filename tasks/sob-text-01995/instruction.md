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
Bob Brookmeyer Plays Bob Brookmeyer and Some Others: Bob Brookmeyer Plays Bob Brookmeyer and Some Others

James Kelso (footballer): James Kelso (8 January 1869 in Cardross – 25 July 1900 in Renton) was a Scottish footballer who played as a right half.  he was the younger brother of Scotland international player Bob Kelso.  He began his career with Renton before joining Liverpool in 1892 for their inaugural season.  He made one appearance for Liverpool, in a 4-0 win over Bury in the Lancashire League on 24 September 1892.  He rejoined Renton in 1893.  Kelso committed suicide at the age of 31.

Warm Waters: Warm Waters is an album by jazz saxophonist Charles Lloyd recorded in 1971 and released on the Kapp label featuring performances by Lloyd with John Cipollina, Dave Mason, Tom Trujillo, Woodrow Theus II, Ken Jenkins, Bill Wolff, James Zitro, Jesse Ed Davis, and Michael Cohen with guest vocalists Mike Love, Al Jardine, Billy Cowsill, Michael O'Gara, Brian Wilson, Eric Sherman, Carl Wilson and Rhetta Hughes.  The album appeared in Europe the same year on the MCA label in West Germany (MAPS 4961) with the same track listing.

What About Bob?: What About Bob?  is a 1991 American black comedy film directed by Frank Oz, and starring Bill Murray and Richard Dreyfuss.  Murray plays Bob Wiley, a psychiatric patient who follows his egotistical psychiatrist Dr. Leo Marvin (Dreyfuss) on vacation.  When the unstable Bob befriends the other members of Marvin's family, it pushes the doctor over the edge.

Scrubs (TV series): Scrubs (stylized as [scrubs]) is an American medical comedy-drama television series created by Bill Lawrence that aired from October 2, 2001, to March 17, 2010, on NBC and later ABC.  The series follows the lives of employees at the fictional Sacred Heart teaching hospital.  The title is a play on surgical scrubs and a term for a low-ranking person because at the beginning of the series, most of the main characters are medical interns.

Edge of Honor: Edge Of Honor is a 1991 drama / thriller movie directed by Michael Spence who also directed "The Dread" (2007).  The film stars Corey Feldman, Don Swayze, Scott Reeves and Ken Jenkins.

List of Bob Marley and the Wailers band members: Bob Marley and the Wailers were a Jamaican reggae band created by Bob Marley.  The band formed when self-taught musician Hubert Winston McIntosh (Peter Tosh) met Neville Livingston (Bunny Wailer), and Robert Nesta Marley (Bob Marley) in 1963 and taught them how to play guitar, keyboards, and percussion.  By late 1963 Junior Braithwaite, Beverley Kelso, and Cherry Smith had joined the Wailers.  After Peter Tosh and Bunny Wailer left the band in 1974, Bob Marley began touring with new band members.  His new backing band included brothers Carlton Barrett and Aston "Family Man" Barrett on drums and bass respectively, Junior Marvin and Al Anderson on lead guitar, Tyrone Downie and Earl "Wya" Lindo on keyboards, and Alvin "Seeco" Patterson on percussion.  The "I Threes", consisting of Judy Mowatt, Marcia Griffiths, and Marley's wife, Rita, provided backing vocals.

Ken Jenkins: Ken Jenkins (born August 28, 1940) is an American actor, best known for his role as Dr. Bob Kelso, the Chief of Medicine on the American comedy "Scrubs".

Bob Kelso: Robert "Bob" Kelso, M.D., is a fictional character played by Ken Jenkins in the American comedy-drama "Scrubs".

Ivy Jenkins: Ivana Jenkins (née) Vujić (Serbian: Ивана Вујић , born June 15, 1983), known by her stage name Ivy Jenkins is a Serbian-born Canadian bassist.  She played bass for the metal, all-woman band Kittie from October 2007 until March 2012.  She began her career with Kittie by initially filling in for ailing bassist Trish Doan in late 2007, a period which found the band playing concerts in Central and South America.  Before she was in Kittie, Ivy played bass for the melodic hard rock band In The Wake from Toronto, Canada.  In 2008, it was officially announced that Ivy was a full-time member of Kittie and in 2009 she appeared on their fifth studio CD, "In The Black".  Ivy also wrote and recorded bass for Kittie's sixth album, "I've Failed" "You", which was released on August 15, 2011.  Jenkins plays a black Warwick Corvette 5 string bass guitar.

Question: Who created the series where Ken Jenkins plays Bob Kelso?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "series_name": {
      "type": "string",
      "description": "The name of the television series."
    },
    "character_played": {
      "type": "string",
      "description": "The name of the character played by the actor."
    },
    "actor_name": {
      "type": "string",
      "description": "The name of the actor."
    },
    "series_creator": {
      "type": "string",
      "description": "The creator of the television series."
    },
    "series_genre": {
      "type": "string",
      "description": "The genre of the television series."
    }
  },
  "required": [
    "series_name",
    "character_played",
    "actor_name",
    "series_creator",
    "series_genre"
  ],
  "additionalProperties": false
}

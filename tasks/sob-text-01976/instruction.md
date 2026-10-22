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
James Young (director): James Young (January 1, 1872 – June 9, 1948) was an American film director, actor and screenwriter of the silent era.  Before films Young had a successful career as a stage actor appearing on Broadway and throughout the country, and was the author of a notable 1905 book on theatrical makeup.  His first wife was librettist Rida Johnson Young who often composed with Victor Herbert.  Turning to silent films he directed 93 films between 1912 and 1928.  He also appeared as an actor in 62 films between 1909 and 1917.

D.C. Follies: D.C. Follies is a syndicated sitcom which aired from 1987–1989 and was set in a Washington, D.C. bar, where bartender Fred Willard would welcome puppet caricatures of politicians and pop culture figures.  The show was satirical, and frequently commented on politicians and the political process.  Although Willard was the only live actor appearing regularly, each episode brought a celebrity guest into the bar, such as Martin Mull, Robin Leach, Bob Uecker, and Betty White.  In one episode, Robert Englund showed up as his Freddy Krueger character, and in a special Christmas episode an un-billed actor played Santa Claus.  Another episode had Mike Tyson confront his own puppet character.

Johan Widerberg: Johan Olof Widerberg (born 16 March 1974 in Stockholm), is a Swedish actor appearing in numerous Swedish films and TV series.

The Doctor's Dilemma (film): The Doctor's Dilemma is a 1958 British comedy drama film directed by Anthony Asquith and starring Leslie Caron, Dirk Bogarde, Alastair Sim, Robert Morley and Terence Alexander.  It is based on the 1906 play "The Doctor's Dilemma" by George Bernard Shaw.

Jack Kehoe: Jack Kehoe (born November 21, 1938) is an American film actor appearing in a wide variety of films, including the crime dramas "Serpico" (1973), "The Pope of Greenwich Village" (1984) and Brian De Palma's "The Untouchables" (1987), as well as the cult favorites "Car Wash" (1976), "Midnight Run" (1988), the popular western "Young Guns II" (1990) and "On the Nickel" (1980).

Nunzio Gallo: Nunzio Gallo (25 March 1928 – 22 February 2008) was an Italian singer.  He was born in Naples and represented his country in the 1957 Eurovision Song Contest, coming 6th.  The song he performed, "Corde Della Mia Chitarra", is famous for being the longest song ever played for Eurovision at 5:09 before the new rules came into place.  Gallo was also an actor appearing in over 20 films.  Gallo suffered severe brain haemorrhage in September 2007 from which he never fully recovered.  He died on 22 February 2008 in Telese Terme.

Alastair Sim: Alastair George Bell Sim, CBE (9 October 1900 – 19 August 1976) was a Scottish character actor who began his theatrical career at the age of thirty, but quickly became established as a popular West End performer, remaining so until his death in 1976.  He also appeared in more than fifty British films, starting in 1935.

Raoul Retzer: Raoul Retzer (1919–1974) was an Austrian actor.  Retzer was a prolific film actor appearing in more than a hundred and forty productions between 1952 and 1975 generally in small or supporting roles.  He appeared in the 1955 film "The Last Ten Days".

Vijay Kumar (British filmmaker): Vijay Kumar is a long-standing member of the film and media industry.  Having started in his early days as an actor in theatre productions, Vijay then moved on to becoming a fully fledged actor appearing in a number of feature films in Bollywood, such as: Gangster, Main Solah Baras Ki, Master, King of Bollywood and Love U Mr Kalakaar.  Vijay also played a comic role in the hit TV series Dekh Bhai Dekh.  During Vijay's career as an actor, he was always involved in presenting, whether it was on air or TV.  Vijay had amassed a large following with his featured show on BBC and Asian Sound Radio in the early 2000s.  Vijay still however had not satisfied his creative flow and took up the chance to be the Director, Writer and Producer of his own short films.  Vijay has gone on to create over 5 short films since 2003, many of which have been featured in film festivals such as: Cannes Film Festival, Ekotop Film Festival, JIFF India, Wirral International Film Festival and the Edinburgh Film Festival.

Jarlath Conroy: Jarlath Conroy (born 30 September, 1944) is an Irish theatre, film and television actor.  Since 1971, he has become a successful actor appearing in film and television, including "NYPD Blue", "Law & Order", and "".  He also appeared in the movies "Day of the Dead" and "The Art of Getting By".  His most recent appearance is as the Undertaker in the 2010 remake of "True Grit".  He is also the voice actor of Aiden O'Malley in Rockstar Games's "Grand Theft Auto IV".

Question: What actor appearing in "The Doctor's Dilemma," died in 1979?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film mentioned in the question."
    },
    "death_year_sought": {
      "type": "integer",
      "description": "The specific death year requested for the actor."
    },
    "search_performed": {
      "type": "boolean",
      "description": "Indicates whether a search for actors matching the criteria was performed."
    },
    "matching_actors": {
      "type": "array",
      "description": "A list of actors who appeared in the specified film and died in the specified year.",
      "items": {
        "type": "object",
        "properties": {
          "actor_name": {
            "type": "string",
            "description": "The full name of the actor."
          },
          "death_year": {
            "type": "integer",
            "description": "The year the actor died."
          }
        },
        "required": [
          "actor_name",
          "death_year"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "film_title",
    "death_year_sought",
    "search_performed"
  ],
  "additionalProperties": false
}

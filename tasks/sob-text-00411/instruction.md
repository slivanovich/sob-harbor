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
Christopher Nelson (makeup artist): Christopher Nelson is an American makeup artist, VFX artist, writer and actor.  He is best known for his makeup and stylings for films such as "", "", "", "Sin City", "", "The Amazing Spider-Man", "World War Z", "Deadpool", "Guardians of the Galaxy Vol.  2" and "Suicide Squad" (2016) has earned him numerous awards and nominations.  He also played the groom of Beatrix "Black Mamba" Kiddo in "Kill Bill: Volume 2".

Mark Sanchez (make-up artist): Mark Sanchez is an American makeup artist.  He was nominated at the 68th Academy Awards for Best Makeup.  He was nominated for the film "My Family, Mi Familia", which he shared the nomination with Ken Diaz.

World War Z (film): World War Z is a 2013 American action horror film directed by Marc Forster.  The screenplay by Matthew Michael Carnahan, Drew Goddard, and Damon Lindelof is from a screen story by Carnahan and J. Michael Straczynski, based on the title of the 2006 novel of the same name by Max Brooks.  The film stars Brad Pitt as Gerry Lane, a former United Nations investigator who must travel the world to find a way to stop a zombie pandemic.

David LeRoy Anderson: David LeRoy Anderson is an American makeup artist who has won two Academy Awards for Best Makeup, first was at the 69th Academy Awards for the film "The Nutty Professor", then the following year at the 70th Academy Awards for "Men in Black".  Both wins were shared with Rick Baker.

Jeff Dawn: Jeff Dawn is an American makeup artist who is known for working with Arnold Schwarzenegger, which he has done makeup on 19 of his films.

Lynn Barber (make-up artist): Lynn Barber is an American makeup artist.  She won at the 1989 Academy Awards for Best Makeup for the film "Driving Miss Daisy".  Which she shared with Kevin Haney and Manlio Rocchetti.

Julie Hewett: Julie Hewett is an American makeup artist.  She first began working in the field with the 1987 film "The Whales of August" and since then has gone on to work with films such as "American Beauty", "Spider-Man 2", "Ocean's Eleven" and "The Artist".  Hewett has her own cosmetics company, Julie Hewett Los Angeles.

Face Off (TV series): Face Off is an American reality television game show on the Syfy cable network in which a group of prosthetic makeup artists compete against each other to create prostheses such as those found in science fiction and horror films. Each episode features one or more challenges, with the work reviewed by a panel of judges and eliminating one or more artists each week until a final winner is chosen.  Actress McKenzie Westmore, known for her role as Sheridan Crane on the former NBC/DirecTV soap opera "Passions" and a member of the Westmore family of makeup artists, serves as the show's host.  For each assignment, the contestants' work is individually evaluated by a panel of professional special effects makeup artists who serve as judges.  These judges have included Academy Award-winning makeup artist Ve Neill, and television and film makeup artist Glenn Hetrick, creature designer and director Patrick Tatopoulos (Season 1 - 3), and Neville Page (Season 3 - present).  Industry figures and artists including Brian Grazer, Kevin Smith, Paul W. S. Anderson, Greg Nicotero, Rick Baker, Doug Jones, Len Wiseman and Gale Anne Hurd have served as guest judges.

John Blake (makeup artist): John Blake is an American makeup artist.  He has been nominated for one Academy Award, for the film Hoffa.  He shared the nomination with Ve Neill and Greg Cannom.  He has worked on films for directors like Oliver Stone and the Coen Brothers as key makeup artist on Nixon, U Turn, and Fargo.  In more recent years, he has worked on The Avengers, the Iron Man trilogy, There Will Be Blood, Tropic Thunder, and many other films over a 30 year career.

Lance Anderson: Lance Anderson is an American makeup artist who was nominated at the 78th Academy Awards in the category of Best Makeup.  He shared his nomination with his son, David LeRoy Anderson for their work on the film "Cinderella Man".

Question: Christopher Nelson is an American makeup artist, VFX artist, writer and actor, he's best known for his makeup and stylings for films such as World War Z, a 2013 American action horror film, directed by who?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "film_year": {
      "type": "integer",
      "description": "The release year of the film."
    },
    "film_genre": {
      "type": "string",
      "description": "The genre of the film."
    },
    "director_name": {
      "type": "string",
      "description": "The name of the director of the film."
    },
    "makeup_artist_involved": {
      "type": "string",
      "description": "The name of the makeup artist associated with the film in the context."
    }
  },
  "required": [
    "film_title",
    "film_year",
    "film_genre",
    "director_name",
    "makeup_artist_involved"
  ],
  "additionalProperties": false
}

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
Rudolf Rittner: Rudolf Rittner (30 June 1869 – 4 February 1943) was a German actor born in Weissbach, Moravia, famous for playing knight and folk hero Florian Geyer in Gerhart Hauptmann's drama of the same name.  The well-known German painter Lovis Corinth portrayed him in 1906.  Only one year later, at the age of 38, Rittner being at the peak of his career retired as theatrical actor.

Abe Vigoda: Abraham Charles Vigoda ( ; February 24, 1921 – January 26, 2016) was an American character actor who was known for a number of roles, most notably, his portrayals of Salvatore Tessio in "The Godfather" (1972) and Phil Fish in "Barney Miller" (1975–1977, 1982) and "Fish" (1977–1978).

Jerry O'Connell: Jeremiah "Jerry" O'Connell (born February 17, 1974) is an American actor, known for his roles as Quinn Mallory in the TV series "Sliders", Andrew Clements in "My Secret Identity", Vern Tessio in the film "Stand by Me" (1986), Frank Cushman in "Jerry Maguire" (1996), Derek in "Scream 2" (1997), Charlie Carbone in "Kangaroo Jack" (2003), and Detective Woody Hoyt on the drama "Crossing Jordan".  He starred as Pete Kaczmarek in the CBS TV series "The Defenders" until its cancellation in 2011.  He also had a starring role in the comedy horror film "Piranha 3D" (2010).

Casey Siemaszko: Kazimierz A. "Casey" Siemaszko (born March 17, 1961) is an American actor.  His best known film roles are "Back to the Future" and "Back to the Future Part II" as 3-D, "Stand By Me" as Billy Tessio, "Young Guns" as Charlie Bowdre, and as Curley in "Of Mice and Men".

Christian Byers: Christian Byers (born 31 July 1993, Sydney, New South Wales, Australia), is an Australian actor born on 31 July 1993 in Sydney.  In 2006, he made his film debut in Opal Dream, before featuring in December Boys alongside Daniel Radcliffe.  In 2007, Christian portrayed Jacob in Hey, Hey, It's Esther Blueburger.  Christian is also the lead vocalist, second guitarist and organist of the band The Slippers.  He is also participating in a Sydney-based television show,The Flip, as Maxx.  He currently attends University of Technology, Sydney

Salvatore Tessio: Salvatore "Sal" Tessio is a fictional character in Mario Puzo's 1969 novel "The Godfather", as well as two of the films based on it: "The Godfather" and "The Godfather Part II" (1974).  His given name was created for the films; in the novel he is referred to only as "Tessio".  In the film "The Godfather", Tessio was portrayed by Abe Vigoda.  In "The Godfather Part II", John Aprea portrayed the younger Tessio, while Vigoda reprised the role in a flashback, set in late 1941, at the end of the film.

Derek Royle: Derek Royle (7 September 1928 – 23 January 1990) was a British actor born in London, England.  His face was probably better known than his name to British viewers, but he acted in films and TV from the mid-1960s until his death.  He had a supporting role in the Beatles' film "Magical Mystery Tour" in 1967, as well as a minor one with Cilla Black in the film "Work Is a Four-Letter Word" a year later.  Most of his film appearances were in comedy films such as "Don't Just Lie There, Say Something! " (1973), "Tiffany Jones" (1973) and "Confessions of a Sex Maniac" (1974).

John Aprea: Jonathan "John" Aprea (born March 4, 1941) is an American actor and comedian, best known for his role as the young Sal Tessio in "" (1974) and on television as Lucas Castigliano in "Another World" from 1989 to 1992.  In 2006, he appeared in "The Heiress".  He also portrayed Nick Katsopolis in "Full House".  He also co-starred with Lee Horsley in "Matt Houston" during the 1980s.

Bruce Locke: Bruce Asato Locke is an American actor born and raised in Oregon.  Though he wasn't originally a martial artist, Locke frequently portrayed action characters who are, which led to his own career in martial arts.  He is trained in kempo, wing chun, shaolin kung fu and Choy Li Fut.

D'Arcy Browning: D'Arcy Browning is a Canadian actor born in Edmonton and raised in South Cooking Lake, Alberta in the early 2000's he portrayed Jesus Christ in the "Canadian Badlands Passion Play", Drumheller.  The CBC filmed the documentary "The Cross and Bones" following Browning and the cast, paleontology experts from the Tyrell Museum and the bikers of the valley for the clash of science and religion every summer for the past dozen years.  The film opened Hot Docs Canadian International Documentary Festival for the Toronto-based documentary film festival and travelled internationally.

Question: In the film "The Godfather", Salvatore Tessio was portrayed by an actor born in which year ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "character_name": {
      "type": "string",
      "description": "The name of the character in the film."
    },
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "actor": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the actor who portrayed the character."
        },
        "birth_year": {
          "type": "integer",
          "description": "The birth year of the actor."
        }
      },
      "required": [
        "name",
        "birth_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "character_name",
    "film_title",
    "actor"
  ],
  "additionalProperties": false
}

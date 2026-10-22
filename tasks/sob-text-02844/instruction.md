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
The Swords of the Swashbucklers: Swords of the Swashbucklers first appeared in the Marvel Graphic Novel range.  Epic Comics, a division of Marvel Comics, began publishing it as a twelve-issue mini-series between March 1985 and March 1987.  The series was created by Bill Mantlo and Jackson Guice.

Jackson Guice: Jackson "Butch" Guice (born June 27, 1961) is an American comics artist who has worked in the comics industry since the 1980s.

Cloak and Dagger (comics): Cloak (Tyrone "Ty" Johnson) and Dagger (Tandy Bowen) are a fictional comic book superhero duo appearing in American comic books published by Marvel Comics.  They were created by writer Bill Mantlo and artist Ed Hannigan.  In April 2016, Marvel Television announced that the duo would appear in their own television series, with Aubrey Joseph and Olivia Holt portraying Johnson and Bowen, respectively.

Dmitri Bukharin: Dmitri Bukharin is a fictional character appearing in American comic books published by Marvel Comics.  Created by writer Bill Mantlo and artist Carmine Infantino, the character made his first appearance in "Iron Man" #109 (April 1978).  The fifth character to use the Crimson Dynamo name, he spent the longest time using the identity and armor.

Rocket Raccoon: Rocket Raccoon is a fictional superhero appearing in American comic books published by Marvel Comics.  Created by writer Bill Mantlo and artist Keith Giffen, the character first appeared in "Marvel Preview" #7 (Summer 1976).  He is an intelligent, anthropomorphic raccoon, who is an expert marksman and master tactician.  His name and aspects of his character are a nod to The Beatles' 1968 song "Rocky Raccoon".

Micronauts (comics): The Micronauts comic books featuring a group of characters based on the Mego Micronauts toy line.  The first title was published by Marvel Comics in 1979, with both original characters and characters based on the toys.  Marvel published two "Micronauts" series, mostly written by Bill Mantlo, until 1986, well after the toy line was cancelled in 1980.  In the 2000s, Image Comics and Devil's Due Publishing each briefly published their own "Micronauts" series.  Byron Preiss Visual Publications also published three paperback novels based on the Micronauts.  In July 2015, IDW Publishing announced that they would publish a new comic book series.

Shooting Star (comics): Shooting Star is a comic book superheroine appearing in American comic books published by Marvel Comics.  The character was created by writer Bill Mantlo and penciller Sal Buscema and first appeared in "Incredible Hulk" vol.1 #265 (November 1981).  She is a member of the Rangers, the American Southwest superhero team.

Jack of Hearts: Jack of Hearts (Jack Hart) is a fictional character, a superhero appearing in American comic books published by Marvel Comics.  The character first appeared in Deadly Hands of Kung Fu 22, and was created by writer Bill Mantlo and artist Keith Giffen.  He starred in his own 4 issue mini series and has been a regular character in the Iron Man comics as well as at one point being a regular in the Avengers comic book.

White Tiger (Hector Ayala): White Tiger (Hector Ayala) is a fictional character appearing in American comic books published by Marvel Comics.  He was created by Bill Mantlo and George Pérez.  He is the first Puerto Rican superhero in the history of comics, and Marvel's first superhero of Latino descent.  Hector is the uncle of Angela del Toro and the brother of Ava Ayala.

Copperhead (Marvel Comics): Copperhead is the name of three different fictional characters appearing in American comic books published by Marvel Comics.  The first Copperhead was Lawrence Chesney, who made his debut in "Daredevil" #124 (Aug 1975) and was created by writers Len Wein and Marv Wolfman, and artist Gene Colan.  The second Copperhead, Arthur Reynolds, was a coworker of Chesney and stole his costume after Chesney was killed.  Reynolds first appeared in "Human Fly #8" (Apr 1978) by writer Bill Mantlo and artist.  Frank Robbins.  The third person to use the name Copperhead is totally unrelated to the first two characters, Davis Lawfers, who took the name from the snake of the same name.  Lawfers first appeared in "Captain America" #337 (1988) created by writers Mark Gruenwald and Ralph Macchio and artist Tom Morgan.

Question: When was the American comics artist born who along with Bill Mantlo created The Swords of the Swashbucklers?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "creator_name": {
      "type": "string",
      "description": "The name of the artist who co-created the comic series."
    },
    "birth_date": {
      "type": "string",
      "format": "date",
      "description": "The birth date of the artist."
    },
    "comic_series_created": {
      "type": "string",
      "description": "The name of the comic series co-created by the artist and Bill Mantlo."
    }
  },
  "required": [
    "creator_name",
    "birth_date",
    "comic_series_created"
  ],
  "additionalProperties": false
}

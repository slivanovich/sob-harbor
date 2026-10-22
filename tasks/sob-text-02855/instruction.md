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
Domestic Disturbance: Domestic Disturbance is a 2001 American psychological thriller film directed by Harold Becker (his last film to date) and starring John Travolta, Vince Vaughn, Teri Polo, Steve Buscemi, and Matt O'Leary.

Mystery Date: Mystery Date is a 1991 American teen comedy film directed by Jonathan Wacks and starring Ethan Hawke, Teri Polo, and Brian McNamara.  Shock-rockers Gwar have a brief cameo in the film.

The Beacon (film): The Beacon is a 2009 American horror/thriller film.  It is the second film made by Sabbatical Pictures.  It was later officially renamed "Haunting at the Beacon".  The film was shot in The Rogers Hotel in Waxahachie, Texas.  The film's theatrical debut is in seven cities in October 2009.  The film debuted at the 2009 Paranoia Film Festival where it won for Best Picture and Best Actress (Teri Polo).  It has been selected to be one of the films for the 2009 LA Femme Film Festival.  The film was directed and written by Michael Stokes.

The Hole (2009 film): The Hole is a 2009 American 3D fantasy horror film directed by Joe Dante and stars Teri Polo, Chris Massoglia, and Haley Bennett.

Second String: Second String is a direct-to-TV film from 2002 about the Buffalo Bills football team who find its first string (led by real-life Bills quarterback Doug Flutie, who had left the team by the time the film was released) out for a month after a food poisoning incident, leading the team's head coach, "Chuck Dichter" (portrayed by Jon Voight), to hire an insurance salesman named Dan Heller (played by Gil Bellows) as the team's backup quarterback.  Teri Polo also appeared as Heller's wife; Flutie, Mike Ditka, Chris Berman, Van Miller, Bills cornerback Donovan Greer and Ken "Pinto Ron" Johnson appear as themselves.  The film originally aired on TNT.

Full Circle (novel): Full Circle is a 1984 romance novel by Danielle Steel.  It was adapted by Karol Ann Hoeffner into a 1996 television film starring Teri Polo.

Joe Dante: Joseph James "Joe" Dante, Jr. ( ; born November 28, 1946) is an American film director, producer, editor and actor.  His films—notably "Gremlins" (1984)—often mix fantastical storylines with comedic elements.

Gremlins 2: The New Batch: Gremlins 2: The New Batch is a 1990 American comedy horror film, and the sequel to the 1984 film "Gremlins".  It was directed by Joe Dante and written by Charles S. Haas, with creature designs by Rick Baker.  It stars Zach Galligan, Phoebe Cates, John Glover, Robert Prosky, Haviland Morris, Dick Miller, Jackie Joseph, Robert Picardo and Christopher Lee; additionally, the film features Tony Randall and Frank Welker providing the voices for two gremlins.  The story continues the adventures of the creature Gizmo (once again voiced by Howie Mandel), who spawns numerous small monsters when wet.  In the first film, Gizmo's offspring rampaged through a small fictional town.  In "Gremlins 2", Gizmo multiplies within a skyscraper in New York City.  The new creatures thus pose a serious threat to the city should they be able to leave the building, and much of the story involves the human characters' efforts to prevent this disaster.

A Plumm Summer: A Plumm Summer is a 2007 adventure-family film directed by Caroline Zelder.  It stars Owen Pearce, Chris Massoglia (appearing under the name "Chris J. Kelly"), Morgan Flynn, William Baldwin, Henry Winkler, and Lisa Guerrero.  The film follows a teenage boy, his young brother, and a new-to-town teenage girl as they try to find a marionette from a local television show which has been stolen and held for ransom.  Meanwhile, the brothers' father struggles with alcoholism and their mother tries to hold her marriage together.

Authors Anonymous: Authors Anonymous is a 2014 comedy American film directed and produced by Ellie Kanner.  It stars Kaley Cuoco, Chris Klein, Tricia Helfer, Jonathan Banks, Jonathan Bennett, Teri Polo and Dennis Farina in his final film role.  The film was released on March 18, 2014 through video on demand prior to its limited release on April 18, 2014 by Screen Media Films and Starz Digital.

Question: What is the release date of the film that the director of the 1984 film "Gremlins" directed that stared Teri Polo, Chris Massoglia, and Haley Bennett?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "director": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the film's director."
        }
      },
      "required": [
        "name"
      ],
      "additionalProperties": false
    },
    "main_actors": {
      "type": "array",
      "description": "A list of the main actors starring in the film.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of an actor."
          }
        },
        "required": [
          "name"
        ],
        "additionalProperties": false
      }
    },
    "release_year": {
      "type": "integer",
      "description": "The release year of the film."
    }
  },
  "required": [
    "film_title",
    "director",
    "main_actors",
    "release_year"
  ],
  "additionalProperties": false
}

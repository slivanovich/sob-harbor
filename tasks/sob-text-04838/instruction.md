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
Smiley Face (film): Smiley Face is a 2007 comedy film written by Dylan Haggerty and directed and co-produced by Gregg Araki.  It stars Anna Faris as a young woman who has a series of misadventures after eating a large number of cupcakes laced with cannabis.  The supporting cast includes Danny Masterson, John Krasinski, Adam Brody, Jayma Mays, Marion Ross, Jane Lynch, and Roscoe Lee Browne in his final film.  This was the ninth feature film directed by Araki.

Jennifer's Body: Jennifer's Body is a 2009 supernatural horror black comedy film written by Diablo Cody and directed by Karyn Kusama.  The film stars Megan Fox, Amanda Seyfried, Johnny Simmons, and Adam Brody.  Fox portrays a demonically possessed high school girl who kills her male classmates, with her best friend striving to stop her.  The film premiered at the 2009 Toronto International Film Festival and was released in the United States and Canada on September 18, 2009.  The title is a reference to the song of the same name by alternative rock band Hole on their album "Live Through This".  As a tie-in to the film, Boom!  Studios produced a "Jennifer's Body" graphic novel, released in August 2009.

Adam Brody: Adam Jared Brody (born December 15, 1979) is an American actor, writer, musician and producer.  He is best known for his role as Seth Cohen on "The O.C.".  Brody has appeared in the films "Mr. & Mrs. Smith" (2005), "Thank You for Smoking" (2006), "In the Land of Women" (2007), "Jennifer's Body" (2009), "Cop Out" (2010), "Scream 4" (2011), "Lovelace" (2013), "Life Partners" (2014), and "Sleeping with Other People" (2015).

Life Partners: Life Partners is a 2014 American comedy film directed by Susanna Fogel and co-written with Joni Lefkowitz.  It is Fogel's feature film directorial debut.  The film stars are Leighton Meester, Gillian Jacobs, Adam Brody, Greer Grammer, Gabourey Sidibe, and Julie White.  The film premiered on April 18, 2014 at the Tribeca Film Festival in the Spotlight section.  The film was released on November 6, 2014 on demand platforms, and in select theaters on December 5, 2014.

Some Girl(s) (film): Some Girl(s) is a 2013 American comedy film directed by Daisy von Scherler Mayer and written by Neil LaBute.  It is based on the play of the same name, also written by LaBute.  The film stars Adam Brody, Kristen Bell, Zoe Kazan, Mía Maestro, Jennifer Morrison and Emily Watson.  The film was released on June 26, 2013, by Leeden Media.

Damsels in Distress: Damsels in Distress (original title: Violet Wister's Damsels in Distress and Whit Stillman's Damsels in Distress) is an American comedy film written and directed by Whit Stillman and starring Greta Gerwig, Adam Brody, and Analeigh Tipton.  It is set at a United States East Coast university.  First screened at the 68th Venice International Film Festival and the Toronto International Film Festival, the film opened in New York and Los Angeles on April 6, 2012.

CHiPs (film): CHiPs is a 2017 American action comedy buddy cop film written and directed by Dax Shepard, based on the 1977–1983 television series of the same name created by Rick Rosner.  The film stars Shepard as Officer Jon Baker and Michael Peña as Frank "Ponch" Poncherello, with Rosa Salazar, Adam Brody and Vincent D'Onofrio in supporting roles.

Play Dead (2009 film): Play Dead is a 2009 black comedy film directed and co-produced by Jason Wiles, and written by Wiles and Shem Bitterman.  The film stars Chris Klein, Fred Durst, and Jake Busey.  Filming took place at the end of 2006, in Ely, Nevada and Los Angeles, California.  The film was ultimately released direct-to-video on September 22, 2009.

Baggage Claim (film): Baggage Claim is a 2013 American romantic comedy film directed by David E. Talbert and written by Talbert based on his book of the same name.  It stars Paula Patton, Derek Luke, Taye Diggs, Jill Scott, Adam Brody, Djimon Hounsou, Jenifer Lewis, and Ned Beatty.  The film was released on September 27, 2013.  It features Little Mix's debut single, Wings.

Welcome to the Jungle (2013 film): Welcome to the Jungle is a 2013 American comedy film directed by Rob Meltzer, and starring Jean-Claude Van Damme, Adam Brody, Megan Boone, Rob Huebel, Kristen Schaal and Dennis Haysbert.  The film premiered at the 2013 Newport Beach Film Festival.

Question: Adam Brody appeared the 2009 black comedy film written by whom?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "release_year": {
      "type": "integer",
      "description": "The year the film was released."
    },
    "genre": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The genres of the film."
    },
    "writer": {
      "type": "string",
      "description": "The writer of the film."
    },
    "adam_brody_appeared": {
      "type": "boolean",
      "description": "Indicates if Adam Brody appeared in the film."
    }
  },
  "required": [
    "film_title",
    "release_year",
    "genre",
    "writer",
    "adam_brody_appeared"
  ],
  "additionalProperties": false
}

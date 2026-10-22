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
If the Cap Fits: If the Cap Fits is an Irish television sketch show that aired on RTÉ for one series in 1973.  The show was written by and starred Niall Tóibín.

Tom Cruise: Unauthorized: Tom Cruise: Unauthorized is a non-fiction biographical book about Tom Cruise, written by Wensley Clarkson.  The book was published by Hastings House in 1998.  The book discusses Tom Cruise's early life, his rise as an actor, involvement with Scientology, and past relationships with Mimi Rogers and Nicole Kidman.  The book ended during the filming of "Eyes Wide Shut".

The Last Samurai: The Last Samurai is a 2003 American epic period drama war film directed and co-produced by Edward Zwick, who also co-wrote the screenplay with John Logan and Marshall Herskovitz.  The film stars Tom Cruise, who also co-produced, with Timothy Spall, Ken Watanabe, Billy Connolly, Tony Goldwyn, Hiroyuki Sanada, Koyuki, and Shin Koyamada in supporting roles.

Being Tom Cruise: "The Church of Scientology Presents: Being Tom Cruise, Why Scientology Isn't In Any Way Mental" is a satirical spoof documentary from the series "Star Stories", parodying the life of Tom Cruise and his relationship with the Church of Scientology.  It is episode 2 of the second series of "Star Stories", and first aired on Channel 4 on 2 August 2007.  The show recounts Cruise's time with a group of some of his early acting friends.  After filming "Top Gun", Cruise (Kevin Bishop) is introduced to Scientology by John Travolta (Steve Edge), who convinces him to join the organization by smashing Cruise over the head with a shovel.  He meets Nicole Kidman (Dolly Wells) and they start a relationship.  After dating Penélope Cruz, Cruise is introduced to Katie Holmes (Laura Patch) by Travolta.  Holmes agrees to marry Cruise, and the program ends with a voiceover asking the viewer to visit a Scientology website and purchase expensive products.

Days of Thunder: Days of Thunder is a 1990 American sports action drama film released by Paramount Pictures, produced by Don Simpson and Jerry Bruckheimer and directed by Tony Scott.  The cast includes Tom Cruise, Nicole Kidman, Robert Duvall, Randy Quaid, Cary Elwes, Caroline Williams, and Michael Rooker.  The film also features appearances by real life NASCAR racers, such as Rusty Wallace, Neil Bonnett, and Harry Gant.  Commentator Dr. Jerry Punch, of ESPN, has a cameo appearance, as does co-producer Don Simpson.

Bracken (TV series): Bracken is a television soap opera broadcast from 1978 to 1982 on RTÉ One in Ireland, depicting rural life in and around County Wicklow.  Created and written by Wesley Burrowes, it starred Gabriel Byrne and Niall Tóibín.

Nicole Kidman filmography: Australian actress Nicole Kidman made her film debut in the drama remake "Bush Christmas" in 1983.  Four years later, she starred in the television miniseries "Vietnam", for which she received the Best Performance by an Actress in a Mini Series award from the Australian Film Institute.  Kidman's breakthrough role was in the 1989 thriller "Dead Calm"; her performance as a married woman trapped on a yacht with a psychopathic murderer earned critical acclaim and international recognition.  She followed this with her Hollywood debut opposite Tom Cruise in Tony Scott's auto-racing film "Days of Thunder" (1990).  Her role as a homicidal weather forecaster in Gus Van Sant's crime comedy-drama "To Die For" garnered Kidman a Golden Globe Award for Best Actress – Motion Picture Comedy or Musical in 1996.  She worked with Cruise again on Stanley Kubrick's erotic thriller "Eyes Wide Shut" in 1999.

Far and Away: Far and Away is a 1992 American epic romantic adventure drama film directed by Ron Howard from a script by Howard and Bob Dolman.  It stars Tom Cruise and Nicole Kidman.  The cinematographer was Mikael Salomon, and the music score was done by John Williams.  It was screened out of competition at the 1992 Cannes Film Festival.

Niall Tóibín: Niall Tóibín (born 21 November 1929) is an Irish comedian and actor.  Born in Cork into an Irish speaking family, Tóibín grew up on the north-side of the city in Bishop's Field.  He has appeared in "Ryan's Daughter", "Bracken", "The Ballroom of Romance", "The Irish R.M.", "Caught in a Free State", "Ballykissangel", "Far and Away", and "Veronica Guerin", and has played Brendan Behan too.  He was awarded honorary lifetime membership of the Irish Film and Television Academy (IFTA) in 2011.

Time Now Mr T: Time Now Mr T was an Irish television sketch show that aired on RTÉ for one series in 1977.  The show was written by and starred Niall Tóibín.

Question: Niall Tóibín appeared in what 1992 American epic romantic adventure that stars Tom Cruise and NIcole Kidman?

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
    "director": {
      "type": "string",
      "description": "The director of the film."
    },
    "starring_actors": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The main actors starring in the film."
    },
    "niall_toibin_appearance": {
      "type": "boolean",
      "description": "Indicates if Niall T\u00f3ib\u00edn appeared in the film."
    }
  },
  "required": [
    "film_title",
    "release_year",
    "genre",
    "director",
    "starring_actors",
    "niall_toibin_appearance"
  ],
  "additionalProperties": false
}

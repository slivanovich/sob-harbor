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
Year of the Dog (film): Year of the Dog is a 2007 comedy-drama film written and directed by Mike White, and starring Molly Shannon, Laura Dern, Regina King, Thomas McCarthy, Josh Pais, John C. Reilly and Peter Sarsgaard.  The film describes the process of a woman that goes from having one pet dog at home to becoming a vegan and an animal rights activist.

Jurassic Park: Operation Genesis: Jurassic Park: Operation Genesis is a construction and management simulation video game based on the "Jurassic Park" series and released for Windows, Xbox, and PlayStation 2.  The main point of the game is to recreate Jurassic Park - building a five-star theme park with dinosaurs, and turning John Hammond's dream into reality.  In the park, the player builds paths, amenities for visitors such as food, restrooms, enclosures, and attractions.  One must also keep the park safe and secure.  The park can be populated with up to sixty dinosaurs, with twenty-five different species available from the three "Jurassic Park" films.  The player can also add attractions similar to those seen in the films, such as the safari seen in the first "Jurassic Park" film from 1993, and additional attractions such as a balloon tour and several varieties of viewing platform.

Jurassic Park III: Jurassic Park III is a 2001 American science-fiction adventure film and the third installment in the "Jurassic Park" film series.  The film stars Sam Neill, William H. Macy, Téa Leoni, Alessandro Nivola, Trevor Morgan, and Michael Jeter.  It is the first film in the series not to have been directed by Steven Spielberg, nor based on a book by Michael Crichton (though numerous scenes in the film were ultimately taken from Crichton's novels "Jurassic Park" and "The Lost World").  The film takes place on Isla Sorna, off Central America's Pacific coast, the island featured in the , where a divorced couple has tricked Dr. Alan Grant into going in order to help them find their son.

Isla Nublar: Isla Nublar is a fictional Central American island in the "Jurassic Park" franchise, first depicted in Michael Crichton's 1990 novel of the same name.  It is the primary setting of the 1993 film "Jurassic Park" and of "Jurassic World" (2015).  Both the novel and film versions of the Jurassic Park theme park are located on Isla Nublar off the west coast of Costa Rica, which has leased the island to John Hammond, the CEO of bio-engineering firm InGen.

Jurassic Park III: Island Attack: Jurassic Park III: Island Attack (known as Jurassic Park III: Advanced Action in Japan and Jurassic Park III: Dino Attack in Europe; originally known as Jurassic Park III: Primal Fear) is a video game for the Game Boy Advance.  "Island Attack" is loosely based on the 2001 film "Jurassic Park III".

Jurassic World: Fallen Kingdom: Jurassic World: Fallen Kingdom is an upcoming American science fiction adventure film.  It is the sequel to the 2015 film "Jurassic World", the second film in the sequel trilogy and the fifth installment in the "Jurassic Park" film series.  Derek Connolly and "Jurassic World" director Colin Trevorrow both return as writers, with J. A. Bayona as the director.  It will be produced by Frank Marshall, Patrick Crowley and Belén Atienza.  Trevorrow and original "Jurassic Park" director Steven Spielberg are executive producers.

Laura Dern: Laura Elizabeth Dern (born February 10, 1967) is an American actress.  For her performance in the 1991 film "Rambling Rose", she was nominated for the Academy Award for Best Actress, while for her performance in the 2014 film "Wild", she was nominated for the Academy Award for Best Supporting Actress.  Her other film roles include "Mask" (1985), "Smooth Talk" (1985), "Blue Velvet" (1986), "Wild at Heart" (1990), "Jurassic Park" (1993), "Citizen Ruth" (1996), "October Sky" (1999), "I Am Sam" (2001), "Inland Empire" (2006), "The Master" (2012), "The Fault in Our Stars" (2014), and "" (2017).  She is known for her collaborations with filmmaker David Lynch, having appeared in four of his films and the 2017 "Twin Peaks" revival.

List of Jurassic Park characters: The following is a list of fictional characters from Michael Crichton's novel "Jurassic Park", its sequel "The Lost World", and their film adaptations, "Jurassic Park" and "".  Also included are characters from the films "Jurassic Park III", "Jurassic World" and "", which are not adaptations and have no original source novels but contain characters and events based on the fictional universe of Crichton's novels.

Jurassic Park (song): "Jurassic Park" is a parody of Jimmy Webb's single "MacArthur Park" written and performed by "Weird Al" Yankovic; it was released both as a single and as part of Yankovic's "Alapalooza" album in October 1993.  "Jurassic Park" was penned by Yankovic after he remembered the enjoyment he had when he combined a classic rock track with a recent movie topic with his 1985 song "Yoda".  Yankovic decided to combine the plot of the recent movie "Jurassic Park"—a film about a park on a fictional island where geneticists have succeeded in cloning dinosaurs.

Jurassic World: Jurassic World is a 2015 American science-fiction adventure film, the first film in the sequel trilogy and the fourth installment of the "Jurassic Park" series.  The film was directed and co-written by Colin Trevorrow, produced by Frank Marshall and Patrick Crowley, and stars Chris Pratt and Bryce Dallas Howard.  The production companies were Steven Spielberg's Amblin Entertainment, also responsible for the rest of the "Jurassic Park" franchise, and Thomas Tull's Legendary Pictures.  Set 22 years after the events of "Jurassic Park", "Jurassic World" takes place on the same fictional Central American island of Isla Nublar, off the Pacific coast of Costa Rica, where a theme park populated with cloned dinosaurs has operated for ten years.  The park plunges into chaos when a genetically created dinosaur breaks loose and goes on a rampage across the island.

Question: Who starred in both Year of the Dog and Jurassic Park?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The full name of the actor who starred in both films."
    },
    "films_starred_in": {
      "type": "array",
      "description": "A list of the films the actor starred in, as per the question.",
      "items": {
        "type": "string"
      }
    },
    "number_of_films": {
      "type": "integer",
      "description": "The count of films the actor starred in, as per the question."
    }
  },
  "required": [
    "actor_name",
    "films_starred_in",
    "number_of_films"
  ],
  "additionalProperties": false
}

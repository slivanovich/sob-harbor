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
Puss in Boots: The Three Diablos: Puss in Boots: The Three Diablos is a 2012 American computer-animated short comedy film, and a sequel to "Puss in Boots".  It was directed by Raman Hui and features Antonio Banderas as the voice of the title character.  The short was released on February 24, 2012, attached as a bonus feature to the "Puss in Boots" DVD and Blu-ray (3D) release.  The short tells a story of Puss in Boots on a mission to recover a princess' stolen ruby from the notorious French thief the Whisperer.  Reluctantly accompanied by three cute little kittens called the Three Diablos, Puss must tame them before they endanger the mission.

Dawn of the Dragon Racers: Dawn of the Dragon Racers is a 2014 computer-animated short film by DreamWorks Animation and directed by Elaine Bogan and John Sanford.  Based on the film series of the same name.  It was directed by John Sanford and Elaine Bogan, and it features the voices of Jay Baruchel and America Ferrera along with the cast from the television series.  In the short, a hunt for a lost sheep turns into a competition between Hiccup and his friends for the first title of Dragon Racing Champion of Berk.

Another Wild Idea: Another Wild Idea is a 1934 American Pre-Code short comedy science fiction film which was directed by Charley Chase who was also the film's director.  This short comedy movie focuses on a Ray Gun which releases all of a persons inhibitions.

Cornwall Capital: Cornwall Capital is a New York City based private financial investment corporation.  It was founded in 2002 by James Mai, President and Chief Investment Officer, under the guidance of his father, Vincent Mai, who ran the private equity firm AEA Investors, one of the oldest leveraged buyout firms in the United States.  It was profiled in the book "The Big Short" by Michael Lewis as one of a handful of investors in the world that correctly foresaw and profited from the subprime mortgage crisis of 2007.  In addition, James Mai’s investment strategy was portrayed by Jack D. Schwager in the book "Hedge Fund Market Wizards" (2012), an inside analysis of the world's greatest hedge fund experts and the strategies that they implement.  The characters Charlie Geller, Jamie Shipley and Ben Rickert in the film adaptation of The Big Short by John Magaro, Finn Wittrock and Brad Pitt has meant that they are more widely known for their investments running up to the financial crash in 2007-8.

Will Finn: Will Finn (born November 1, 1958) is an American animator, voice actor, and director.  His work in animation includes characters from Disney and Don Bluth films such as "The Secret of NIMH", "Oliver & Company", "The Little Mermaid", "The Rescuers Down Under", and "Pocahontas".  His characters includes Cogsworth in "Beauty and the Beast", Iago in "Aladdin", and Laverne in "The Hunchback of Notre Dame".  Finn wrote and directed "Home on the Range" and did some voice acting the Hollywood Fish in "Chicken Little".  In 2006, Finn directed the computer animated short Hammy's Boomerang Adventure, a spin-off of "Over the Hedge".

Going Spanish: Going Spanish (1934) is an American short comedy film featuring the film debut of Bob Hope and directed by Al Christie.  The short comedy co-stars Leah Ray and Jules Epailly.  Released by Educational Pictures, the film premiered on March 2, 1934, and is also known as Bob's Busy Day (American recut version).

Red's Dream: Red's Dream is a 1987 American computer-animated short film produced by Pixar and directed by John Lasseter.  The short film, which runs four minutes, stars Red, a unicycle.  Propped up in the corner of a bicycle store on a rainy night, Red dreams about a better place.  "Red's Dream" was Pixar's second computer-animated short following "Luxo Jr." in 1986, also directed by Lasseter.

Surviving Sid: Surviving Sid is a 2008 computer-animated short film from Blue Sky Studios, starring Sid the Sloth of "Ice Age" and a cameo appearance by Scrat.  It is the third in the series of "Ice Age" short films, the other two being "Gone Nutty" and "No Time for Nuts".  Unlike the first two "Ice Age" short films, "Surviving Sid" focuses on Sid and a small animal group of camping children.  Directed by Galen Tan Chu and Karen Disher, the short premiered on December 9, 2008, on the "Horton Hears a Who! " DVD and Blu-ray.

Hammy's Boomerang Adventure: Hammy's Boomerang Adventure is a computer-animated short comedy film based on the film "Over the Hedge", which was based on a comic strip of the same name.  It can be found on the movie's DVD or the "Madly Madagascar" DVD as a bonus feature.

La Luna (2011 film): La Luna (IPA: /laˈluna/ [laˈluːna] , Italian for "The Moon") is a 2011 Pixar computer-animated short film, directed and written by Enrico Casarosa.  The short premiered on June 6, 2011 at the Annecy International Animated Film Festival in France, and it was paired with Pixar's "Brave" for its theatrical release on June 22, 2012, being shown before the film's beginning.  "La Luna" was released on November 13, 2012, on the "Brave" DVD and Blu-ray, and on a new "Pixar Short Films Collection, Volume 2", the second collection of Pixar's short films.  "La Luna" was nominated for an Academy Award for Best Animated Short Film at the 84th Academy Awards.

Question: When was the computer-animated short comedy film based on the film "Over the Hedge" by Will Finn directed?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the short film."
    },
    "director": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the director."
        }
      },
      "required": [
        "name"
      ],
      "additionalProperties": false
    },
    "directed_year": {
      "type": "integer",
      "description": "The year the film was directed."
    },
    "film_type": {
      "type": "string",
      "description": "The type of film (e.g., computer-animated short comedy film)."
    },
    "based_on_film": {
      "type": "string",
      "description": "The title of the film it is based on."
    }
  },
  "required": [
    "film_title",
    "director",
    "directed_year",
    "film_type",
    "based_on_film"
  ],
  "additionalProperties": false
}

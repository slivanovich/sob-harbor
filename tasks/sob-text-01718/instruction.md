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
Mud (2012 film): Mud is a 2012 American coming-of-age drama film written and directed by Jeff Nichols.  The film stars Matthew McConaughey, Tye Sheridan, Jacob Lofland, Sam Shepard, and Reese Witherspoon.  The film competed for the Palme d'Or at the 2012 Cannes Film Festival.  It was shown at the Sundance Film Festival in January 2013.  The film opened on April 26, 2013 with a limited release in select theaters, before having a wide release on May 10, 2013.  It performed well at the box office, grossing $32.6 million on a $10 million budget and received critical acclaim.

A Time to Kill (1996 film): A Time to Kill is a 1996 American crime drama film based on John Grisham's 1989 novel of the same name, directed by Joel Schumacher.  Sandra Bullock, Samuel L. Jackson, Matthew McConaughey, and Kevin Spacey star, with Oliver Platt, Ashley Judd, Kiefer and Donald Sutherland, and Patrick McGoohan appearing in supporting roles.  Set in Canton, Mississippi, the film involves the rape of a young girl, the arrest of the rapists, their subsequent murder by the girl's father, and the father's trial for murder.  The film was a critical and commercial success, making $152 million at the worldwide box office.

Carlos (miniseries): Carlos, also known as Carlos the Jackal, is a 2010 French-German biographical film/miniseries about the life of the 1970s Venezuelan revolutionary Carlos the Jackal (Ilich Ramírez Sánchez), covering his first series of attacks in 1973 until his arrest in 1994.  It premiered as a three-part TV mini-series on French pay channel Canal+, with the three parts airing on 19 May, May 26, and June 2, 2010.  On the same day it premiered on Canal+, the full 5½ hour version was also shown out of competition at the 2010 Cannes Film Festival.

Matthew McConaughey filmography: Matthew McConaughey is an American actor who made his breakthrough by starring in the Richard Linklater-directed coming of age comedy "Dazed and Confused" in 1993.  His first lead role was in the 1996 film adaptation of the John Grisham novel "A Time to Kill".  The following year, McConaughey played the lawyer Roger Sherman Baldwin opposite Morgan Freeman and Anthony Hopkins in the Steven Spielberg-directed historical drama "Amistad", and also starred opposite Jodie Foster in the Robert Zemeckis-directed science fiction drama "Contact".  In 1998, he appeared in the Linklater-directed comedy-drama "The Newton Boys".  During the 2000s, McConaughey was typecast as a romantic comedy lead in the films "The Wedding Planner" (2001), "How to Lose a Guy in 10 Days" (2003), "Failure to Launch" (2006), and "Ghosts of Girlfriends Past" (2009).

Gold (2016 film): Gold is a 2016 American crime drama film directed by Stephen Gaghan and written by Patrick Massett and John Zinman.  The film stars Matthew McConaughey, Édgar Ramírez, Bryce Dallas Howard, Corey Stoll, Toby Kebbell, Craig T. Nelson, Stacy Keach and Bruce Greenwood.  The film is loosely based on the true story of the 1993 Bre-X mining scandal, when a massive gold deposit was supposedly discovered in the jungles of Indonesia; however, for legal reasons and to enhance the appeal of the film, character names and story details were changed.

Too Much Pussy!: Too Much Pussy!  is a 2010 French-German documentary film directed by Émilie Jouvet.  It follows a group of performers who are all members the sex-positive movement during the tour of their "Queer X Show" through Europe, from Berlin to Malmö.  The group consists of the writer and actress Wendy Delorme, the DJ Metzgerei, the adult actress Judy Minx, the singer Mad Kate, the artist and performer Sadie Lune, and the adult actress and director Madison Young.

Sandra Bullock filmography: Sandra Bullock is an American actress who made her film debut with a minor role in the 1987 thriller "Hangmen".  She made her television debut in the television film "Bionic Showdown: The Six Million Dollar Man and the Bionic Woman" (1989) and played the lead role in the short-lived sitcom "Working Girl" (1990) before making her breakthrough starring in the action film "Speed" (1994).  She starred with Sylvester Stallone in "Demolition Man" (1994).  Bullock founded her own production company, Fortis Films, and starred in the romantic comedy "While You Were Sleeping" in 1995.  Her performance in the film earned her first nomination for the Golden Globe Award for Best Actress – Motion Picture Comedy or Musical.  The following year, Bullock starred with Matthew McConaughey in the film adaptation of John Grisham's novel "A Time to Kill" (1996).  In 1997, she reprised her "Speed" role in the sequel, "".  The following year, Bullock starred in the romantic comedy "Practical Magic", voiced Miriam in the animated biblical film "The Prince of Egypt" and also executive produced her first film, the romantic drama "Hope Floats".

Alexie Gilmore: Alexie Gilmore (born December 11, 1976) is an American actress who starred in the television series "New Amsterdam" as Dr. Sara Dillane.  She is featured in the 2008 movie "Definitely, Maybe" and starred alongside Matthew McConaughey in the 2008 movie "Surfer, Dude".  Alexie also played the part of Kelly in the 2013 film "Willow Creek (film)" starring "Bryce Johnson" and directed by "Bobcat Goldthwait".  She played Devon Atwood in three episodes of "" as "Elijah Mundo" wife.  Alexie's other credits include "90210", "Legends" with "Sean Bean" and many others.

The Wolf of Wall Street (2013 film): The Wolf of Wall Street is a 2013 American biographical black comedy crime film directed by Martin Scorsese and written by Terence Winter, based on the memoir of the same name by Jordan Belfort.  It recounts Belfort's perspective on his career as a stockbroker in New York City and how his firm Stratton Oakmont engaged in rampant corruption and fraud on Wall Street that ultimately led to his downfall.  Leonardo DiCaprio (who was also a producer) stars as Belfort, with Jonah Hill as his business partner and friend Donnie Azoff, Margot Robbie as his wife Naomi Lapaglia and Kyle Chandler as Patrick Denham, the FBI agent who tries to bring him down.  Matthew McConaughey, Rob Reiner, Jon Favreau, Joanna Lumley and Jean Dujardin also star.  The film marks the director's fifth collaboration with DiCaprio, after "Gangs of New York" (2002), "The Aviator" (2004), "The Departed" (2006) and "Shutter Island" (2010), as well as his second collaboration with Winter after the television series "Boardwalk Empire" (2010–14).

Édgar Ramírez: Édgar Ramírez Arellano (] , born March 25, 1977) is a Venezuelan actor and former journalist.  He played Carlos the Jackal in the 2010 French-German biopic series of the same name, a role for which he won the César Award for Most Promising Actor at the César Awards 2011, and was nominated for a Golden Globe and Emmy Award for best actor.

Question: The actor that played Carlos the Jackal in the 2010 French-German biopic series of the same name also starred with Matthew McConaughey in a 2016 Ameican drama film by what director?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_who_played_carlos": {
      "type": "string",
      "description": "The name of the actor who played Carlos the Jackal."
    },
    "film_title": {
      "type": "string",
      "description": "The title of the film where the actor and Matthew McConaughey starred together."
    },
    "film_year": {
      "type": "integer",
      "description": "The release year of the film."
    },
    "film_genre": {
      "type": "string",
      "description": "The genre of the film."
    },
    "director_of_film": {
      "type": "string",
      "description": "The director of the specified film."
    },
    "other_co_stars": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Other notable co-stars in the film."
    }
  },
  "required": [
    "actor_who_played_carlos",
    "film_title",
    "film_year",
    "film_genre",
    "director_of_film",
    "other_co_stars"
  ],
  "additionalProperties": false
}

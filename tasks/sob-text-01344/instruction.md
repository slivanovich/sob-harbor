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
Star Wars Battle Pod: Star Wars Battle Pod is a 2014 arcade game based on the franchise "Star Wars".  It was unveiled at the New York Comic-Con on October 8, 2014.  The game consists of multiple scenarios that correspond with one of the major battles in the original trilogy.  There are five scenarios, the Battle of Yavin (Yavin) from "Star Wars" where the player is placed in an X-wing attacking the Death Star to prevent it from destroying Yavin 4, the Battle of Hoth (Hoth), from "The Empire Strikes Back", where one pilots a snowspeeder to assist in the evacuation of Hoth from invading Imperial forces, a speeder run through Endor (Endor) where one helps Han Solo make it to the shield generator to destroy the Death Star's shield for the rebels in space.  and the Battle of Endor (Death Star II) from "Return of the Jedi", which places the player in the cockpit of the "Millennium Falcon" to try to destroy the Death Star II and end the war.  There is one scenario that doesn't follow the storyline of the movies but sets its own path, (Vader's Revenge).  This scenario takes place literally seconds after the destruction of the first Death Star where one plays as Darth Vader who is trying to prevent the rebels from escaping with a piece of the Death Star with the ability to eliminate Han Solo in the process.  Another version of the game adds a scene from "The Force Awakens", where the player pilots a T-60 X-Wing to engage First Order ships on Takodana and protect General Leia's transport.

Kylo Ren: Kylo Ren is a fictional character in the "Star Wars" franchise.  Introduced in the 2015 film "", he is portrayed by Adam Driver.  Kylo Ren is the chosen name of Ben Solo, the son of original "Star Wars" trilogy characters Han Solo and Leia Organa.  Though trained by his uncle Luke Skywalker as a Jedi, he has been seduced to the dark side of the Force by Supreme Leader Snoke, and aspires to be as powerful as his grandfather, Darth Vader.  Kylo Ren is also the master of the Knights of Ren, and a commander for the First Order, an organization spawned from the fallen Galactic Empire.  He is featured in "The Force Awakens" media and merchandising, and will appear in the film's forthcoming sequel, "" (2017).

John Boyega: John Adedayo B. Adegboyega (born 17 March 1992), known professionally as John Boyega, is an English actor and producer best known for playing Finn in the 2015 film "", the seventh film of the "Star Wars" series.  Boyega rose to prominence in his native United Kingdom for his role as Moses in the 2011 sci-fi comedy film "Attack the Block".

Solo family: The Solo family is a fictional family of characters in the "Star Wars" franchise.  Introduced in the 1977 film "Star Wars", smuggler Han Solo is initially a morally ambiguous character but evolves into one of the heroes of the film.  He is also a major character in the sequels "The Empire Strikes Back" (1980), "Return of the Jedi" (1983) and "" (2015).  In "The Force Awakens", Han and Princess Leia have a son named Ben Solo.

Star Wars: The Force Awakens: Star Wars: The Force Awakens (also known as Star Wars: Episode VII – The Force Awakens) is a 2015 American epic space opera film co-written, co-produced and directed by J. J. Abrams.  The sequel to 1983's "Return of the Jedi", "The Force Awakens" is the first installment of the "Star Wars" sequel trilogy.  It stars Harrison Ford, Mark Hamill, Carrie Fisher, Adam Driver, Daisy Ridley, John Boyega, Oscar Isaac, Lupita Nyong'o, Andy Serkis, Domhnall Gleeson, Anthony Daniels, Peter Mayhew, and Max von Sydow.  Produced by Lucasfilm Ltd. and Abrams' production company Bad Robot Productions and distributed worldwide by Walt Disney Studios Motion Pictures, "The Force Awakens" was the first "Star Wars" film not produced by franchise creator George Lucas.  Set 30 years after "Return of the Jedi", it follows Rey, Finn and Poe Dameron's search for Luke Skywalker and their fight alongside the Resistance, led by veterans of the Rebel Alliance, against Kylo Ren and the First Order, a successor to the Galactic Empire.

Star Wars: Poe Dameron: Star Wars: Poe Dameron is an ongoing "Star Wars" comic book series which centers on Poe Dameron, the Resistance X-wing fighter pilot introduced in the 2015 film "".  The series is written by Charles Soule and was first illustrated by Phil Noto, and later Angel Unzueta.  It is set immediately before "The Force Awakens".  Published by Marvel Comics, "Poe Dameron" debuted on April 6, 2016.

Journey to Star Wars: "Journey to "Star Wars" is a Disney/Lucasfilm publishing initiative that connects the "Star Wars" sequel films with previous film installments in the franchise.  It currently includes the initiatives "Journey to "Star Wars: The Force Awakens" and "Journey to "Star Wars: The Last Jedi"".  All titles under the program are canonical to the "Star Wars" universe.

Poe Dameron: Poe Dameron is a fictional character in the "Star Wars" franchise.  Introduced in the 2015 film "", he is portrayed by Oscar Isaac.  Poe is an X-wing fighter pilot for the Resistance who inadvertently brings renegade stormtrooper Finn (John Boyega) and Jakku scavenger Rey (Daisy Ridley) into the fight against—and eventually a victory over—the sinister First Order.  He is featured in "The Force Awakens" media and merchandising as well as , and will appear in the film's forthcoming sequel, "".  Isaac and the character have received positive reviews, with Poe being compared to the characterization of Han Solo (Harrison Ford) in the original "Star Wars" film trilogy.

Lego Star Wars: The Force Awakens: Lego Star Wars: The Force Awakens is a Lego-themed action-adventure video game developed by TT Fusion, based on the film "".  It is the fifth entry in TT Games' "Lego Star Wars" series.  Under license from Lucasfilm, the game was released by Warner Bros.  Interactive Entertainment for iOS, Microsoft Windows, PlayStation 3, PlayStation 4, Xbox 360, Xbox One, Nintendo 3DS, PlayStation Vita, Nvidia Shield and Wii U, on 28 June 2016, and for Android on 27 July 2016.  The game was ported and released by Feral Interactive for OS X on 30 June 2016.

Captain Phasma: Captain Phasma is a fictional character in the "Star Wars" franchise, portrayed by Gwendoline Christie.  Introduced in "" (2015), the first film in the "Star Wars" sequel trilogy, Phasma is the commander of the First Order's force of stormtroopers. Christie confirmed that the character would reappear in the next of the trilogy's films, "".  The character also made an additional appearance in "Before the Awakening", an anthology book set before the events of "The Force Awakens".

Question: What is the birth date of this English actor and producer, who starred in Star Wars: The Force Awakens?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the actor."
    },
    "nationality": {
      "type": "string",
      "description": "The nationality of the actor."
    },
    "profession": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The professions of the individual."
    },
    "birth_date": {
      "type": "string",
      "description": "The birth date of the actor in 'DD Month YYYY' format."
    },
    "starred_in_movie": {
      "type": "string",
      "description": "The title of the movie the actor starred in."
    }
  },
  "required": [
    "actor_name",
    "nationality",
    "profession",
    "birth_date",
    "starred_in_movie"
  ],
  "additionalProperties": false
}

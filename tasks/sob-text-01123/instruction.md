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
Skeksis: The Skeksis are a fictional species which act as the main antagonists in the 1982 fantasy film "The Dark Crystal", its companion book "The World of The Dark Crystal" and the Tokyopop prequel "Legends of the Dark Crystal".  They are also referenced as an alien race in S03E07 of Farscape and are strikingly similar in appearance to the Halosians in S02E09 of the same show, which was produced by Jim Henson Productions.  The word "Skeksis" serves as both singular and plural form for this species, with the singular being pronounced and the plural .  They are described by concept artist Brian Froud as, "part reptile, part predatory bird, part dragon."  In the film, the Skeksis are represented by puppets engineered under the direction of Jim Henson.  Jim Henson said that in the development of the Skeksis, the creators drew inspiration from the Seven Deadly Sins.

Gonzo (Muppet): Developed and performed by Dave Goelz, Gonzo made his first appearance in the 1970 special "The Great Santa Claus Switch", as the "Cigar Box Frackle".  Originally a minor figure in "The Muppet Show", he soon evolved into one of the franchise's primary characters.  Gonzo has appeared in every Muppet film, including "The Muppet Christmas Carol", where he portrayed author Charles Dickens and developed a double act with Rizzo the Rat.

Bunsen Honeydew: Dr. Bunsen Honeydew is a Muppet character from "The Muppet Show", performed by Dave Goelz.  He is a bald, green-skinned, bespectacled, lab-coated scientist who would do periodic science segments from "Muppet Labs, where the future is being made today."  The character has no eyes, only completely transparent, lensless glasses, giving the appearance of a stereotypical absent-minded intellectual.  His first name is derived from Robert Bunsen, after whom the Bunsen Burner was named.  His last name is a reference to the honeydew melon, which his head is virtually shaped like.  It is also a reference to Honeywell Labs, a technology company which aired TV commercials (""That someday is today ... at Honeywell"") well-known at the time of the original Muppet Show.

Characters and races of The Dark Crystal: The characters and races of "The Dark Crystal" were created by puppeteer Jim Henson and concept artist Brian Froud for the 1982 cult fantasy film "The Dark Crystal" and its expanded universe in books, comics, artwork, games, and proposed sequel.  Notably, most of the information about specific character and race names comes from supplementary material such as Froud's book "The World of the Dark Crystal", rather than the film itself.

The Dark Crystal (video game): The Dark Crystal is a graphic adventure computer game based on Jim Henson's fantasy film, "The Dark Crystal".  The game was designed by Roberta Williams and published under the SierraVenture line in 1983 as "Hi-Res Adventure #6: The Dark Crystal".  It was the first Hi-Res Adventure released under the SierraVenture line, the previous titles being released under earlier names and later re-released under SierraVenture.

The Dark Crystal: The Dark Crystal is a 1982 American–British fantasy adventure film directed by Jim Henson and Frank Oz and stars the voices of Stephen Garlick, Lisa Maxwell, Billie Whitelaw, Percy Edwards, and Barry Dennen.  The plot revolves around Jen, an elf-like 'Gelfling' on a quest to restore balance to his alien world by returning a lost shard to a powerful but broken gem.

Toby Philpott: Toby Philpott is an English puppeteer best known for his work in motion picture animatronics during the 1980s in such films as "The Dark Crystal" and "Return of the Jedi".  Born into a family of entertainers, Philpott dropped out of school and traveled the world during the 1960s, squatting in various locations and surviving off money he earned from his work as a street performer, which included juggling, fire eating, magic shows, clowning and acrobatics.  He began his film career after Jim Henson personally selected Philpott to work on the 1982 fantasy film "The Dark Crystal", in which he worked side-by-side with Henson.

The Muppets (film): The Muppets is a 2011 American musical comedy film and the seventh theatrical film featuring the Muppets.  The film is directed by James Bobin, written by Jason Segel and Nicholas Stoller, produced by David Hoberman and Todd Lieberman, and stars Segel, Amy Adams, Chris Cooper and Rashida Jones, as well as Muppet performers Steve Whitmire, Eric Jacobson, Dave Goelz, Bill Barretta, David Rudman, Matt Vogel, and Peter Linz.  Bret McKenzie served as music supervisor, writing four of the film's five original songs, and Christophe Beck composed the film's score.  In "The Muppets", devoted fan Walter, his brother Gary, and Gary's girlfriend Mary help Kermit the Frog reunite the disbanded Muppets, as they must raise $10 million to save the Muppet Theater from Tex Richman, a businessman who plans to demolish the studio to drill for oil.

Dave Goelz: David Charles "Dave" Goelz (born July 16, 1946) is an American puppeteer and voice actor known for his work with the Muppets.  As part of the Muppets' performing cast, Goelz performs The Great Gonzo, as well as Bunsen Honeydew, Waldorf (after Jim Henson's death), Zoot and Beauregard, originating on "The Muppet Show".  Goelz's puppeteering roles also include roles in "Fraggle Rock", "The Dark Crystal", and "Labyrinth".  Outside of puppeteering work, he is also the voice of Figment in the Journey into Imagination with Figment attraction at Epcot.

Muppets Most Wanted: Muppets Most Wanted is a 2014 American musical comedy film and the eighth theatrical film featuring the Muppets.  Directed by James Bobin and written by Bobin and Nicholas Stoller, the film is a sequel to 2011's "The Muppets" and stars Ricky Gervais, Ty Burrell, and Tina Fey, as well as Muppet performers Steve Whitmire, Eric Jacobson, Dave Goelz, Bill Barretta, David Rudman, Matt Vogel, and Peter Linz.  In the film, the Muppets find themselves unwittingly involved in an international crime caper while on tour in Europe.

Question: In addition to his puppeteering on The Dark Crystal, Dave Goelz is known for performing as which Muppet?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "puppeteer_name": {
      "type": "string",
      "description": "The name of the puppeteer."
    },
    "known_for_film": {
      "type": "string",
      "description": "The film for which the puppeteer's work is mentioned in the context."
    },
    "muppet_character_performed": {
      "type": "string",
      "description": "The name of a Muppet character performed by the puppeteer, in addition to their work on the specified film."
    }
  },
  "required": [
    "puppeteer_name",
    "known_for_film",
    "muppet_character_performed"
  ],
  "additionalProperties": false
}

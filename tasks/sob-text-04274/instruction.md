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
Dido (singer): Dido Florian Cloud de Bounevialle O'Malley Armstrong, known as Dido ( , born 25 December 1971), is an English singer and songwriter.  Dido attained international success with her debut album "No Angel" (1999).  It sold over 21 million copies worldwide, and won several awards, including the MTV Europe Music Award for Best New Act, two NRJ Awards for Best New Act and Best Album, and two Brit Awards for Best British Female and Best Album.  Her next album, "Life for Rent" (2003), continued her success with the hit singles "White Flag" and "Life for Rent".

Lil Wayne albums discography: American rapper Lil Wayne has released eleven studio albums, one collaborative album, three compilation albums, one extended play, and twenty mixtapes. Wayne made his album debut in 1999, with "Tha Block Is Hot", which was certified platinum by the Recording Industry Association of America.  His later albums, "Lights Out" released in 2000, and "500 Degreez", released in 2002, attracted minor attention.  In 2004, he released the first of his infamous "Carter" series, with "Tha Carter".  In 2005, "Tha Carter II" was released.  In 2006, Wayne released a collaborative album with rapper Birdman, titled "Like Father, Like Son".  In 2008, Wayne released his best-selling album so far, titled "Tha Carter III".  Certified triple platinum by the RIAA, "Tha Carter III" won the Best Rap Album award at the 2009 Grammy Awards.  Lil Wayne founded record label Young Money Entertainment and released a collaborative album featuring rappers signed to the label, "We Are Young Money", in 2009, followed by his debut rock music album "Rebirth" in 2010.  While serving an 8-month prison sentence in New York he released another album entitled "I Am Not a Human Being", in September 2010.  The latest addition to "Tha Carter" series, "Tha Carter IV", was released on August 29, 2011.  In 2013, Wayne released a sequel to his 2010 album "I Am Not a Human Being", titled "I Am Not a Human Being II", followed by two compilation albums with his labels, "Rich Gang (2013)", and " (2014)".

Rhythms del Mundo Classics: Rhythms del Mundo Classics is the follow-up album to the internationally successful album "Rhythms del Mundo", with the Buena Vista Social Club appearing with artists including The Killers, Amy Winehouse, Keane, Jack Johnson, The Rolling Stones, KT Tunstall and Rodrigo y Gabriela.

Julie Atherton: Julie Atherton is a British actress, who is best known for her work on stage.  On 3 October 2009 she finished playing the roles of Kate Monster and Lucy the Slut in the West End production of "Avenue Q".  She released her debut album, "A Girl of Few Words," on 2 October 2006.  After signing with the Speckulation record label, she released her second album titled "No Space for Air" in the Summer of 2010.  She starred as Sister Mary Robert in the first UK tour of "Sister Act: The Musical" in 2011.  In 2013 she was featured as 'French Teacher' in the world premiere of the musical 'LIFT' by Craig Adams and Ian Watson, at the Soho Theatre.  This was followed in 2014 by the title role in 'Thérèse Raquin', again by Craig Adams with Book and Lyrics by Nona Shepphard.  After a sold out run at The Finborough Theatre the production transferred to Park Theatre in Finsbury Park.  Julie wrapped up a stellar year in 2014 with the release of her third album titled 'Rush of Life', with songs written for her by Craig Adams, Dougal Irvine, Lance Horne, George Maguire and Benedict.

Ciudad Mitad del Mundo: The Ciudad Mitad del Mundo (] , "Middle of the World City") is a tract of land owned by the prefecture of the province of Pichincha, Ecuador.  It is located at San Antoñio parish of the canton of Quito, 26 km north of the center of Quito.  The grounds contain the Monument to the Equator, which highlights the exact location of the Equator (from which the country takes its name) and commemorates the eighteenth century Franco-Spanish Geodesic Mission which fixed its approximate location; they also contain the Museo Etnográfico Mitad del Mundo, a museum about the indigenous ethnography of Ecuador.

Better Together (song): Better Together is a song written and performed by Jack Johnson.  As well as being the first track on Johnson's album "In Between Dreams", which was released in February 2005, "Better Together" was released as a single in January 2006.  It charted at #24 in the United Kingdom.  In the United States, a live version from the "En Concert" live album was released as a single in 2009, peaking at #23 on the Mediabase Triple A chart.  It was also included in a Cuban remix of the song which was included in Rhythms del Mundo.  An edited version of Better Together featuring a ukulele was included in the album, The Mango Tree.

La última noche del mundo: La última noche del mundo (Spanish for "the last night of the world") is the debut album by Mexican post-rock band Austin TV.

Emigrante del Mundo (song): "Emigrante del Mundo" is the debut single of Lucenzo.  It was released in France initially in 2007 and a second time in 2010 after the success of the kuduro music promoted by Lucenzo's new hits.  It also appears in the debut album of Lucenzo of the same title "Emigrante del Mundo".

Rhythms del Mundo: Rhythms del Mundo is a nonprofit collaborative album, which fuses an all-star cast of Cuban musicians including Ibrahim Ferrer and Omara Portuondo of the Buena Vista Social Club with tracks from US, UK and Irish artists such as Dido, Arctic Monkeys, U2, Coldplay, Sting, Jack Johnson, Maroon 5, Franz Ferdinand, Kaiser Chiefs and others.  A follow-up album, Rhythms del Mundo Classics, was released in 2009.

Guillotine IV (The Final Chapter): 'Guillotine IV (The Final Chapter)' is the second single from Falling in Reverse's third album "Just Like You".  It is the fourth and final installment of the Guillotine series, which was started by Escape the Fate when former lead singer Ronnie Radke was in the band.  The first song titled 'The Guillotine' was in Escape the Fate's debut album Dying Is Your Latest Fashion in 2006.  The second song which was titled 'This War Is Ours (The Guillotine II)' was on Escape the Fate's second studio album This War Is Ours in 2008.  The third song which was titled 'The Aftermath (The Guillotine III)' was on Escape the Fate's third self-titled album in 2010.  Then finally in 2015 Falling in Reverse finished the series with ""Guillotine IV (The Final Chapter).

Question: What is the stage name of the arist with a debut album titled 'No Angel' that also appeared on the 'Rhythms del Mundo' collaborative album?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "artist_stage_name": {
      "type": "string",
      "description": "The stage name of the artist."
    },
    "debut_album": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the artist's debut album."
        },
        "release_year": {
          "type": "integer",
          "description": "The release year of the debut album."
        }
      },
      "required": [
        "title",
        "release_year"
      ],
      "additionalProperties": false
    },
    "collaborative_album": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the collaborative album the artist appeared on."
        },
        "artist_contribution_confirmed": {
          "type": "boolean",
          "description": "Indicates if the artist's contribution to the collaborative album is confirmed."
        }
      },
      "required": [
        "title",
        "artist_contribution_confirmed"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "artist_stage_name",
    "debut_album",
    "collaborative_album"
  ],
  "additionalProperties": false
}

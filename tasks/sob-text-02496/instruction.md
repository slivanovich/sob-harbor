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
15 (film): 15 is a 2003 Singaporean coming of age dark comedy-drama film about teenage gangsters in the Singapore suburbs.  Directed by Royston Tan, the film is an expanded version of Tan's 2002 award-winning short film, also titled "15".  It is one of the few Singaporean films to feature brief full-frontal male nudity, together with the Singaporean-Thai film "Pleasure Factory" and the Singaporean-Hong Kong film "Bugis Street".

Lee Sung-jae: Lee Sung-jae (born August 23, 1970) is a South Korean actor.  Among his notable works include the films "Art Museum by the Zoo", "Attack the Gas Station", "Barking Dogs Never Bite", and "Kick the Moon", as well as the television series "Lie" and "A Wife's Credentials".

Ice Rain: Ice Rain () is a 2004 South Korean romance drama film starring Lee Sung-jae, Song Seung-heon and Kim Ha-neul.  Co-written and directed by first-time director Kim Eun-sook, it tells the story of two mountaineers stranded on a climb to Mount Asiaq in Alaska.  While waiting out the storm, they share stories of the women that changed their lives, not knowing how closely connected they actually are.

Wiener-Dog (film): Wiener-Dog is a 2016 American dark comedy-drama film directed and written by Todd Solondz.  Starring an ensemble cast led by Ellen Burstyn, Kieran Culkin, Julie Delpy, Danny DeVito, Greta Gerwig, Tracy Letts, and Zosia Mamet, the film serves as a spin-off from Solondz's 1995 film "Welcome to the Dollhouse", which also features the character of Dawn Wiener.

Dance with the Wind: Dance with the Wind (Korean: 바람의 전설 ; "Baramui jeonseol") is a 2004 South Korean film starring Lee Sung-jae and Park Sol-mi, and is the directorial debut of Park Jung-woo.  The story is adapted from a 1999 book by novelist Ji Seong-sa.

Stan Bush: Stan Bush is an American singer-songwriter and musician whose most notable works include the songs "The Touch" and "Dare" from the soundtrack to the 1986 animated film "", "Hearts vs. Heads" from the soundtrack to the 1986 action/supernatural film "The Wraith", and "She's Got the Power", featured in the American voice dub of the animated series "Sailor Moon".  He also had one track on the children's album "Take My Hand – Songs from the 100 Acre Wood" entitled "That's What Tiggers Do Best," released in 1995.  Other notable works include the songs "Never Surrender," "Streets of Siam," and "Fight for Love" from the movie "Kickboxer", and "Fight to Survive" and "On My Own – Alone", the theme from "Bloodsport".  In 1987, Bush (and back-up band Barrage) wrote and recorded the ballad "Love Don't Lie", which became a minor MTV hit when covered a year later by House of Lords.

Ghost in Love: Ghost in Love (; aka Suicide Ghost Club) is a 1999 South Korean film written by Li Hong-zhou and directed by Lee Kwang-hoon.  The film stars Kim Hee-sun in the title role as the girlfriend of a man she suspects of cheating on her.  She throws herself underneath an oncoming train (with some help from nearby ghosts), and discovers that in the afterlife she can roam as a ghost and take revenge, if she wants to, on her former boyfriend, who has quickly moved on.  Lee Sung-jae also stars as Kantorates, a ghost who befriends the protagonist.  The film was released on August 14, 1999.

Wonderful World (2009 film): Wonderful World is a 2009 dark comedy-drama film directed and written by Joshua Goldin, who in this movie makes his directorial debut.  The film stars Matthew Broderick, Sanaa Lathan, Michael K. Williams and Jodelle Ferland.

Daisy (2006 film): Daisy () is a 2006 film directed by Hong Kong filmmaker Andrew Lau of the "Infernal Affairs" trilogy.  "Daisy" is an urban romantic melodrama involving young painter Hye-young (Jun Ji-hyun), Interpol detective Jeong Woo (Lee Sung-jae), and professional hitman Park Yi (Jung Woo-sung).

Barking Dogs Never Bite: Barking Dogs Never Bite (Korean: 플란다스의 개 , also known as "A Higher Animal" and "Dog of Flanders") is a 2000 South Korean dark comedy-drama film.  The film's original Korean title is a satirical take on "A Dog of Flanders", a European pet story that is very popular in parts of East Asia.  It is also the directorial debut of Bong Joon-ho, who would later go on to direct "Memories of Murder" in 2003, "The Host" in 2006, and "Snowpiercer" in 2013.

Question: Lee Sung-jae's notable works include a dark comedy-drama film that was the directorial debut of who?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film."
        },
        "genre": {
          "type": "string",
          "description": "The genre of the film."
        },
        "is_directorial_debut": {
          "type": "boolean",
          "description": "Indicates if the film was a directorial debut."
        }
      },
      "required": [
        "title",
        "genre",
        "is_directorial_debut"
      ],
      "additionalProperties": false
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
    "actor_involved": {
      "type": "string",
      "description": "The name of the actor whose notable works include this film."
    }
  },
  "required": [
    "film",
    "director",
    "actor_involved"
  ],
  "additionalProperties": false
}

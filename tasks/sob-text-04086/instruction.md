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
Bodies (TV series): Bodies is a British television medical drama produced by Hat Trick Productions for the BBC.  Created by Jed Mercurio, the series first broadcast on 23 June 2004, and is based on Mercurio's book of the same name.  The series is centred on specialist registrar Rob Lake (Max Beesley), who starts in a new post in the Obstetrics and gynaecology department at the fictional South Central Infirmary, under the guidance of consultant obstetrician Roger Hurley (Patrick Baladi).  Nicholas Palliser reprises his part as Hospital Manager Paul Tennant from "Cardiac Arrest".

Jane Wymark: Jane Wymark (born 31 October 1952) is an English actress.  The daughter of English actor Patrick Wymark (1926–1970) and the American writer and playwright Olwen Wymark, she is best known for playing Morwenna Chynoweth Whitworth (Morwenna Carne by the close of the series) in the 1970s BBC television period drama "Poldark" (1977), and more recently as Joyce Barnaby (1997–2011) in the ITV detective series "Midsomer Murders".  She has appeared in UK television dramas such as "The Bass Player and the Blonde", "A Touch of Frost", "Dangerfield", "Lovejoy" and "Pie in the Sky".  She also appeared as Jill Mason in the Birmingham Rep production of "Equus".

The Gray Man (2007 film): The Gray Man (previously known as Wisteria: The Horrible Story of Albert Fish) is a 2007 biographical thriller film based on the actual life and events of American serial killer, rapist and cannibal Albert Fish.  It premiered at the Montreal World Film Festival on August 31, 2007, and was scheduled for a theatrical release sometime in 2007.  It is directed by Scott Flynn and stars Belgian actor Patrick Bauchau as Albert Fish.

Sarah Woodward: Sarah Woodward (born 3 April 1963) is a British actress.  She won the Olivier Award for best performance in a supporting role in 1998 for her role in "Tom & Clem" by Stephen Churchett. , directed by Richard Wilson, and was nominated for a Tony Award in 2000 for her role in the Donmar Warehouse production of Tom Stoppard's "The Real Thing".  opposite Jennifer Ehle and Stephen Dillane, directed by David Levaux.  She is the daughter of actor Edward Woodward and his first wife, actress Venetia Barrett, and the sister of actor Tim Woodward, actor and screenwriter Peter Woodward, and actress Emily Woodward, whose mother is actress Michele Dotrice.  She is married to actor Patrick Toomey.  They have two daughters and live in London.

Patrick Baladi: Patrick Bashir Baladi (born 25 December 1971 in Sutton Coldfield, Warwickshire) is an English actor.  He is best known for playing Neil Godwin in the BBC Sitcom "The Office", Michael Jackson in the Sky 1 drama "Stella" and Stephen Holmes in the ITV thriller "Marcella".

Marcella (TV series): Marcella is a British crime noir detective series produced, written and directed by Hans Rosenfeldt, a Swedish screenwriter and creator of the series "The Bridge" (adapted as "The Tunnel" for British audiences).  The series began airing on ITV from 4 April 2016.  Episodes are available on Netflix worldwide outside the UK and Ireland after it airs on ITV.  On 26 August 2016, ITV announced that a second series had been commissioned, scheduled to premiere in 2017, with Hans Rosenfeldt and Anna Friel returning.

Worm Miller: Joshua "Worm" Miller (born September 23, 1978) is an American writer, director, and actor.  He is best known for directing "Hey, Stop Stabbing Me! " and creating the animated television series "Golan the Insatiable" for Fox's Animation Domination HD programming block.  He often collaborates with writer/actor Patrick Casey.  On December 1, 2010 his first book, "A Zombie's History of the United States: From the Massacre at Plymouth Rock to the CIA's Secret War on the Undead" was released.  His second book, this time written with Patrick Casey, "The World Reduced to Infographics: From Hollywood's Life Lessons and Doomed Cities of the U.S. to Sociopathic Cats and What Your Drink Order Says About You", was released December 13, 2011.

Nicholas Pinnock: Nicholas Andre Pinnock (born 2 September 1973) is a British actor.  He is known for his role as Frank Sutter in the Sky Atlantic psychological thriller "Fortitude".  Pinnock is currently starring in "Marcella" as Jason Backland.  The series aired on ITV on 4 April 2016.

Neil Godwin: Neil Godwin is a fictional character in the BBC sitcom, "The Office", played by Patrick Baladi.  Neil first appeared in the first episode of the second series of the show as the UK Manager of Wernham Hogg, newly promoted from manager of the Swindon branch, thus making him David Brent's new boss.  He was mentioned by name in some episodes of the first series but he did not make an appearance.

Tawny Moyer: Tawny Moyer, born March 30, 1957 to Neil and Harlene Moyer, is an American actress who starred in film and television.  She is likely best known for her role as Jill Franco, the nurse in the 1981 horror film "Halloween II".  Her first feature role was in the 1978 film "California Suite".  She is married to actor Patrick St. Esprit.

Question: What role did actor Patrick Baladi play in the ITV thriller Marcella available on Netflix?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The full name of the actor."
    },
    "series_name": {
      "type": "string",
      "description": "The name of the television series."
    },
    "role_played": {
      "type": "string",
      "description": "The character role played by the actor in the series."
    },
    "series_genre": {
      "type": "string",
      "description": "The genre of the television series."
    },
    "broadcasting_platforms": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of platforms where the series is broadcast or available."
    },
    "is_available_on_netflix": {
      "type": "boolean",
      "description": "Indicates if the series is available on Netflix."
    }
  },
  "required": [
    "actor_name",
    "series_name",
    "role_played",
    "series_genre",
    "broadcasting_platforms",
    "is_available_on_netflix"
  ],
  "additionalProperties": false
}

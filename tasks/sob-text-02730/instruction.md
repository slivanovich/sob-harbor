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
Hirohiko Araki: Hirohiko Araki (Japanese: 荒木 飛呂彦 , Hepburn: Araki Hirohiko , born June 7, 1960 in Sendai, Miyagi) is a Japanese manga artist.  He made his debut under the name Toshiyuki Araki (荒木 利之 , Araki Toshiyuki ) in 1980 with his one-shot "Poker Under Arms", and began his professional career with the short series "Cool Shock B.T.", "Baoh", and "The Gorgeous Irene".  Araki is best known for his long-running series "JoJo's Bizarre Adventure", first published in "Weekly Shōnen Jump" in 1986 and which to date has sold over 100 million copies in Japan alone, which is known for its frequent references to Western rock music and Italy, both of which Araki is reportedly very fond of.

Abiola Abrams: Abiola Abrams (born July 29, 1976) is an American TV host, Internet personality, personal coach, motivational speaker and author.  Her advice columns on topics such as relationships and self-worth include "Intimacy Intervention" on Essence.com and "Abiola’s Love Class" on MommyNoire.com.  She is the author of the self-esteem advice guide "The Official Bombshell Handbook: The 13 Sacred Secrets of Feminine Power" and "Dare", a love story retelling of "Faust" set in the hip hop world.  Abrams is also the creator of a lifestyle blog and web video series at AbiolaTV.com.

James Duval: James Edward Duval (born September 10, 1972) is an American actor, who is known for his roles in the Gregg Araki trilogy—"Totally Fucked Up, The Doom Generation," and "Nowhere"—in addition to Frank in "Donnie Darko", Blank in "May", Miguel in "Independence Day" and Singh in "Go".

Smiley Face (film): Smiley Face is a 2007 comedy film written by Dylan Haggerty and directed and co-produced by Gregg Araki.  It stars Anna Faris as a young woman who has a series of misadventures after eating a large number of cupcakes laced with cannabis.  The supporting cast includes Danny Masterson, John Krasinski, Adam Brody, Jayma Mays, Marion Ross, Jane Lynch, and Roscoe Lee Browne in his final film.  This was the ninth feature film directed by Araki.

Jump Tomorrow: Jump Tomorrow is a 2001 British independent romantic comedy film written and directed by Joel Hopkins, starring Tunde Adebimpe, Hippolyte Girardot, and Natalia Verbeke.  It concerns George (Adebimpe), a shy, bespectacled man who is about to marry a fellow Nigerian American woman named Sophie Ochenado, played by Abiola Abrams, when he falls for a Spanish woman.  It is based on a short film called "Jorge".  

Strand Releasing: Strand Releasing is a theatrical distribution company founded in 1989 and is based in Culver City, California.  The company has distributed over 300 auteur-driven titles from acclaimed international and American directors such as Apichatpong Weerasethakul, Gregg Araki, François Ozon, Jean-Luc Godard, Catherine Breillat, Claire Denis, Fatih Akin, Aki Kaurismaki, Claude Miller, Manoel de Oliveira, Gaspar Noe, Andre Techine and Terence Davies.

The Doom Generation: The Doom Generation is a 1995 American dark comedy film written and directed by Gregg Araki.  It stars James Duval, Rose McGowan, and Johnathon Schaech.  The film follows two troubled teenage lovers Amy Blue (McGowan) and Jordan White (Duval) who pick up a young handsome drifter named Xavier Red (Schaech).  After he accidentally kills a store's clerk, the trio embarks on a journey full of sex, violence, and people from Amy's past.  Billed as "A Heterosexual Movie by Gregg Araki", "The Doom Generation" is the second film in the director's trilogy known as the "Teenage Apocalypse Trilogy", the first being "Totally Fucked Up" (1993) and the last one "Nowhere" (1997).  The characters of Amy Blue and Jordan White are based on the Mark Beyer comic strip "Amy and Jordan".

Totally Fucked Up: Totally Fucked Up (censored title Totally F***ed Up in many references and publicity material) is a 1993 American drama film written and directed by Gregg Araki.  The first installment of Araki's Teenage Apocalypse Trilogy, it is considered a seminal entry in the New Queer Cinema genre.

Gregg Araki: Gregg Araki (born December 17, 1959) is an American filmmaker involved heavily with New Queer Cinema.  His film "Kaboom" was the first ever winner of the Cannes Film Festival Queer Palm awarded in 2010.

Mysterious Skin: Mysterious Skin is a 2004 Dutch-American drama film directed by American filmmaker Gregg Araki, who also wrote the screenplay based on Scott Heim's 1995 novel of the same name.  The film is Araki's eighth, premiering at the 61st Venice International Film Festival in 2004, although it was not more widely distributed until 2005.

Question: Who was born first out of Gregg Araki and Abiola Abrams?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_born_first": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "birth_date": {
          "type": "string",
          "format": "date"
        }
      },
      "required": [
        "name",
        "birth_date"
      ],
      "additionalProperties": false
    },
    "person_born_second": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "birth_date": {
          "type": "string",
          "format": "date"
        }
      },
      "required": [
        "name",
        "birth_date"
      ],
      "additionalProperties": false
    },
    "comparison_result": {
      "type": "string",
      "description": "States which person was born first."
    }
  },
  "required": [
    "person_born_first",
    "person_born_second",
    "comparison_result"
  ],
  "additionalProperties": false
}

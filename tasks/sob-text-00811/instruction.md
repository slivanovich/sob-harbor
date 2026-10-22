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
Kō Nishimura: Kō Nishimura (西村 晃 , Nishimura Kō , 25 January 1923 – 29 April 1997) was a Japanese actor who appeared in supporting roles in such films as Akira Kurosawa's "The Bad Sleep Well" and "Yojimbo", Kihachi Okamoto's "Sword of Doom", Yoshitaro Nomura's "Zero Focus", and Kon Ichikawa's "The Burmese Harp" (where he was credited as Akira Nishimura).

The Bad Sleep Well: The Bad Sleep Well (悪い奴ほどよく眠る , Warui yatsu hodo yoku nemuru ) is a 1960 film directed by the Japanese director Akira Kurosawa.  It was the first film to be produced under Kurosawa's own independent production company.  It was entered into the 11th Berlin International Film Festival.

Snow Trail: Snow Trail (Japanese: 銀嶺の果て , Hepburn: Ginrei no hate ) is a 1947 black-and-white Japanese film directed by Senkichi Taniguchi from Akira Kurosawa's screenplay.  It was the first film role for Toshirō Mifune, later to become one of Japan's most famous actors.  Mifune and the other main actor in the film, Takashi Shimura, later became long-term collaborators of film director Akira Kurosawa.

Dreams (1990 film): Dreams (夢 , Yume , aka Akira Kurosawa's Dreams) is a 1990 Japanese-American magical realism film of eight vignettes written and directed by Akira Kurosawa.  It was inspired by actual dreams that Kurosawa claimed to have had repeatedly.  It was his first film in 45 years on which he was the sole author of the screenplay.  It was made five years after "Ran", with assistance from George Lucas, Francis Ford Coppola, and Steven Spielberg, and funded by Warner Bros. The film was screened out of competition at the 1990 Cannes Film Festival, and to this day has received positive reviews.

A.K. (film): A.K. is a 1985 French documentary film directed by Chris Marker about the Japanese director Akira Kurosawa.  Though it was filmed while Kurosawa was working on "Ran", the film focuses more on Kurosawa's remote but polite personality than on the making of the film.  The film is sometimes seen as being reflective of Marker's fascination with Japanese culture, which he also drew on for one of his best-known films, "Sans Soleil".  The film was screened in the Un Certain Regard section at the 1985 Cannes Film Festival.

Akira Kurosawa Memorial Short Film Competition: The Akira Kurosawa Memorial Short Film Competition is a major international short film awards ceremony, run by the Akira Kurosawa Foundation.  Since the inaugural 2004-2005 competition, the Grand Prix and numerous other prizes have been awarded on an annual basis.

Kurosawa's Way: Kurosawa's Way (French: Kurosawa, la voie ) is a 2011 French documentary directed and written by Catherine Cadou.  The film features 11 major filmmakers from Asia, America and Europe as they discuss how the films of Japanese director Akira Kurosawa influenced them.

Hideo Oguni: Hideo Oguni (小国 英雄 , Oguni Hideo ) was a Japanese writer who wrote over 100 screenplays.  He is best known for co-writing screenplays for a number of films directed by Akira Kurosawa, including "Ikiru", "The Seven Samurai", "Throne of Blood" and "The Hidden Fortress".  His first film with Kurosawa was "Ikiru", and according to film professor Catherine Russell, it was Oguni who devised that film's two-part structure.  Film critic Donald Richie regarded him as the "humanist" among Kurosawa's writers.  In 2013, Oguni and frequent screenwriting collaborators Kurosawa, Shinobu Hashimoto and Ryuzo Kikushima were awarded the Jean Renoir Award by the Writers Guild of America West.

Isao Kimura: Isao Kimura (木村 功 , "Kimura Isao" , July 22, 1923 – June 4, 1981) , also known as Kō Kimura, was a Japanese actor.  He appeared in several films directed by Akira Kurosawa.  The first was "Stray Dog" (1949) as Yusa the criminal.  Perhaps his most notable role was in "Seven Samurai" as the youngest of the samurai, Katsushiro.

Susumu Fujita: Susumu Fujita (藤田 進|Fujita Susumu) (8 January 1912 – 23 March 1991) was a Japanese film and television actor.  He played the lead role in Akira Kurosawa's first feature, "Sanshiro Sugata", and appeared in other Kurosawa films including "The Men Who Tread On the Tiger's Tail" (as Togashi, commander of the border guards) and "The Hidden Fortress" (as General Tadokoro).  Later, he was a supporting actor in Ishirō Honda's "Mothra vs. Godzilla", among many other films.

Question: Kō Nishimura had a supporting role in this film by Akira Kurosawa that came out in what year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "role_type": {
          "type": "string",
          "enum": [
            "lead",
            "supporting"
          ]
        }
      },
      "required": [
        "name",
        "role_type"
      ],
      "additionalProperties": false
    },
    "film": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string"
        },
        "director": {
          "type": "string"
        },
        "release_year": {
          "type": "integer"
        }
      },
      "required": [
        "title",
        "director",
        "release_year"
      ],
      "additionalProperties": false
    },
    "question_answered": {
      "type": "boolean"
    }
  },
  "required": [
    "actor",
    "film",
    "question_answered"
  ],
  "additionalProperties": false
}
